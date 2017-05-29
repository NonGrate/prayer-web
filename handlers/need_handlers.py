import json

import webapp2

from database import ndb_need_database as database
from popos import JsonEncoder


class All(webapp2.RequestHandler):
    def get(self):
        needs = database.get_all()

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(needs, cls=JsonEncoder))


class ById(webapp2.RequestHandler):
    def get(self, need_id):
        needs = database.get_by_id(int(need_id))

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(needs, cls=JsonEncoder))


class Add(webapp2.RequestHandler):
    def post(self):
        print(self.request.body)
        body = json.loads(self.request.body)
        new_id = database.add_need(content=body.get('content'), color=int(body.get('color')))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write({"id": int(new_id)})


class Like(webapp2.RequestHandler):
    def get(self, need_id):
        need = database.like_need(int(need_id))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(need, cls=JsonEncoder))


class Close(webapp2.RequestHandler):
    def get(self, need_id):
        new_need_id = database.close_need(int(need_id))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write({"id": int(new_need_id)})


class Remove(webapp2.RequestHandler):
    def get(self, need_id):
        success = database.remove_need(int(need_id))

        self.response.headers['Content-Type'] = 'text/plain'
        self.abort(304)
        # self.response.write(success)


class Clear(webapp2.RequestHandler):
    def post(self):
        success = database.clear()
        self.response.headers['Content-type'] = 'text/plain'
        self.abort(304)
        # self.response.write(success)
