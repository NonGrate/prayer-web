from app.popos import User


def get_all():
    return {"name": "user/all"}


def get_by_id(need_id):
    return {"name": "user/by_id"}


def add_user(name):
    return {"name": "user/add"}


def remove_user(user_id):
    return {"name": "user/remove"}


def clear():
    return {"name": "user/clear"}
