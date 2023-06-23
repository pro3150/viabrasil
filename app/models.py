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


class Cars(db.Model):

    id = Column(Integer, primary_key=True)
    image_url = db.relationship('Img', backref='cars', lazy=True)
    plate = Column(String)
    brand = Column(String)
    model = Column(String)
    manufacture_year = Column(String)
    buy_price = Column(String)
    sell_price = Column(String)
    status = Column(String)
    created_at = Column(DateTime, server_default=db.func.now())
    updated_at = Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    salesman_id = Column(Integer)


class Img(db.Model):
    id = Column(Integer, primary_key=True)
    image = Column(String)
    name = Column(String)
    mimetype = Column(String)
    car_id = Column(Integer, db.ForeignKey('cars.id'), nullable=False)
    created_at = Column(DateTime, server_default=db.func.now())
    updated_at = Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class Stock(db.Model):

    id = Column(Integer, primary_key=True)
    stock_moviment_id = Column(Integer)
    car_id = Column(Integer)
    created_at = Column(DateTime, server_default=db.func.now())
    updated_at = Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class StockMoviment(db.Model):

    id = Column(Integer, primary_key=True)
    text = Column(Integer)
    created_at = Column(DateTime, server_default=db.func.now())
    updated_at = Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

