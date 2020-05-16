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


# postgresql://{0}:{1}@{2}:{3}/{4}
# DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
# DEBUG=False
# SECRET_KEY=5(15ds+i2+%ik6z&!yer+ga9m=e%jcqiz_5wszg)r-z!2--b2d
# DB_NAME=postgres
# DB_USER=postgres
# DB_PASS=postgres
# DB_SERVICE=postgres
# DB_PORT=5432
