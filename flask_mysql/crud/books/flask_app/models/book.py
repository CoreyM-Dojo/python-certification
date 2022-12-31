from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

db = "books"


class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.authors = []

    @classmethod
    def all(cls):
        query = "SELECT * FROM books;"
        return connectToMySQL(db).query_db(query)

    @classmethod
    def unfavorited(cls, id):
        data = {"id": id}
        query = "SELECT * FROM books WHERE books.id NOT IN (SELECT books_id FROM favorites WHERE authors_id = %(id)s)"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get(cls, id):
        query = "SELECT * FROM books LEFT JOIN favorites on books.id = favorites.Books_id LEFT JOIN authors ON authors.id = favorites.authors_id WHERE books.id = %(id)s;"
        data = {"id": id}
        result = connectToMySQL(db).query_db(query, data)
        book = cls(result[0])
        for row in result:
            author_data = {"id": row["authors.id"], "name": row["name"]}
            book.authors.append(author.Author(author_data))

        return book

    @classmethod
    def create(cls, data):

        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        connectToMySQL(db).query_db(query, data)

    @classmethod
    def add_to_favorites(cls, data):
        query = "INSERT INTO favorites (authors_id, books_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(db).query_db(query, data)
