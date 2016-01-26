from flask_sqlalchemy import SQLAlchemy 
# from sqlalchemy.dialects import postgresql


db = SQLAlchemy()


class Actor(db.Model):
    """ Profile information """

    __tablename__ = "actors"

    name = db.Column(db.Text, primary_key=True)
    last_name = db.Column(db.Text, nullable=True)
    first_name = db.Column(db.Text, nullable=True)
    person_id = db.Column(db.Text, nullable=True)
    star_meter = db.Column(db.Integer, nullable=True)
    manager = db.Column(db.Text, nullable=True)
    publicist = db.Column(db.Text, nullable=True)
    legal_representative = db.Column(db.Text, nullable=True)
    talent_agent = db.Column(db.Text, nullable=True)


def connect_to_db(app):
    """ Connect the database to my Flask app """

    # Configure to use database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///imdb.db'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()
