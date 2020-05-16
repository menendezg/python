from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from bulk_insert import bulk
from db import db

migrate = Migrate(app, db)
manager = Manager(app)

db.init_app(app)
manager.add_command("db", MigrateCommand)
manager.add_command("bulk", bulk())

if __name__ == "__main__":
    manager.run()
