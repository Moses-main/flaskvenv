from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

posts = [
    {
        'author':"Sunday Moses",
        'title':"Blog Post 1",
        'content': "First Post Content",
        'date_posted':"April 20, 2018"
    },

    {
        'author':"Chizaram Tirzah",
        'title':"Blog Post 2",
        'content': "Second Post Content",
        'date_posted':"April 21, 2018"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


if __name__ == "__main__":
    app.run(debug=True)