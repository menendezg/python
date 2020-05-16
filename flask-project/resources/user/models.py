from datetime import datetime
from resources.states.models import State
from db import db
from sqlalchemy.orm.exc import NoResultFound


class User(db.Model):
    """Class User ORM representation."""

    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    state = db.Column(db.Integer, db.ForeignKey("States.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    def __init__(self, name, age, state):
        self.name = name
        self.age = age
        self.state = state

    def update(self, name, age, state):
        self.name = name
        self.age = age
        self.state = state

    def json(self):
        """return json self representation object."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "state": self.state,
            "created_at": str(self.created_at),
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_username(cls, name):

        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        users = [
            {"name": name, "age": age, "state": state}
            for name, age, state in db.session.query(cls.name, cls.age, State.name)
            .join(State)
            .filter(User.state == State.id)
            .all()
        ]
        return users

    @classmethod
    def delete_by_id(cls, _id):
        cls.query.filter_by(id=_id).delete()
        db.session.commit()
