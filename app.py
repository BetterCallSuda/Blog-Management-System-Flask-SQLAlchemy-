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

