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
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
db.init_app(app)
setup_db(app, db)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/index")
def inicio():
    return render_template("index.html")


@app.route("/stats")
def stats():
    # Ensure the user reached path via GET
    if request.method == "GET":
        return render_template("stats.html")

    else:
        pass  # Pass is a Python way to say 'do nothing'


@app.route("/checklist")
def checklist():
    # Ensure the user reached path via GET
    if request.method == "GET":
        return render_template("checklist.html")

    else:
        pass  # Pass is a Python way to say 'do nothing'


@app.route("/stock")
def stock():
    # Ensure the user reached path via GET
    if request.method == "GET":
        cars = Cars.query.all()
        return render_template("stock.html", cars=cars)

    else:
        pass  # Pass is a Python way to say 'do nothing'


@app.route("/cars", methods=["GET"])
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
        return render_template("stock.html", cars=cars)

    else:
        pass  # Pass is a Python way to say 'do nothing'


@app.route("/cars/create", methods=["GET", "POST"])
def cars_create():
    # Ensure the user reached path via GET
    if request.method == "GET":
        return render_template("stock_create.html")
    else:
        form = request.form

        car = Cars(
            plate=form["plate"],
            brand=form["brand"],
            model=form["model"],
            manufacture_year=form["manufacture_year"],
            buy_price=form["buy_price"],
            sell_price=form["sell_price"],
            status=form["status"],
        )

        db.session.add(car)
        db.session.commit()

        return render_template("stock_crud_success.html", crud="car-create")


@app.route("/cars/update/<id>", methods=["GET", "POST"])
def cars_update(id):
    if request.method == "GET":
        return render_template("stock_update.html", id=id)
    else:
        form = request.form
        car = Cars.query.filter_by(id=id).first()
        car.plate = form["plate"]
        car.brand = form["brand"]
        car.model = form["model"]
        car.manufacture_year = form["manufacture_year"]
        db.session.commit()
        return redirect(url_for("stock_operation", crud_message="car-update"))


@app.route("/cars/delete/<id>", methods=["GET", "POST"])
def cars_delete(id):
    if request.method == "GET":
        car = Cars.query.filter_by(id=id).first()
        return render_template("stock_delete.html", car=car)
    else:
        car = Cars.query.filter_by(id=id).first()
        db.session.delete(car)
        db.session.commit()
        return redirect(url_for("stock_operation", crud_message="car-delete"))


@app.route("/stock/operation/<crud_message>", methods=["GET"])
def stock_operation(crud_message):
    return render_template("stock_crud_success.html", crud=crud_message), 200
