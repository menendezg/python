import csv

from flask_script import Command
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import BaseConfig
from resources.states.models import State


def get_states():
    with open("states.csv") as f:
        csv_r = csv.DictReader(f)
        for row in csv_r:
            yield row


class bulk(Command):
    def run(self):
        """
        Insert list of states given
        """
        states = [
            State(
                code=state["codigo;nombre"].split(";")[0],
                name=state["codigo;nombre"].split(";")[1],
            )
            for state in get_states()
        ]

        session = sessionmaker(create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI))
        s = session()
        s.bulk_save_objects(states)
        s.commit()
