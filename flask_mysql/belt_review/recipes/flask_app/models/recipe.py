from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, queries
from flask import flash
db = "recipes"
table ="recipes"
class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.made_in = data["made_in"]
        self.under_30 = data["under_30"]
        self.creator = None

    @classmethod
    def save(cls, data):
        query = queries.create_query(table, data)
        print(query)
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = queries.one_to_many("recipes","users", False, True)
        results = connectToMySQL(db).query_db(query)
        all_recipes = []
        for row in results:
            recipe = cls(row)
            recipe.creator = user.User({
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password" : row["password"]
            })
            all_recipes.append(recipe)
        return all_recipes

    @classmethod
    def get(cls, id):
        data = {"id": id}
        query = queries.one_to_many("recipes",  "users", True, True)
        result = connectToMySQL(db).query_db(query, data)
        print(result)
        recipe = cls(result[0])
        recipe.creator = user.User({
                "id": result[0]["users.id"],
                "first_name": result[0]["first_name"],
                "last_name": result[0]["last_name"],
                "email": result[0]["email"],
                "password" : result[0]["password"]
            })
        return recipe

    @classmethod
    def update(cls, data):
        query = queries.update_query(table, data)
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def destroy(cls,id):
        data ={"id": id}
        query = queries.delete_query(table)
        return connectToMySQL(db).query_db(query, data)


    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe["name"]) < 2:
            flash("Name field is required and must have at least 2 characters")
            is_valid = False
        if len(recipe["description"]) < 2:
            flash("Description field is required and must have at least 2 characters")
            is_valid = False
        if len(recipe["instructions"]) < 2:
            flash("Instructions field is required and must have at least 2 characters")
            is_valid = False
        if not recipe["made_in"]:
            flash("Date is required")
            is_valid = False
        if not recipe["under_30"]:
            flash("Is your recipe made in under 30 minutes? We need to know")
            is_valid=False
        return is_valid


    

