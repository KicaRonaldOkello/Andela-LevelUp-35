from myapp import app
from model import User, GuestList
from flask import request, json, jsonify, make_response

user = User()
guests = GuestList()
@app.route("/api/add-user", methods = ["POST"])
def add_user():
    """Adds user to list."""
    data = {
        "name": request.json["name"],
        "email": request.json["email"]
    }
    duplicate = [dup for dup in user.USERS if data["name"] == dup["name"]]
    if data["name"] == "":
        return make_response(jsonify({"Error": "Name cannot be empty"}), 400)
    if data["email"] == "":
        return make_response(jsonify({"Error": "Email cannot be empty"}), 400)
    if not duplicate:
        user.adding_user(data)
        return make_response(jsonify({"User": data}), 201)
    else:
        return make_response(jsonify({"Error": "Duplicate data"}), 409)


@app.route("/api/get-users", methods = ["GET"])
def get_users():
    user_info = user.getting_user()
    return make_response(jsonify({"User info": user_info}), 200)


@app.route("/api/delete-user", methods = ["DELETE"])
def delete_users():
    deleted = user.deleting_user()
    return make_response(jsonify({"Deleted": deleted}), 200)


@app.route("/api/guest/add", methods = ["POST"])
def add_guests():
    """Adds users to guest list if name exists in user."""
    guest_detail = {
        request.json["name"]
    }
    guest_exist = [guest for guest in user.USERS if guest["name"] == guest_detail["name"]]
    if guest_detail != "":
        return make_response(jsonify({"Error": "Please etner a valid guest name"}), 400)
    if guest_exist:
        guests.adding_guest(guest_detail)
        return make_response(jsonify({"Guest name": guest_detail}), 201)
    else:
        return make_response(jsonify({"Error": "Guest name not available, please register as user first"}), 400)



@app.route("/api/guest/get", methods = ["GET"])
def get_guest_list():
    guest_info = guests.getting_guests()
    return make_response(jsonify({"Guests"}: guest_info), 200)


@app.route("/api/guest/delete/<guest_no>", methods = ["DELETE"])
def delete_guest(guest_no):
    guest_deleted = guests.deleting_guest(guest_no)
    return make_response(jsonify({"Deleted guest"}: guest_deleted), 200)