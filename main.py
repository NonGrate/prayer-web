# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import json
import database
from popos import Need


class AllPage(webapp2.RequestHandler):
    def get(self):
        needs = database.get_all()

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps([ob.__dict__ for ob in needs]))


class HelpPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Help, I\'m inside this green robot!')


class AddPage(webapp2.RequestHandler):
    def post(self):
        need = Need(self.request.body)
        new_id = database.add_need(need.content, need.color)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(new_id)


class LikePage(webapp2.RequestHandler):
    def post(self):
        path_url = self.request.path_url
        need_id = path_url.split("/")[-1]
        new_rating = database.like_need(need_id)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(new_rating)


class ClearPage(webapp2.RequestHandler):
    def post(self):
        database.clear()
        self.response.headers['Content-type'] = 'text/plain'
        self.response.write(self.request)


app = webapp2.WSGIApplication([
    ('/all', AllPage),
    ('/help', HelpPage),
    ('/add', AddPage),
    ('/like/.*', LikePage),
    ('/clear', ClearPage)
], debug=True)
