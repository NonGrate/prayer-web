import json

import webapp2

from database import ndb_closed_need_database as database
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


class Revert(webapp2.RequestHandler):
    def get(self, need_id):
        new_need_id = database.revert_need(int(need_id))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write({"id": new_need_id})


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
