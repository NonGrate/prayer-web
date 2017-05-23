# from popos import Need


def get_all():
    # query = Need.query().order(-Need.date).fetch()
    return []


def get_by_id(need_id):
    # query = Need.query(Need.id == need_id).get()
    #
    return 0, "content", 1, 123


def add_need(content, color):
    return 1


def like_need(need_id):
    return 1


def clear():
    return
