from datetime import datetime

from db import db


class State(db.Model):
    """Class User ORM representation."""

    __tablename__ = "States"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer)
    name = db.Column(db.String)
    user = db.relationship("User", uselist=False, backref="state")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def json(self):
        """return json self representation object."""
        return {
            "code": self.code,
            "name": self.name,
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
