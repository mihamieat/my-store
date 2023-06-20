# -*- coding: utf-8 -*-
"""Store model."""

from db import db


class StoreModel(db.Model):
    """Store model."""

    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    items = db.relationship(
        "ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete"
    )
    tags = db.relationship(
        "TagModel", back_populates="store", lazy="dynamic", cascade="all, delete"
    )
