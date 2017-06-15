from popos import Need
from popos import ClosedNeed


def get_all():
    query = ClosedNeed.query().order(-ClosedNeed.date).fetch()
    return query


def get_by_id(need_id):
    return ClosedNeed.get_by_id(need_id)


def revert_need(need_id):
    closed_need = get_by_id(need_id)
    need = Need(closed_need)
    key = need.put()
    closed_need.key().delete()

    return key.id()


def remove_need(need_id):
    closed_need = get_by_id(need_id)
    closed_need.key().delete()

    return True


def clear():
    return False
