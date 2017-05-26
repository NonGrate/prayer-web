from google.appengine.ext import ndb
import json


class Need(ndb.Model):
    content = ndb.StringProperty(indexed=False)
    rating = ndb.IntegerProperty()
    color = ndb.IntegerProperty()
    date = ndb.DateTimeProperty(auto_now=True)

    def __str__(self):
        return "id: {}; content: {}; rating: {}; color: {}; date: {}".format(self.key.id(), self.content, self.rating,
                                                                             self.color, self.date)

    def json(self):
        return json.dumps(self, cls=JsonEncoder)


class ClosedNeed(Need):
    pass


class User(ndb.Model):
    name = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now=True)

    def __str__(self):
        return "id: {}; name: {}".format(self.key.id(), self.name)

    def json(self):
        return json.dumps(self, cls=JsonEncoder)


class Selection(ndb.Model):
    need_id = ndb.IntegerProperty()
    user_id = ndb.IntegerProperty()
    date = ndb.DateTimeProperty(auto_now=True)

    def __str__(self):
        return "id: {}; need_id: {}; user_id: {}".format(self.key.id(), self.need_id, self.user_id)

    def json(self):
        return json.dumps(self, cls=JsonEncoder)


def encode_need(obj):
    return {
        "id": obj.key.id(),
        "content": obj.content,
        "rating": obj.rating,
        "color": obj.color,
        "timestamp": int(obj.date.strftime('%s'))
    }


def encode_user(obj):
    return {
        "id": obj.key.id(),
        "name": obj.name,
        "timestamp": int(obj.date.strftime('%s'))
    }


def encode_selection(obj):
    return {
        "id": obj.key.id(),
        "need_id": obj.need_id,
        "user_id": obj.user_id,
        "timestamp": int(obj.date.strftime('%s'))
    }


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Need):
            return encode_need(obj)
        elif isinstance(obj, ClosedNeed):
            return encode_need(obj)
        elif isinstance(obj, User):
            return encode_user(obj)
        elif isinstance(obj, Selection):
            return encode_selection(obj)
        else:
            return json.JSONEncoder.default(self, obj)
