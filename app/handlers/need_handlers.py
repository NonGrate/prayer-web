from flask import jsonify

from app.database import flask_need_database as database


def need_all():
    needs = database.get_all()
    return jsonify(needs)


def need_by_id(need_id):
    needs = database.get_by_id(int(need_id))
    return jsonify(needs)


def need_add():
    new_id = database.add_need("abv", 123)
    return jsonify({"id": new_id})


def need_like(need_id):
    need = database.like_need(int(need_id))
    return jsonify(need)


def need_close(need_id):
    new_need_id = database.close_need(int(need_id))
    return jsonify({"id": new_need_id})


def need_remove(need_id):
    success = database.remove_need(int(need_id))
    return success, 304


def need_clear():
    success = database.clear()
    return jsonify(success), 304
