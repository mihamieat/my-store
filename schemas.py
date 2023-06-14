# -*- coding: utf-8 -*-
"""API schema."""
from marshmallow import Schema, fields


class StoreSchema(Schema):
    """Store schema."""

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class ItemSchema(Schema):
    """Item schema."""

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    """Item update schema."""

    name = fields.Str()
    price = fields.Float()
