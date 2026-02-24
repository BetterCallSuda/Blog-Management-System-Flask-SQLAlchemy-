from flask import Flask, request, jsonify
from models import db, User, Post, Comment

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# -----------------------------
# CREATE USER
# -----------------------------
@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.get_json()

    user = User(
        username=data["username"],
        email=data["email"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"})


# -----------------------------
# CREATE POST
# -----------------------------
@app.route("/create_post", methods=["POST"])
def create_post():
    data = request.get_json()

    user = User.query.get(data["user_id"])

    if not user:
        return jsonify({"error": "User not found"}), 404

    post = Post(
        title=data["title"],
        content=data["content"],
        author=user
    )

    db.session.add(post)
    db.session.commit()

    return jsonify({"message": "Post created successfully"})


# -----------------------------
# ADD COMMENT
# -----------------------------
@app.route("/add_comment", methods=["POST"])
def add_comment():
    data = request.get_json()

    user = User.query.get(data["user_id"])
    post = Post.query.get(data["post_id"])

    if not user or not post:
        return jsonify({"error": "User or Post not found"}), 404

    comment = Comment(
        text=data["text"],
        user=user,
        post=post
    )

    db.session.add(comment)
    db.session.commit()

    return jsonify({"message": "Comment added successfully"})


# -----------------------------
# GET ALL POSTS
# -----------------------------
@app.route("/posts")
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])


if __name__ == "__main__":
    app.run(debug=True)
