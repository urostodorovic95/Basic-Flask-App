from website import create_app, db
from website.models import User, Post

app = create_app()

with app.app_context():
    # db.create_all()
    # user_1 = User(
    #     username="Test",
    #     email="test1@email.com"
    # )
    # user_2 = User(
    #     username="Test1",
    #     email="test2@email.com"
    # )
    # db.session.add(user_1)
    # db.session.add(user_2)
    
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)

    