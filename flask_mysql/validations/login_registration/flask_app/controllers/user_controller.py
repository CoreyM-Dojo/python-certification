from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
bcrypt = Bcrypt(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "logged_in" not in session:
        return redirect("/")
    user = User.get_by_id(session["logged_in"])
    user = User(user)
    return render_template("dashboard.html", user_name=(user.first_name + " " + user.last_name))

@app.route("/process", methods=["POST"])
def process():
    if request.form["which_form"] == "registration":
        if not User.validate_user(request.form):
            return redirect("/")
        else:
            data = {
                "first_name": request.form["first_name"],
                "last_name": request.form["last_name"],
                "email": request.form["email"],
                "password": bcrypt.generate_password_hash(request.form["password"])
            }
            logged_in = User.save(data)
            session["logged_in"] = logged_in
            return redirect("/dashboard")
    elif request.form["which_form"] == "login":
        if not User.validate_login(request.form):
            return redirect("/")
        else:
            logged_in = User.get_by_email(request.form["email"])
            session["logged_in"] = logged_in.id
            return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


