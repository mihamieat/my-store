# -*- coding: utf-8 -*-
"""Item models."""

from db import db


class ItemModel(db.Model):
    """Item model."""

    __table_name__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    store_id = db.Column(
        db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False
    )

    store = db.relationship("StoreModel", back_populates="items")
