from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.url import URL
from dotenv import load_dotenv
from models.setup import (
    db,
    setup_db,
    Users,
)
from models.checklists import (
    Checklist,
    ChecklistItem,
    ChecklistTemplate,
    ChecklistTemplateItem,
)
from models.stock import Car, Image, Stock, StockMoviment
from werkzeug.utils import secure_filename
import os


DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USERNAME")
DB_PASS = os.environ.get("DB_PASS")

app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
UPLOAD_FOLDER = "static/img_uploads/"
app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), UPLOAD_FOLDER)

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

@app.route("/stats/dados_frota")
def dados_frota():
    # Ensure the user reached path via GET
    if request.method == "GET":
        cars = Car.query.all()
        ano = 0
        preço_compra = 0 
        preço_venda = 0
        nb_cars = len(cars)
        for car in cars:
            ano = ano+int(car.manufacture_year)
            preço_compra = preço_compra +int(car.buy_price)
            preço_venda = preço_venda + int(car.sell_price)
        ano_medio = 2023 - int(ano/nb_cars)
        compra_medio = int(preço_compra/nb_cars)
        venda_medio = int(preço_venda/nb_cars)

        return render_template("stats_dados_frota.html", nb_cars = nb_cars, ano_medio=ano_medio, compra_medio=compra_medio, venda_medio=venda_medio)
    else:
        pass



@app.route("/checklist")
def checklist():
    # Ensure the user reached path via GET
    if request.method == "GET":
        checklist_items = ChecklistItem.query.all()
        return render_template("checklist.html", checklist_items=checklist_items)
    else:
        pass


@app.route("/checklist/create")
def checklist_create():
    # Ensure the user reached path via GET
    if request.method == "GET":
        checklist_templates = ChecklistTemplate.query.all()
        cars = Car.query.all()
        return render_template("checklist_create.html", checklist_templates=checklist_templates, cars=cars)
    else:
        pass


@app.route("/checklist/create/build")
def checklist_create_with_template():
    # Ensure the user reached path via GET
    if request.method == "GET":
        req = request.args
        car_id = req.get("car_id")
        #checklist_template = ChecklistTemplate.query.filter_by(id=checklist_template_id).first()
        return car_id#render_template("checklist_create_with_template.html", checklist_template=checklist_template)
    else:
        pass


@app.route("/checklist/template/create", methods=["GET", "POST"])
def checklist_template_create():
    if request.method == "GET":
        return render_template("checklist_template_create.html")
    else:
        form = request.form

        checklist_template = ChecklistTemplate(
            title=form["checklist_template_title"],
        )
        db.session.add(checklist_template)

        checklist_template_items_input = form.getlist("checklist_template_item")
        checklist_template_items_order_input = form.getlist(
            "checklist_template_item_order"
        )

        for item_input, item_order in zip(
            checklist_template_items_input, checklist_template_items_order_input
        ):
            checklist_template_item = ChecklistTemplateItem(
                checklist_template=checklist_template,
                text=item_input,
                order=item_order,
            )
            db.session.add(checklist_template_item)
        
        db.session.commit()

        return redirect(url_for("checklist_create"))


@app.route("/checklist/template/edit/<id>")
def checklist_template_edit(id):
    checklist_template_items = ChecklistTemplateItem.query.filter_by(
        ChecklistTemplateItem.checklist_template_id == id
    ).all()
    return checklist_template_items


@app.route("/stock")
def stock():
    if request.method == "GET":
        cars = Car.query.all()
        return render_template("stock.html", cars=cars)
    else:
        pass


@app.route("/cars/create", methods=["GET", "POST"])
def cars_create():
    # Ensure the user reached path via GET
    if request.method == "GET":
        return render_template("stock_create.html")
    else:
        form = request.form

        image_file = request.files["image"]
        image_filename = secure_filename(image_file.filename)
        image_mimetype = image_file.mimetype

        image_path = os.path.join(UPLOAD_FOLDER, image_filename)
        image_file.save(image_path)

        image = Image(
            image=image_path,
            name=image_filename,
            mimetype=image_mimetype,
        )

        car = Car(
            image=image,
            plate=form["plate"],
            brand=form["brand"],
            model=form["model"],
            manufacture_year=form["manufacture_year"],
            buy_price=form["buy_price"],
            sell_price=form["sell_price"],
            status=form["status"],
        )

        db.session.add_all([image, car])
        db.session.commit()

        return redirect(url_for("stock"))


@app.route("/cars/update/<id>", methods=["GET", "POST"])
def cars_update(id):
    if request.method == "GET":
        return render_template("stock_update.html", id=id)
    else:
        form = request.form
        car = Car.query.filter_by(id=id).first()
        if len(form["plate"]) !=0:
            car.plate = form["plate"]
        if len(form["brand"]) !=0:
            car.brand = form["brand"]
        if len(form["model"]) !=0:
            car.model = form["model"]
        if len(form["status"]) !=0:
            car.status = form["status"]
        if len(form["manufacture_year"]) !=0:
            car.manufacture_year = form["manufacture_year"]
        db.session.commit()
        return redirect(url_for("stock_operation", crud_message="car-update"))


@app.route("/cars/delete/<id>", methods=["GET", "POST"])
def cars_delete(id):
    if request.method == "GET":
        car = Car.query.filter_by(id=id).first()
        return render_template("stock_delete.html", car=car)
    else:
        car = Car.query.filter_by(id=id).first()
        car_image = Image.query.filter_by(id=car.image_id).first()
        db.session.delete(car)
        db.session.delete(car_image)
        db.session.commit()
        return redirect(url_for("stock_operation", crud_message="car-delete"))


@app.route("/stock/operation/<crud_message>", methods=["GET"])
def stock_operation(crud_message):
    return render_template("stock_crud_success.html", crud=crud_message), 200
