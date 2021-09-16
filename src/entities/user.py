# coding=utf-8

from marshmallow import Schema, fields

from sqlalchemy import Column, String

from .entity import Entity, Base


class User(Entity, Base):
    __tablename__ = 'users'

    username = Column(String)
    description = Column(String)

    def __init__(self, username, description, created_by):
        Entity.__init__(self, created_by)
        self.username = username
        self.description = description

class UserSchema(Schema):
    id = fields.Number()
    username = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
