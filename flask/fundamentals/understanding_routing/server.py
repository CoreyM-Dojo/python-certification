from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"


@app.route("/dojo")
def hello_dojo():
    return "Dojo"


@app.route("/say/<string:word>")
def say(word):
    return "Hi " + word + "!"


@app.route("/repeat/<int:num>/<string:word>")
def repeat(num, word):
    return (word + " ") * num


@app.errorhandler(404)
def handle_404(e):
    return "Sorry! No response. Try Again!"


if __name__ == "__main__":
    app.run(debug=True)
