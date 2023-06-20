# -*- coding: utf-8 -*-
"""API schema."""
from marshmallow import Schema, fields


class UserSchema(Schema):
    """User schema."""

    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class PlainItemSchema(Schema):
    """Plain item schema."""

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    """Plain store schema."""

    id = fields.Int(dump_only=True)
    name = fields.Str()


class PlainTagSchema(Schema):
    """Plain tag schema."""

    id = fields.Int(dump_only=True)
    name = fields.Str()


class ItemSchema(PlainItemSchema):
    """Item schema."""

    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainItemSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema(), dump_only=True))


class ItemUpdateSchema(Schema):
    """Item update schema."""

    name = fields.Str()
    price = fields.Float()


class StoreSchema(PlainStoreSchema):
    """Store schema."""

    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    """Tag schema."""

    store_id = fields.Int(load_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    store = fields.Nested(PlainStoreSchema, dump_only=True)


class TagAndItemSchema(Schema):
    """Tag and item schema."""

    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)
