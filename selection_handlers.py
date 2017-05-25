import webapp2
import ndb_selection_database as database
from popos import JsonEncoder
import json


class ByUser(webapp2.RequestHandler):
    def get(self):
        path_url = self.request.path_url
        user_id = path_url.split("/")[-1]
        needs = database.get_by_user(int(user_id))

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(needs, cls=JsonEncoder))


class ByNeed(webapp2.RequestHandler):
    def get(self):
        path_url = self.request.path_url
        need_id = path_url.split("/")[-1]
        needs = database.get_by_need(int(need_id))

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(needs, cls=JsonEncoder))


class Add(webapp2.RequestHandler):
    def post(self):
        body = json.loads(self.request.body)
        new_id = database.add_selection(user_id=int(body.get('user_id')), need_id=int(body.get('need_id')))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(new_id)


class Remove(webapp2.RequestHandler):
    def post(self):
        body = json.loads(self.request.body)
        success = database.remove_selection(user_id=int(body.get('user_id')), need_id=int(body.get('need_id')))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(success)


class Clear(webapp2.RequestHandler):
    def post(self):
        success = database.clear()
        self.response.headers['Content-type'] = 'text/plain'
        self.response.write(success)
