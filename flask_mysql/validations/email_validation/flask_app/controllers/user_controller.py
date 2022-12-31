from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user

@app.route("/")
def home():
    all_users = user.User.all()
    return render_template("index.html", all_users=all_users)
@app.route("/users")
def user_form():
    return render_template("create.html")
@app.route("/process", methods=["POST"])
def process():
    if not user.User.validate_user(request.form):
        return redirect("/users")
    else:
        user.User.create(request.form)
        return redirect("/")