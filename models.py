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


    def to_dict(self):
            return {
                "id": self.id,
                "username": self.username,
                "email": self.email
            }


# -----------------------------
# POST MODEL
# -----------------------------
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = db.relationship("User", back_populates="posts")

    comments = db.relationship("Comment", back_populates="post", cascade="all, delete")

    def __repr__(self):
        return f"<Post {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author.username,
            "created_at": self.created_at,
            "comments": [comment.to_dict() for comment in self.comments]
        }
