from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Damian Galben',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 12, 2023'
    },
    {
        'author': 'Steve Platon',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 13, 2023'
    }
]

# Configure application
app = Flask(__name__)

# Use a secret token
app.config['SECRET_KEY'] = '6400945f04791b91638e31e1eb31491a'

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please Check you username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)
