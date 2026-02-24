from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# -----------------------------
# USER MODEL
# -----------------------------
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    posts = db.relationship("Post", back_populates="author", cascade="all, delete")
    comments = db.relationship("Comment", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"<User {self.username}>"
