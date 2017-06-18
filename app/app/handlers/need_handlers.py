from flask import jsonify

from database import flask_need_database as database


def all():
    needs = database.get_all()
    return jsonify(needs)


def by_id(need_id):
    needs = database.get_by_id(int(need_id))
    return jsonify(needs)


def add(need):
    print(self.request.body)
    body = json.loads(self.request.body)
    new_id = database.add_need(content=body.get('content'), color=int(body.get('color')))

    return jsonify({"id": new_id})


def like(need_id):
    need = database.like_need(int(need_id))
    return jsonify(need)


def close(need_id):
    new_need_id = database.close_need(int(need_id))
    return jsonify({"id": new_need_id})


def remove(need_id):
    success = database.remove_need(int(need_id))
    return success, 304


def clear():
    success = database.clear()
    return success, 304
