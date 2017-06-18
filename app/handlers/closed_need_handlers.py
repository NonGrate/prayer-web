from flask import jsonify

from app.database import flask_closed_need_database as database


def closed_all():
    needs = database.get_all()
    return jsonify(needs)


def closed_by_id(need_id):
    needs = database.get_by_id(int(need_id))
    return jsonify(needs)


def closed_revert(need_id):
    new_need_id = database.revert_need(int(need_id))
    return jsonify({"id": new_need_id})


def closed_remove(need_id):
    success = database.remove_need(int(need_id))
    return success, 304


def closed_clear():
    success = database.clear()
    return success, 304
