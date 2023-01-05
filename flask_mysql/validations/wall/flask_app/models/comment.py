from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import queries, user

db = "wall"
table = "comments"
class Comment:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.commenter = None
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = queries.create_query(table,data)
        return connectToMySQL(db).query_db(query, data)


