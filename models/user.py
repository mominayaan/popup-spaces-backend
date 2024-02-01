from mongoengine import *
from models.base_model import BaseModel


class User(BaseModel):
    username: str = StringField(required=True, unique=True)

    meta = {"indexes": ["username"], "collection": "user"}
