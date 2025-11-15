from app.models.user import User
from app import db

def create_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user