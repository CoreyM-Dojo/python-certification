from flask_app import app
from flask import redirect, session, request
from flask_app.models import post

@app.route("/posts", methods=["POST"])
def create_post():
    if not post.Post.validate_post(request.form):
        return redirect("/dashboard")
    else:
        post.Post.save(request.form)
        return redirect("/dashboard")

@app.route("/posts/<int:id>")
def destroy_post(id):
    post.Post.destroy(id)
    return redirect("/dashboard")