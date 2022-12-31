from flask_app import app
from flask import request, redirect, render_template
from flask_app.models import author, book


@app.route("/authors")
def author_form():
    all_authors = author.Author.all()
    return render_template("authors/create.html", all_authors=all_authors)


@app.route("/authors/<int:id>")
def show_author(id):
    one_author = author.Author.get(id)
    all_books = book.Book.unfavorited(one_author.id)
    print(one_author)
    return render_template(
        "authors/show.html", one_author=one_author, all_books=all_books
    )


@app.route("/authors/process", methods=["POST"])
def process_author():
    author.Author.create(request.form)
    return redirect("/authors")


@app.route("/authors/add", methods=["POST"])
def add_books():
    author.Author.add_to_favorites(request.form)
    return redirect("/authors/" + request.form["author_id"])
