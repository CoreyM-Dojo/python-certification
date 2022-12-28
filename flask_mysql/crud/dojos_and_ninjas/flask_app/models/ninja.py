from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas"


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get(cls, id):
        data = {"id": id}
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return result[0]

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, dojo_id=%(dojo_id)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def destroy(cls, id):
        data = {"id": id}
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
