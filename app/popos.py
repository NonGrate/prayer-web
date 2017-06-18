from flask import json
from flask import jsonify


class Need():
    id = 0
    content = ""
    rating = 0
    color = 0
    date = 0

    def __str__(self):
        return "id: {}; content: {}; rating: {}; color: {}; date: {}".format(self.id,
                                                                             self.content.encode('utf-8'), self.rating,
                                                                             self.color, self.date)
class ClosedNeed(Need):
    pass


class User():
    id = 0
    name = ""
    date = 0

    def __str__(self):
        return "id: {}; name: {}".format(self.id, self.name)


class Selection():
    id = 0
    need_id = 0
    user_id = 0
    date = 0

    def __str__(self):
        return "id: {}; need_id: {}; user_id: {}".format(self.id, self.need_id, self.user_id)


def encode_need(obj):
    return {
        "id": obj.id,
        "content": obj.content,
        "rating": obj.rating,
        "color": obj.color,
        "timestamp": int(obj.date.strftime('%s'))
    }


def encode_user(obj):
    return {
        "id": obj.id,
        "name": obj.name,
        "timestamp": int(obj.date.strftime('%s'))
    }


def encode_selection(obj):
    return {
        "id": obj.id,
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
            return json.dumps(obj)
