# -*- coding: utf-8 -*-
"""Main flask app for my store."""
import os
from flask import Flask
from flask_smorest import Api
from db import db
import models  # noqa # pylint: disable=W0611
from resources.item import blueprint as ItemBlueprint
from resources.store import blueprint as StoreBlueprint


def create_app(db_url=None):
    """Create my Flask app."""

    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "My Store REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/\
swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)  # pylint: disable=E1120
    api = Api(app)

    with app.app_context():
        db.create_all()  # pylint: disable=E1120

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)

    return app
