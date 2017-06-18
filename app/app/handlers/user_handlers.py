from flask import jsonify

from database import flask_user_database as database


def all():
    users = database.get_all()
    return jsonify(users)


def by_id(user_id):
    users = database.get_by_id(int(user_id))
    return jsonify(users)


def add(user):
    new_id = database.add_user(name=user.name)
    return jsonify({"id": new_id})


def remove(user_id):
    success = database.remove_user(int(user_id))
    return success, 304


def clear():
    success = database.clear()
    return success, 304