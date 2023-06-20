# -*- coding: utf-8 -*-
"""Items API resource. """
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.item import ItemModel
from schemas import ItemSchema, ItemUpdateSchema


blueprint = Blueprint("Items", __name__, description="Operations on items.")


@blueprint.route("/item/<string:item_id>")
class Item(MethodView):
    """Items API resource."""

    @jwt_required()
    @blueprint.response(200, ItemSchema)
    def get(self, item_id):
        """Returns an intem by its id."""
        item = ItemModel.query.get_or_404(item_id)
        return item

    @blueprint.arguments(ItemUpdateSchema)
    @blueprint.response(200, ItemSchema)
    def put(self, item_data, item_id):
        """Update an existing item."""
        item = ItemModel.query.get_or_404(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

    @jwt_required()
    def delete(self, item_id):
        """Deletes an item by its id."""
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(403, message="Admin privilege required")
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}


@blueprint.route("/item")
class ItemList(MethodView):
    """Items list API resource."""

    @jwt_required()
    @blueprint.response(200, ItemSchema(many=True))
    def get(self):
        """Returns all items."""
        return ItemModel.query.all()

    @jwt_required(fresh=True)
    @blueprint.arguments(ItemSchema)
    @blueprint.response(201, ItemSchema)
    def post(self, data):
        """Creates a new item in a specified store."""
        item = ItemModel(**data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item")

        return item
