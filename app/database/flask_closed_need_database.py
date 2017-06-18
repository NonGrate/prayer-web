from app.popos import Need
from app.popos import ClosedNeed


def get_all():
    return {"name": "closed/all"}


def get_by_id(need_id):
    return {"name": "closed/by_id"}


def revert_need(need_id):
    return {"name": "closed/revert"}


def remove_need(need_id):
    return {"name": "closed/remove"}


def clear():
    return {"name": "closed/clear"}
