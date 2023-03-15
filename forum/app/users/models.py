from app.basemodel import BaseModel
from app.extensions import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))


class UserModel(BaseModel, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.__class__.__name__} - {self.id} : {self.username}"


class UserFollow(BaseModel, UserMixin):
    follower_id = db.Column(db.Integer)
    followed_id = db.Column(db.Integer)
    followed_at = db.Column(db.DateTime, default=db.func.current_timestamp())
