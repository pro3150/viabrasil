import os
from sqlalchemy import Column, Integer, String, DateTime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def setup_db(app, db):
    with app.app_context():
        db.create_all()


class Users(db.Model):

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime, server_default=db.func.now())
    updated_at = Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

