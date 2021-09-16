from sqlalchemy import Column, String

from .entity import Entity, Base


class User(Entity, Base):
    __tablename__ = 'exams'

    username = Column(String)
    description = Column(String)

    def __init__(self, username, description, created_by):
        Entity.__init__(self, created_by)
        self.username = username
        self.description = description