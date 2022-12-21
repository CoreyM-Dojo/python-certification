from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/play")
def play():
    return render_template("index.html", num=3, color="cyan")


@app.route("/play/<int:num>")
def play_num(num):
    return render_template("index.html", num=num, color="cyan")


@app.route("/play/<int:num>/<color>")
def play_num_color(num, color):
    return render_template("index.html", num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)
