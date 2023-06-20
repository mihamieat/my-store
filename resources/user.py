# -*- coding: utf-8 -*-
"""User resources."""
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.user import UserModel
from schemas import UserSchema

blueprint = Blueprint("Users", "users", description="Operations on users.")


@blueprint.route("/register")
class UserRegister(MethodView):
    """User registration resource."""

    @blueprint.arguments(UserSchema)
    @blueprint.response(201, UserSchema)
    def post(self, data):
        """Create a new user."""
        if UserModel.query.filter(UserModel.username == data["username"]).first():
            abort(409, message="User with that name already exists.")
        user = UserModel(
            username=data["username"],
            password=pbkdf2_sha256.hash(data["password"]),
        )

        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as err:
            abort(500, message=str(err))

        return user


@blueprint.route("/login")
class UserLogin(MethodView):
    """User login resource."""

    @blueprint.arguments(UserSchema)
    def post(self, data):
        """Login with user credentials."""
        user = UserModel.query.filter(UserModel.username == data["username"]).first()

        password = pbkdf2_sha256.hash(data["password"])

        if user and pbkdf2_sha256.verify(data["password"], password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")


@blueprint.route("/user/<int:user_id>")
class User(MethodView):
    """
    This resource can be useful when testing our Flask app.
    We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful
    when we are manipulating data regarding the users.
    """

    @blueprint.response(200, UserSchema)
    def get(self, user_id):
        """Returns a user by its id."""
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        """Delete a specific user by its id."""
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User successfully deleted."}, 200
