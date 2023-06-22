from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import db, Users, Cars, Stock, StockMoviment, setup_db
import os

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USERNAME")
DB_PASS = os.getenv("DB_PASS")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
db.init_app(app)
setup_db(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def inicio():
    return render_template('index.html')

@app.route('/stats.html')
def stats():
   # Ensure the user reached path via GET
   if request.method == "GET":
      return render_template("stats.html")

   else:
      pass # Pass is a Python way to say 'do nothing'

@app.route('/operations.html')
def operations():
   # Ensure the user reached path via GET
   if request.method == "GET":
      return render_template("operations.html")

   else:
      pass # Pass is a Python way to say 'do nothing'

@app.route('/stock')
def stock():
   # Ensure the user reached path via GET
   if request.method == "GET":
      db.get_or_404(Cars, 1)
      return render_template("stock.html")

   else:
      pass # Pass is a Python way to say 'do nothing'


@app.route('/cars/add', methods=['GET'])
def cars():
   # Ensure the user reached path via GET
   if request.method == "GET":
      # car = Cars(
      #    id = "1"
      # )
      # db.session.add(car)
      # db.session.commit()
      cars = Cars.query.all()
      print(cars[0].plate)
      # cars = db.get_or_404(Cars, 1)
      # print(cars[0])
      return render_template("stock.html")

   else:
      pass # Pass is a Python way to say 'do nothing'