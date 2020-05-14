from flask_restful import Resource

from .models import State


class StateResource(Resource):
    def get(self):
        # user = State.find_by_id(state_id)
        # if user is not None:
        # ret = user.json()
        # else:
        # ret = {"message": "That user dont exist"}, 404
        return {"message": "running state"}
