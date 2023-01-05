from flask_app import app
from flask import redirect, request
from flask_app.models import comment

@app.route("/comments", methods=["POST"])
def create_comment():
    comment.Comment.save(request.form)
    return redirect("/dashboard")