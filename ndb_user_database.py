from popos import User


def get_all():
    query = User.query().order(-User.date).fetch()
    return query


def get_by_id(need_id):
    return User.get_by_id(need_id)


def add_user(name):
    user = User(name=name)
    key = user.put()

    return key.id()


def clear():
    return False
