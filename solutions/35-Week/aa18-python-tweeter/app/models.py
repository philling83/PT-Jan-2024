from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tweet(db.Model):
  __tablename__ = "tweets"

  id = db.Column(db.Integer, primary_key=True)
  tweet = db.Column(db.String(255))