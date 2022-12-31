from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

db = "books"


class Author:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.books = []

    @classmethod
    def all(cls):
        query = "SELECT * FROM authors;"
        return connectToMySQL(db).query_db(query)

    @classmethod
    def unfavorited(cls, id):
        data = {"id": id}
        query = "SELECT * FROM authors WHERE authors.id NOT IN (SELECT authors_id FROM favorites WHERE books_id = %(id)s)"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get(cls, id):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.authors_id LEFT JOIN books ON books.id = favorites.books_id WHERE authors.id = %(id)s;"
        data = {"id": id}
        result = connectToMySQL(db).query_db(query, data)
        author = cls(result[0])
        for row in result:
            print("check", row)
            book_data = {
                "id": row["books.id"],
                "title": row["title"],
                "num_of_pages": row["num_of_pages"],
            }
            author.books.append(book.Book(book_data))
        return author

    @classmethod
    def create(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        connectToMySQL(db).query_db(query, data)

    @classmethod
    def add_to_favorites(cls, data):
        query = "INSERT INTO favorites (authors_id, books_id) VALUES (%(book_id)s, %(author_id)s);"
        return connectToMySQL(db).query_db(query, data)
