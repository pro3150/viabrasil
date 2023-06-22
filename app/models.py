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
    created_at = Column(String)
    updated_at = Column(String)


class Cars(db.Model):

    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    plate = Column(String)
    brand = Column(String)
    model = Column(String)
    manufacture_year = Column(String)
    buy_price = Column(String)
    sell_price = Column(String)
    status = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    salesman_id = Column(Integer)


class Stock(db.Model):

    id = Column(Integer, primary_key=True)
    stock_moviment_id = Column(Integer)
    car_id = Column(Integer)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)


class StockMoviment(db.Model):

    id = Column(Integer, primary_key=True)
    text = Column(Integer)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)

