from app.popos import Selection


def get_by_user(user_id):
    return {"name": "selection/by_user"}


def get_by_need(need_id):
    return {"name": "selection/by_need"}


def get_by_id(selection_id):
    return {"name": "selection/by_id"}


def add_selection(user_id, need_id):
    return {"name": "selection/add"}


def remove_selection(user_id, need_id):
    return {"name": "selection/remove"}


def clear():
    return {"name": "selection/clear"}
