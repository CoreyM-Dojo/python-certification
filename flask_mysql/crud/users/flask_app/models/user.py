from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        return connectToMySQL("users_schema").query_db(query)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        return connectToMySQL("users_schema").query_db(query, data)[0]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL("users_schema").query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL("users_schema").query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL("users_schema").query_db(query, data)
