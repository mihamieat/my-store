# -*- coding: utf-8 -*-
"""Tags API resource."""

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.tag import TagModel
from models.store import StoreModel
from models.item import ItemModel
from models.item_tags import ItemTagsModel  # noqa # pylint: disable=W0611
from schemas import TagSchema, TagAndItemSchema

blueprint = Blueprint("Tags", "tags", description="Operations on tags.")


@blueprint.route("/store/<string:store_id>/tag")
class TagInStore(MethodView):
    """Tags by store_id resource."""

    @blueprint.response(200, TagSchema(many=True))
    def get(self, store_id):
        """Returns a tag."""
        store = StoreModel.query.get_or_404(store_id)
        tags = store.tags.all()
        return tags

    @blueprint.arguments(TagSchema)
    @blueprint.response(201, TagSchema)
    def post(self, data, store_id):
        """Create a new tag if it doesn't already exist in a store."""
        if TagModel.query.filter(
            TagModel.store_id == store_id, TagModel.name == data["name"]
        ).first():
            abort(400, message="A tag with name already exists in that store.")
        tag = TagModel(**data, store_id=store_id)

        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as err:
            abort(500, message=str(err))

        return tag


@blueprint.route("/item/<string:item_id>/tag/<string:tag_id>")
class LinkTagsToItem(MethodView):
    """Link tags to item resource."""

    @blueprint.response(200, TagSchema)
    def post(self, item_id, tag_id):
        """Create a link between tag and item."""
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.append(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return tag

    @blueprint.response(200, TagAndItemSchema)
    def delete(self, item_id, tag_id):
        """Delete a link between tag and item."""
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return {"message": "Item removed from tag", "Item": item, "Tag": tag}


@blueprint.route("/tag/<string:tag_id>")
class Tag(MethodView):
    """Tags resource."""

    @blueprint.response(200, TagSchema)
    def get(self, tag_id):
        """Returns a specific tag."""
        tag = TagModel.query.get_or_404(tag_id)
        return tag

    @blueprint.response(
        202,
        description="Deletes a tag if no item is tagged with it.",
        example={"message": "Tag deleted."},
    )
    @blueprint.alt_response(404, description="Tag not found.")
    @blueprint.alt_response(
        400,
        description="Returned if the tag is assigned to one or more items.\
In this case, the tag is not deleted.",
    )
    def delete(self, tag_id):
        """Deletes a specific tag."""
        tag = TagModel.query.get_or_404(tag_id)

        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "Tag deleted"}
        abort(
            400,
            message="Could not delete tag. Make sure tag is not associated with any items, then try again.",
        )
