from flask import abort
from flask_restful import Resource, reqparse

from .models import User


class UserParser:
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("age", type=int, required=True)
    parser.add_argument("state", type=int, required=True)


class UserList(Resource, UserParser):
    def get(self):
        users = User.get_all()
        return {"message": users}

    def post(self):
        parameters = UserList.parser.parse_args()
        user = User(**parameters)
        user.save_to_db()
        return user.json(), 201


class UserResource(Resource, UserParser):
    def get(self, user_id):
        """
        Return state by id
        """
        user = User.find_by_id(user_id)
        if user:
            return user.json()
        else:
            return {"Error": f"The record with id {user_id} was not found"}, 400

    def delete(self, user_id):
        if not user_id:
            abort("please send an id")
        else:
            User.delete_by_id(user_id)
            return {"message": f"the record with id {user_id} was deleted"}

    def put(self, user_id):
        parameters = UserResource.parser.parse_args()
        user = User.find_by_id(user_id)
        if user:
            user.update(**parameters)
            user.save_to_db()
            return user.json(), 201
        else:
            return {"Error": f"The record with id {user_id} was not found"}, 400
