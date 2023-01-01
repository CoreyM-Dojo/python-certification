from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
db = "cookies"
class Order:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.cookie_type = data["cookie_type"]
        self.num_of_boxes = data["num_of_boxes"]

    @classmethod
    def all(cls):
        query = "SELECT * FROM orders;"
        return connectToMySQL(db).query_db(query)

    @classmethod
    def get(cls, id):
        data = {
            "id": id
        }
        query = "SELECT * FROM orders WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)[0]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO orders (name, cookie_type, num_of_boxes) VALUES (%(name)s,%(cookie_type)s,%(num_of_boxes)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "Update orders SET name=%(name)s, cookie_type=%(cookie_type)s, num_of_boxes=%(num_of_boxes)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_order(order):
        is_valid=True

        if len(order["name"]) < 2:
            flash("Name is required and must contain at least 2 characters")
            is_valid = False
        if len(order["cookie_type"]) < 2:
            flash("Cookie type is required and must contain at least 2 characters")
            is_valid = False
        if int(order["num_of_boxes"]) < 0:
            flash("Must have a positive number of boxes")
            is_valid = False
        return is_valid
