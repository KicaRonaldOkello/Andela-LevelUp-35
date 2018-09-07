from myapp import app
from models import User, GuestList
from flask import request, json, jsonify, make_response

guest = GuestList()
@app.route("/api/add-user", methods = ["POST"])
def add_guest():
    data = {
        "name": request.json["name"],
        "email": request.json["email"]
    }
    duplicate = [dup for dup in guest.USERS if data["name"] == dup["name"]]
    if data["name"] == "":
        return make_response(jsonify({"Error": "Name cannot be empty"}), 400)
    if data["email"] == "":
        return make_response(jsonify({"Error": "Email cannot be empty"}), 400)
    if not duplicate:
        guest.adding_user(data)
        return make_response(jsonify({"User": data}), 201)
    else:
        return make_response(jsonify({"Error": "Duplicate data"}), 409)


@app.route("/api/get-users", methods = ["GET"])
def get_guests():
    user_info = guest.getting_user()
    return make_response(jsonify({"User info": user_info}), 200)


@app.route("/api/delete-user", methods = ["DELETE"])
def delete_guests():
    deleted = guest.deleting_user()
    return make_response(jsonify({"Deleted": deleted}), 200)