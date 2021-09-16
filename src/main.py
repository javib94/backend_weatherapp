# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.user import User

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
users = session.query(User).all()

if len(users) == 0:
    # create and persist mock user
    python_user = User("SQLAlchemy User", "Test your knowledge about SQLAlchemy.", "script")
    session.add(python_user)
    session.commit()
    session.close()

    # reload users
    users = session.query(User).all()

# show existing users
print('### Users:')
for user in users:
    print(f'({user.id}) {user.username} - {user.description}')