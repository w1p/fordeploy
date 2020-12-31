import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    p = reqparse.RequestParser()
    p.add_argument("username", type=str, required=True, help="Can not be blank")
    p.add_argument("password", type=str, required=True, help="Can not be blank")

    def post(self):
        d = UserRegister.p.parse_args()
        if UserModel.findByUsername(d["username"]):
            return {"message": "Username '" + d["username"] + "' already existed"}, 400
        print(d)
        user = UserModel(**d)
        user.saveToDb()
        return {"message": "User created successfully."}, 201
