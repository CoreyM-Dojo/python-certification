from flask import Flask, request, redirect, render_template, session
import base64

app = Flask(__name__)

app.secret_key = "fluffernuggets"


@app.route("/")
def home():
    if "visited" not in session:
        session["visited"] = 1
        session["count"] = 1
    else:
        session["visited"] += 1
        session["count"] += 1
    return render_template("index.html", count=session["count"])


@app.route("/add/<int:x>")
def add_2(x=2):
    if "count" in session:
        session["visited"] += 1
        session["count"] += x
    else:
        session["count"] = 1
        session["visited"] += 1
        session["count"] += x
    return render_template("index.html", count=session["count"])


@app.route("/add", methods=["POST"])
def process_add():
    return redirect("/add/" + request.form["num"])


@app.route("/session/destroy")
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
