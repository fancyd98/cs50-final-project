from app import app, db, User, Post

with app.app_context():
    db.create_all()

user_1 = User(username='Neo', email='neo@demo.com', password='password')
user_2 = User(username='Alex', email='alex@demo.com', password='password')

with app.app_context():
    db.session.add(user_1)
    db.session.add(user_2)
    db.session.commit()