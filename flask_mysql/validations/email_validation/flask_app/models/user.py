from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]

    @classmethod
    def all(cls):
        query = "SELECT * FROM users"
        return connectToMySQL("validations").query_db(query);

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL("validations").query_db(query, data)

    @staticmethod
    def validate_user(user):
        query = "Select * FROM users WHERE email = %(email)s;"
        user_list = connectToMySQL("validations").query_db(query, user)
        print(user_list)
        is_valid= True
        if len(user["first_name"]) < 2:
            flash("First name is required and needs to be at least 2 characters long")
            is_valid = False
        if len(user["last_name"]) < 2:
            flash("Last name is required and needs to be at least 2 characters long")
            is_valid = False
        if not REGEX.match(user["email"]):
            flash("Invalid email format")
            is_valid = False
        if len(user_list) > 0:
            flash("Email must be unique")
            is_valid = False
        return is_valid
        