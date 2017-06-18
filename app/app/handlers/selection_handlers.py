from flask import jsonify

from database import flask_selection_database as database


def by_user(user_id):
    needs = database.get_by_user(int(user_id))
    return jsonify(needs)


def by_need(need_id):
    needs = database.get_by_need(int(need_id))
    return jsonify(needs)


def add(selection):
    new_id = database.add_selection(user_id=selection.user_id, need_id=selection.need_id)
    return jsonify({"id": new_id})


def remove(selection):
    success = database.remove_selection(user_id=selection.user_id, need_id=selection.need_id)
    return success, 304


def clear():
    success = database.clear()
    return success, 304
