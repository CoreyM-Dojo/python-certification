from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models import recipe,user 

@app.route("/recipes", methods=["GET", "POST"])
def create_recipe():
    if not "logged_in" in session:
        return redirect("/")
    if request.method == "GET":
        return render_template("create.html", logged_in = user.User.get_by_id(session["logged_in"]) )
    elif request.method == "POST":
        if request.form["which_form"] == "create":
            print("Radio check:", request.form["under_30"])
            if not recipe.Recipe.validate_recipe(request.form):
                return redirect("/recipes")
            data = {
                "name": request.form["name"],
                "description": request.form["description"],
                "instructions": request.form["instructions"],
                "made_in": request.form["made_in"],
                "under_30": True if request.form["under_30"] == "Yes" else False,
                "users_id": request.form["users_id"]
            }
            recipe.Recipe.save(data)
            return redirect("/dashboard")
@app.route("/recipes/edit/<int:id>", methods=["GET", "POST"])
def edit_recipe(id):
    if not "logged_in" in session:
        return redirect("/")
    if request.method == "GET":
        recipe_from_db = recipe.Recipe.get(id)
        return render_template("edit.html", logged_in = user.User.get_by_id(session["logged_in"]), recipe=recipe_from_db )
    elif request.method == "POST":
        if request.form["which_form"] == "update":
            print("Radio check:", request.form["under_30"])
            if not recipe.Recipe.validate_recipe(request.form):
                return redirect("/recipes/edit/" + str(id))
            data = {
                "id": id,
                "name": request.form["name"],
                "description": request.form["description"],
                "instructions": request.form["instructions"],
                "made_in": request.form["made_in"],
                "under_30": True if request.form["under_30"] == "Yes" else False,
                "users_id": request.form["users_id"]
            }
            recipe.Recipe.update(data)
            return redirect("/dashboard")

@app.route("/recipes/<int:id>")
def show_recipe(id):
    if not "logged_in" in session:
        return redirect("/")
    recipe_from_db = recipe.Recipe.get(id)
    return render_template("show.html", recipe=recipe_from_db)

@app.route("/recipes/delete/<int:id>")
def destroy_recipe(id):
    if not "logged_in" in session:
        return redirect("/")
    recipe.Recipe.destroy(id)
    return redirect("/dashboard")

    