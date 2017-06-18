from flask import jsonify

from app.database import flask_selection_database as database


def selection_by_user(user_id):
    needs = database.get_by_user(int(user_id))
    return jsonify(needs)


def selection_by_need(need_id):
    needs = database.get_by_need(int(need_id))
    return jsonify(needs)


def selection_add(selection):
    new_id = database.add_selection(user_id=selection.user_id, need_id=selection.need_id)
    return jsonify({"id": new_id})


def selection_remove(selection):
    success = database.remove_selection(user_id=selection.user_id, need_id=selection.need_id)
    return success, 304


def selection_clear():
    success = database.clear()
    return success, 304
