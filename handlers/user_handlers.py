import json

import webapp2

from database import ndb_user_database as database
from popos import JsonEncoder


class All(webapp2.RequestHandler):
    def get(self):
        users = database.get_all()

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(users, cls=JsonEncoder))


class ById(webapp2.RequestHandler):
    def get(self, user_id):
        users = database.get_by_id(int(user_id))

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(users, cls=JsonEncoder))


class Add(webapp2.RequestHandler):
    def post(self):
        body = json.loads(self.request.body)
        new_id = database.add_user(name=body.get('name'))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(new_id)


class Remove(webapp2.RequestHandler):
    def get(self, user_id):
        success = database.remove_user(int(user_id))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(success)


class Clear(webapp2.RequestHandler):
    def post(self):
        success = database.clear()
        self.response.headers['Content-type'] = 'text/plain'
        self.response.write(success)
