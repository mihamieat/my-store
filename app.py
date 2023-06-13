"""Main flask app for my store."""
from uuid import uuid4
from flask import Flask, request
from flask_smorest import abort
from db import stores, items


app = Flask(__name__)


@app.get("/store")
def get_stores():
    """Returns all stores."""
    return {"stores": list(stores.values())}


@app.get("/store/<string:sotre_id>")
def get_store(sotre_id):
    """Returns a specific store by its name."""
    try:
        return {"store": stores[sotre_id]}
    except KeyError:
        abort(404, message="Store not found,")


@app.post("/store")
def create_store():
    """Creates a new store."""
    req = request.get_json()
    if "name" not in req:
        abort(
            400,
            message="Bad request. Ensure 'name' \
is included in the JSON payload.",
        )
    for store in stores.values():
        if store["name"] == req["name"]:
            abort(400, message="Store already exists.")
    store_id = uuid4().hex
    store = {**req, "id": store_id}
    stores[store_id] = store
    return {"message": "Store created.", "store": store}, 201


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted."}
    except KeyError:
        abort(404, message="Store not found.")


@app.get("/items")
def get_items():
    """Returns items."""
    return {"items": list(items.values())}


@app.get("/item/<string:item_id>")
def get_items_in_store(item_id):
    """Returs items from a specific store."""
    try:
        return {"item": items[item_id]}
    except KeyError:
        abort(404, message="Item not found.")


@app.post("/item")
def create_item():
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


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted."}, 200
    except KeyError:
        abort(404, message="Item not found.")
