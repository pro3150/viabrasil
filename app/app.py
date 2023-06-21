from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


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

@app.route('/stock.html')
def stock():
   # Ensure the user reached path via GET
   if request.method == "GET":
      return render_template("stock.html")

   else:
      pass # Pass is a Python way to say 'do nothing'
