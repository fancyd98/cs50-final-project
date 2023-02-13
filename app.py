from flask import Flask, render_template, url_for

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

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')