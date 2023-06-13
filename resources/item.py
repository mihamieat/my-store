"""Items API resource. """
from uuid import uuid4
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items


blueprint = Blueprint("Items", __name__, description="Operations on items.")


@blueprint.route("/item/<string:item_id>")
class Item(MethodView):
    """Items API resource."""
    def get(self, item_id):
        """Returns an intem by its id."""
        try:
            item = items[item_id]
            return {"item": item}
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        """Deletes an item by its id."""
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found")


@blueprint.route("/item")
class ItemList(MethodView):
    """Items list API resource."""
    def get(self):
        """Returns all items."""
        return {"items": list(items.values())}

    def post(self):
        """Creates a new item in a specified store."""
        item_data = request.get_json()
        if (
            "price" not in item_data
            or "store_id" not in item_data
            or "name" not in item_data
        ):
            abort(
                400,
                message="Bad request. Ensure 'price', 'store_id', \
and 'name' are included in the JSON payload.",
            )
        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message="Item already exists.")

        item_id = uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item
