from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class Users(db.Model):
    id: int
    username: str
    password: str

    id = db.Column('id', db.Integer, primary_key = True, autoincrement=True) 
    username = db.Column('username', db.String(100), unique = True)
    password = db.Column('password', db.String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password
