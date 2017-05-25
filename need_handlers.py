import webapp2
import ndb_need_database as database
from popos import JsonEncoder
import json


class All(webapp2.RequestHandler):
    def get(self):
        needs = database.get_all()

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(needs, cls=JsonEncoder))


class ById(webapp2.RequestHandler):
    def get(self):
        path_url = self.request.path_url
        need_id = path_url.split("/")[-1]
        needs = database.get_by_id(int(need_id))

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(needs, cls=JsonEncoder))


class Add(webapp2.RequestHandler):
    def post(self):
        body = json.loads(self.request.body)
        new_id = database.add_need(content=body.get('content'), color=int(body.get('color')))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(new_id)


class Like(webapp2.RequestHandler):
    def post(self):
        path_url = self.request.path_url
        need_id = path_url.split("/")[-1]
        new_rating = database.like_need(int(need_id))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(new_rating)


class Clear(webapp2.RequestHandler):
    def post(self):
        success = database.clear()
        self.response.headers['Content-type'] = 'text/plain'
        self.response.write(success)
