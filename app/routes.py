from app import app
from flask import render_template, redirect, url_for


# These are wrappers.
# Routes is the default way to create a URL.
@app.route('/')
@app.route('/index')
def index():
    user = {"username" : "Ethan",
            "password": "pWord"}
    num = 2 + 2
    # Flask will look into the templates folder.
    # user2=user: send in a variable name user, and
    # set it to be user.
    return render_template('index.html', user2 = user, num = num, title = "Awesome")

# This creates a route for posts.html that
# renders the file.
@app.route('/posts')
def posts():
    posts = [
    "This is post #1 ",
    "This is post #2 ",
    "This is post #3 ",
    "We\'re looping through these posts ",
    "This is Flask "
    ]
    return render_template('posts.html', title = "Posts", posts = posts)

@app.route('/redirect')
def getaway():
    return redirect(url_for('index'))
