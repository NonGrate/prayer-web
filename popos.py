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
        return json.dumps(self, cls=NeedEncoder)


class NeedEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Need):
            return {
                "id": obj.key.id(),
                "content": obj.content,
                "rating": obj.rating,
                "color": obj.color,
                "timestamp": obj.date.strftime('%s')
            }
        else:
            return json.JSONEncoder.default(self, obj)