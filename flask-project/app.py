from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig
from resources.states.state_controller import StateResource, StateList
from resources.user.user_controller import UserResource, UserList

app = Flask(__name__)
app.config.from_object(BaseConfig)
api = Api(app)

api.add_resource(UserList, "/users")
api.add_resource(UserResource, "/users/<string:user_id>")
api.add_resource(StateList, "/states")
api.add_resource(StateResource, "/states/<string:state_id>")


if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(host="0.0.0.0")
