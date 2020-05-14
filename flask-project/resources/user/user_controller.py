import json

from flask_restful import Resource, reqparse

from .models import User


class UserResource(Resource):
    def get(self):
        # user = User.find_by_id(userid)
        # if user is not None:
        # ret = user.json()
        # else:
        # ret = {"message": "That user dont exist"}, 404
        return {"message": "runnin"}
