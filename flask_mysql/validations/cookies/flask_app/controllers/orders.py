from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import order

@app.route("/")
def home():
    return render_template("index.html", all_orders=order.Order.all())

@app.route("/orders")
def order_form():
    return render_template("create.html")
@app.route("/orders/<int:id>")
def edit_order_form(id):
    return render_template("edit.html", order=order.Order.get(id))

@app.route("/process", methods=["POST"])
def process():
    if request.form["which_form"] == "create":
        if not order.Order.validate_order(request.form):
            return redirect("/orders")
        else:
            order.Order.create(request.form)
            return redirect("/")
    elif request.form["which_form"] == "update":
        if not order.Order.validate_order(request.form):
            return redirect("/orders/"+ request.form["id"])
        else:
            order.Order.update(request.form)
            return redirect("/")
