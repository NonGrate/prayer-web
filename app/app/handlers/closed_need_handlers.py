from flask import jsonify

from database import flask_closed_need_database as database


def all():
    needs = database.get_all()
    return jsonify(needs)


def byId(need_id):
    needs = database.get_by_id(int(need_id))
    return jsonify(needs)


def revert(need_id):
    new_need_id = database.revert_need(int(need_id))
    return jsonify({"id": new_need_id})


def remove(need_id):
    success = database.remove_need(int(need_id))
    return success, 304


def clear():
    success = database.clear()
    return success, 304
