from flask import Flask
from flask import render_template
from flask import url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1b554ae7c3fdb140a4641088964de4d8'

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


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)



if __name__ == "__main__":
    app.run(debug=True)