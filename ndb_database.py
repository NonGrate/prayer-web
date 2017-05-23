from popos import Need


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


def clear():
    return
