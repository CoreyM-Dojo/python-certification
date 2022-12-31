from flask_app import app
from flask import request, redirect, render_template
from flask_app.models import book, author


@app.route("/")
def index():
    return redirect("/books")


@app.route("/books")
def book_form():
    all_books = book.Book.all()
    return render_template("books/create.html", all_books=all_books)


@app.route("/books/<int:id>")
def show_book(id):
    one_book = book.Book.get(id)
    all_authors = author.Author.unfavorited(one_book.id)
    return render_template("books/show.html", book=one_book, all_authors=all_authors)


@app.route("/books/process", methods=["POST"])
def process_book():
    book.Book.create(request.form)
    return redirect("/")


@app.route("/books/add", methods=["POST"])
def add_authors():
    book.Book.add_to_favorites(request.form)
    return redirect("/books/" + request.form["book_id"])
