# -*- coding: utf-8 -*-
"""Store API resource."""
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models.store import StoreModel
from schemas import StoreSchema


blueprint = Blueprint("stores", __name__, description="Operations on stores")


@blueprint.route("/store/<string:store_id>")
class Store(MethodView):
    """Store API resource."""

    @blueprint.response(200, StoreSchema)
    def get(self, store_id):
        """Returns a store by its UUID."""
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        """Delete a store by its UUID."""
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted"}


@blueprint.route("/store")
class StoreList(MethodView):
    """Stores list API resource."""

    @blueprint.response(200, StoreSchema(many=True))
    def get(self):
        """Returns all stores."""
        return StoreModel.query.all()

    @blueprint.arguments(StoreSchema)
    @blueprint.response(201, StoreSchema)
    def post(self, data):
        """Creates a new store."""
        store = StoreModel(**data)

        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Store with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error has occurred creating store.")

        return store
