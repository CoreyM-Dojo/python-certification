from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

db = "dojos_and_ninjas"


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.ninjas = []

    @classmethod
    def all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL(db).query_db(query)
        return result

    @classmethod
    def with_ninjas(cls, id):
        data = {"dojo_id": id}
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;"

        result = connectToMySQL(db).query_db(query, data)
        dojo = cls(result[0])
        for row in result:
            ninja_data = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    @classmethod
    def save(cls, data):
        query = "INSERT into dojos (name) VALUES (%(name)s);"
        return connectToMySQL("dojos_and_ninjas").query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "Update dojos SET name=%(name)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
