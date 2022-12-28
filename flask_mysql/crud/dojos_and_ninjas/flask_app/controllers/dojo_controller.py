from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo, ninja


@app.route("/")
def home():
    return render_template("dojo/index.html", all_dojos=dojo.Dojo.all())


@app.route("/dojos/<int:id>")
def dojo_page(id):
    return render_template("dojo/dojo.html", dojo=dojo.Dojo.with_ninjas(id))


@app.route("/dojos/update/<int:id>")
def edit_dojo(id):
    return render_template("dojo/edit_dojo.html", dojo=dojo.Dojo.with_ninjas(id))


@app.route("/dojos/delete/<int:id>")
def destroy_dojo(id):
    dojo.Dojo.destroy({"id": id})
    return redirect("/")


@app.route("/process", methods=["POST"])
def process():
    if request.form["which_form"] == "dojo":
        dojo.Dojo.save(request.form)
    elif request.form["which_form"] == "ninja":
        ninja.Ninja.save(request.form)
    elif request.form["which_form"] == "edit_dojo":
        dojo.Dojo.update(request.form)
    elif request.form["which_form"] == "edit_ninja":
        ninja.Ninja.update(request.form)
    return redirect("/")
