from popos import Need
from popos import ClosedNeed


def get_all():
    return {"name": "need/all"}


def get_by_id(need_id):
    return {"name": "need/by_id"}


def add_need(content, color):
    return {"name": "need/add_need"}


def like_need(need_id):
    return {"name": "need/like"}


def close_need(need_id):
    return {"name": "need/close"}


def remove_need(need_id):
    return {"name": "need/remove"}


def clear():
    return {"name": "need/clear"}
