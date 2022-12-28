from flask_app import app
from flask import render_template, redirect
from flask_app.models import dojo, ninja


@app.route("/ninjas")
def add_ninja():
    return render_template("ninja/ninja.html", all_dojos=dojo.Dojo.all())


@app.route("/ninjas/update/<int:id>")
def edit_ninja(id):
    return render_template(
        "ninja/edit_ninja.html", all_dojos=dojo.Dojo.all(), ninja=ninja.Ninja.get(id)
    )


@app.route("/ninjas/delete/<int:id>")
def destroy_ninja(id):
    ninja.Ninja.destroy(id)
    return redirect("/")
