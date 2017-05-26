from popos import Need
from popos import ClosedNeed


def get_all():
    query = Need.query().order(-Need.date).fetch()
    return query


def get_by_id(need_id):
    return Need.get_by_id(need_id)


def add_need(content, color):
    need = Need(content=content, color=color, rating=0)
    key = need.put()

    return key.id()


def like_need(need_id):
    need = get_by_id(need_id)
    need.rating += 1
    need.put()

    return get_by_id(need_id).rating


def close_need(need_id):
    need = get_by_id(need_id)
    closed_need = ClosedNeed(need)
    closed_need.put()
    need.key().delete()


def remove_need(need_id):
    need = get_by_id(need_id)
    need.key().delete()

    return True


def clear():
    return False
