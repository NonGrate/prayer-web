import json

import webapp2

from database import ndb_selection_database as database
from popos import JsonEncoder


class ByUser(webapp2.RequestHandler):
    def get(self, user_id):
        needs = database.get_by_user(int(user_id))

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(needs, cls=JsonEncoder))


class ByNeed(webapp2.RequestHandler):
    def get(self, need_id):
        needs = database.get_by_need(int(need_id))

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(needs, cls=JsonEncoder))


class Add(webapp2.RequestHandler):
    def post(self):
        body = json.loads(self.request.body)
        new_id = database.add_selection(user_id=int(body.get('user_id')), need_id=int(body.get('need_id')))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write({"id": new_id})


class Remove(webapp2.RequestHandler):
    def post(self):
        body = json.loads(self.request.body)
        success = database.remove_selection(user_id=int(body.get('user_id')), need_id=int(body.get('need_id')))

        self.response.headers['Content-Type'] = 'text/plain'
        self.abort(304)
        # self.response.write(success)


class Clear(webapp2.RequestHandler):
    def post(self):
        success = database.clear()
        self.response.headers['Content-type'] = 'text/plain'
        self.abort(304)
        # self.response.write(success)