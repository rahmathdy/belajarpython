from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.user import *
from utils import hash_password


class UserListResource(Resource):
    def post(self):
        json_data = request.get_json()
        username = json_data.get("username")
        email = json_data.get("email")
        non_hash_password = json_data.get("password")
        if User.get_by_username(username):
            return {"message": "Username already exist"}, HTTPStatus.BAD_REQUEST
        if User.get_by_email(email):
            return {"message": "Email already exist"}, HTTPStatus.BAD_REQUEST

        password = hash_password(non_hash_password)
        user = User(username=username, email=email, password=password)
        user.save()  # insert into

        data = {"id": user.id, "username": user.username, "email": user.email}
        return data, HTTPStatus.CREATED
