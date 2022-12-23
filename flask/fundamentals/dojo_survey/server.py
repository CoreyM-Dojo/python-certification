from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key = "flubbernuggets"


@app.route("/")
def survey():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    print(request.form)
    print(request.form.getlist("education"))
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["favorite_language"] = request.form["favorite_language"]
    session["comment"] = request.form["comment"]
    session["chocolate"] = request.form["chocolate"]
    session["education"] = request.form.getlist("education")

    return redirect("/result")


@app.route("/result")
def result():
    return render_template(
        "result.html",
        name=session["name"],
        location=session["location"],
        favorite_language=session["favorite_language"],
        comment=session["comment"]
        if session["comment"] != "" and "comment" in session
        else "No comment",
        chocolate=session["chocolate"],
        education=session["education"],
    )


if __name__ == "__main__":
    app.run(debug=True)
