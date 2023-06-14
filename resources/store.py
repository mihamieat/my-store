# -*- coding: utf-8 -*-
"""Store API resource."""
from uuid import uuid4
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
    def post(self, store_data):
        """Creates a new store."""
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message="Store already exists.")

        store_id = uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store

        return store
