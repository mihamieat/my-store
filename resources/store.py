# -*- coding: utf-8 -*-
"""Store API resource."""
from uuid import uuid4
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema


blueprint = Blueprint("stores", __name__, description="Operations on stores")


@blueprint.route("/store/<string:store_id>")
class Store(MethodView):
    """Store API resource."""

    def get(self, store_id):
        """Returns a store by its UUID."""
        try:
            store = stores[store_id]
            return {"store": store}, 200
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id):
        """Delete a store by its UUID."""
        try:
            del stores[store_id]
            return {"message": "Store deleted"}, 201
        except KeyError:
            abort(404, message="Store not found")


@blueprint.route("/store")
class StoreList(MethodView):
    """Stores list API resource."""

    def get(self):
        """Returns all stores."""
        return {"stores": list(stores.values())}

    @blueprint.arguments(StoreSchema)
    def post(self):
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
