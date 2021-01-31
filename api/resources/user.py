from flask import Response, request
from flask_restful import Resource
from ..data import users
import json


class UsersApi(Resource):
    def get(self):
        print("Users", json.dumps(users))
        return Response(json.dumps(users), mimetype="application/json", status=200)


class UserAddApi(Resource):
    def post(self):
        new_user = request.json['user']
        users.append(new_user)
        return Response(new_user, mimetype="application/json", status=201)


class UserApi(Resource):
    def get(self, target_id):
        for user in users:
            if user.user_id == target_id:
                return Response(user, mimetype="application/json", status=200)
        return Response({}, mimetype="application/json",  status=404)

    def put(self, target_id):
        for user in users:
            if user.user_id == target_id:
                user = request.json['user']
                return Response(user, mimetype="application/json",  status=201)
        return Response({}, mimetype="application/json", status=404)

    def delete(self, target_id):
        for user in users:
            if user.user_id == target_id:
                users.remove(user)
                return Response(user, mimetype="application/json", status=200)
        return Response({}, mimetype="application/json", status=404)
