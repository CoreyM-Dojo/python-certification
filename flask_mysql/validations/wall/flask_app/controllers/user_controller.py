from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models import user,post
bcrypt = Bcrypt(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "logged_in" not in session:
        return redirect("/")
    logged_in = user.User.get_by_id(session["logged_in"])
    logged_in = user.User(logged_in)
    all_posts = post.Post.get_all()
    return render_template("dashboard.html", user_name=(logged_in.first_name + " " + logged_in.last_name), user_id=logged_in.id, all_posts=all_posts)

@app.route("/process", methods=["POST"])
def process():
    if request.form["which_form"] == "registration":
        if not user.User.validate_user(request.form):
            return redirect("/")
        else:
            data = {
                "first_name": request.form["first_name"],
                "last_name": request.form["last_name"],
                "email": request.form["email"],
                "password": bcrypt.generate_password_hash(request.form["password"])
            }
            logged_in = user.User.save(data)
            print("User id", logged_in)
            session["logged_in"] = logged_in
            return redirect("/dashboard")
    elif request.form["which_form"] == "login":
        if not user.User.validate_login(request.form):
            return redirect("/")
        else:
            logged_in = user.User.get_by_email(request.form["email"])
            session["logged_in"] = logged_in.id
            return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


