from app.basemodel import BaseModel
from app.extensions import db


class UserModel(BaseModel):
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer())

    def __repr__(self):
        return f"{self.__class__.__name__} - {self.id} : {self.username}"
