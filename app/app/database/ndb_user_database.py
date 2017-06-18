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


def remove_user(user_id):
    user = get_by_id(user_id)
    user.key().delete()

    return True


def clear():
    return False
