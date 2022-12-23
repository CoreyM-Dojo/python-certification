from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)


@app.route("/")
def home():
    all_users = User.get_all()
    return render_template("index.html", all_users=all_users)


@app.route("/users/create")
def create_user():
    return render_template("create_user.html")


@app.route("/users/update/<id>")
def update_user(id):
    user = User.get_one({"id": id})
    return render_template("update_user.html", user=user)


@app.route("/users/<id>")
def get_user(id):
    data = {"id": id}
    one_user = User.get_one(data)
    return render_template("one_user.html", user=one_user)


@app.route("/process", methods=["POST"])
def process():
    if request.form["which_form"] == "create":
        created_user_id = User.create(request.form)
        return redirect("/users/" + str(created_user_id))
    elif request.form["which_form"] == "update":
        print(request.form)
        # data = {
        #     "id": request.form["id"],
        #     "first_name": request.form["first_name"],
        #     "last_name": request.form["last_name"],
        #     "email": request.form["email"],
        # }
        User.update(request.form)
        return redirect("/users/" + request.form["id"])


@app.route("/users/delete/<id>")
def destroy_user(id):
    data = {"id": id}
    User.destroy(data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
