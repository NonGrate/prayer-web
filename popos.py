import json


class Need:
    id = 0
    content = ""
    rating = 0
    color = 0

    def __init__(self, string):
        self.__dict__ = json.loads(string)

    def __str__(self):
        return "id: {}; content: {}; rating: {}; color: {}".format(self.id, self.content, self.rating, self.color)