# BLOG
#### Video Demo:  https://www.youtube.com/watch?v=n5n2iJ4RUh8
## CS50
>This was my final project for conclude the CS50 Introduction to Computer Sciense course.

>CS, C, Python, SQL, HTML, CSS, Javascript, Flask , Web Development, CS50
## Features

- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/l)
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
- [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

I used the Flask micro web framework which is written in Python.It was necessary to also use flask-sqlalchemy to manage the SQL database with sqlite alongside flask-wtf which is used for creating posts.

## Explaining the project and the database
My final project is a website that allows users to register while also implementing CRUD functionality as the users can create, edit, and delete posts.

All information about users, cases and selected cases for each people are stored in the website's database. 

I used the sqlalchemy extension to connect the database to the flask application and sqlite3 to manage it.

Flask-WTF made it really easy to validate users' email adresses. 

Once a user has successfully registered, they will have a default profile picture which they can update if they wish to do so. With the help of Pillow, I also implemented a function which compresses and resizes the new profile picture in case it is of really good quality.

There's also pagination both on the homepage as well as each individual users' posts.

In the cases a user forgot their password, they will be able to request to change it. Once they will enter their email and press the Request Password Reset button, they will be sent a link with a temporary secret token that they will be able to access for 30 minutes. This is done with the help of Flask-Mail and the sandbox environment provited by mailtrap where I set up a sandbox SMTP account.

Additionally, there are several custom error pages that were created with HTML, CSS, Javascript, Bootstrap as well as additional libraries such as JQuery and dynamics.js

Furthermore, I am using python-dotenv so I can use environment variables in a separate file, .env, instead of having sensitive data directly in config.py, which is added in the .gitignore file, so that way values such as the secret key, email, password and more can be safe and publically viewable by everyone if the codebase will be shared with multiple people.

## About CS50
CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL as well as HTML, CSS, and JavaScript (for web development).

Thanks CS50.

- Where I take the CS50 course?
https://cs50.harvard.edu/x/2023/

[LinkedIn Damian Galben](https://www.linkedin.com/in/damian-g-037380a6/)