from google.appengine.ext import ndb


class Need(ndb.Model):
    id = ndb.IntegerProperty(indexed=True)
    content = ndb.StringProperty(indexed=False)
    rating = ndb.IntegerProperty
    color = ndb.IntegerProperty
    date = ndb.DateTimeProperty(auto_now_add=True)

    def __str__(self):
        return "id: {}; content: {}; rating: {}; color: {}; date: {}".format(self.id, self.content, self.rating,
                                                                             self.color, self.date)
