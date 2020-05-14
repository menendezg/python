from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from resources.states.state_controller import StateResource
from resources.user.user_controller import UserResource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
api = Api(app)

api.add_resource(UserResource, "/user")  # CRUD operations about user register
# api.add_resource(StateResource, "/state/<string:userid>")  # get info about user
api.add_resource(StateResource, "/state")  # get info about user

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(debug=True)
