from flask_restful import Resource, reqparse
from flask import abort
from .models import State


class StateParser:
    parser = reqparse.RequestParser()
    parser.add_argument("code", type=int, required=True)
    parser.add_argument("name", type=str, required=True)


class StateList(Resource, StateParser):
    def get(self):
        """
        Return all state in the table States.
        """
        query_states = State.get_all()
        states = [{"code": state.code, "name": state.name} for state in query_states]
        return states

    def post(self):
        parameters = StateResource.parser.parse_args()
        state = State(**parameters)
        state.save_to_db()
        return state.json(), 201


class StateResource(Resource, StateParser):
    def get(self, state_id):
        """
        Return state by id
        """
        state = State.find_by_id(state_id)
        if state:
            return state.json()
        else:
            return {"Error": f"The record with id {state_id} was not found"}, 400

    def delete(self, state_id):
        if not state_id:
            abort("please send an id")
        else:
            State.delete_by_id(state_id)
            return {"message": f"the record with id {state_id} was deleted"}

    def put(self, state_id):
        parameters = StateResource.parser.parse_args()
        state = State.find_by_id(state_id)
        if state:
            state.update(**parameters)
            state.save_to_db()
            return state.json(), 201
        else:
            return {"Error": f"The record with id {state_id} was not found"}, 400
