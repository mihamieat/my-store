# -*- coding: utf-8 -*-
"""Tags API resource."""

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.tags import TagModel
from models.store import StoreModel
from schemas import TagSchema

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


@blueprint.route("/tag/<string:tag_id>")
class Tag(MethodView):
    """Tags resource."""

    @blueprint.response(200, TagSchema)
    def get(self, tag_id):
        """Returns a specific tag."""
        tag = TagModel.query.get_or_404(tag_id)
        return tag
