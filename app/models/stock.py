from sqlalchemy import Column, Integer, String, DateTime, Boolean
from models.setup import db


class Car(db.Model):

    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, db.ForeignKey('image.id'))
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


class Image(db.Model):
    id = Column(Integer, primary_key=True)
    image = Column(String)
    name = Column(String)
    mimetype = Column(String)
    created_at = Column(DateTime, server_default=db.func.now())
    updated_at = Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    cars = db.relationship('Car', backref='image', lazy=True)


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
