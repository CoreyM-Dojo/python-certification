from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import queries, user, comment
from flask import flash

db = "wall"
table = "posts"


class Post:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.poster = None
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.comments = []

    @classmethod
    def save(cls, data):
        query = queries.create_query(table, data)
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = queries.one_to_many("posts", "users")
        query += " ORDER BY posts.created_at DESC;"
        comments_query = "SELECT * FROM comments JOIN posts ON comments.posts_id = posts.id JOIN users ON comments.users_id = users.id;"
        comments = connectToMySQL(db).query_db(comments_query)
        result = connectToMySQL(db).query_db(query)
        all_posts = []
        for row in result:
            post = cls(row)
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
            }
            post.poster = user.User(user_data)
            comms = filter(lambda c: c["posts_id"] == post.id, comments)
            comms = list(comms)
            for c in comms:
                new_comment = comment.Comment(c)
                new_comment.commenter = user.User(
                    {
                        "id": c["users.id"],
                        "first_name": c["first_name"],
                        "last_name": c["last_name"],
                        "email": c["email"],
                        "password": c["password"],
                    }
                )
                post.comments.append(new_comment)
            all_posts.append(post)
            print("All posts:", all_posts)

        for post in all_posts:
            print("content:", post.content)
            print("comments:", post.comments)

        return all_posts

    @classmethod
    def destroy(cls, id):
        data = {"id": id}
        query = queries.delete_query(table)
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_post(post):
        is_valid = True
        if post["content"] == "":
            flash("Content must not be blank")
            is_valid = False
        return is_valid
