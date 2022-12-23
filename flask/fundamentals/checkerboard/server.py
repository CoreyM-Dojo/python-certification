from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", row=4, col=4, color1="black", color2="red")


@app.route("/<int:x>")
def rows(x):
    return render_template("index.html", row=int(x / 2), col=4)


@app.route("/<int:x>/<int:y>")
def rows_and_columns(x, y):
    return render_template("index.html", row=int(x / 2), col=int(y / 2))


@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def variety_board(x, y, color1, color2):
    return render_template(
        "index.html", row=int(x / 2), col=int(y / 2), color1=color1, color2=color2
    )


if __name__ == "__main__":
    app.run(debug=True)
