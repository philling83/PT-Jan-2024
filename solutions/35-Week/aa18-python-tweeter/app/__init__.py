from flask import Flask, redirect, render_template, session
import random
from datetime import date

from .config import Config
from .tweets import tweets
from .form.form import TweetForm
from .models import db, Tweet

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def home():
    tweet = random.choice(tweets)

    return render_template("index.html", tweet=tweet)

@app.route("/feed")
def feed():
    return render_template("feed.html", tweets=tweets)

@app.route("/new", methods=["GET", "POST"])
def new_tweet_form():
    form = TweetForm()

    if form.validate_on_submit():
        # new_tweet = {
        #     "id": len(tweets),
        #     "author": form.data["author"],
        #     "tweet": form.data["tweet"],
        #     "date": date.today(),
        #     "likes": 0
        # }

        # tweets.append(new_tweet)

        new_tweet = Tweet(tweet=form.data["tweet"])

        db.session.add(new_tweet)
        db.session.commit()

        return redirect("/feed", 302)
        
    if form.errors:
        return form.errors

    return render_template("new_tweet.html", form=form)

@app.route("/session")
def visits():
    if 'visits' in session:
        # reading and updating session data
        session['visits'] = session.get('visits') + 1
    else:
        # setting session data
        session['visits'] = 1
    return "Total visits: {}".format(session.get('visits'))