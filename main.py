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
import logging
import json
import ndb_database as database


class AllPage(webapp2.RequestHandler):
    def get(self):
        needs = database.get_all()

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(map(lambda need: need.json(), needs))


class HelpPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Help, I\'m inside this green robot!')


class AddPage(webapp2.RequestHandler):
    def post(self):
        post = self.request.POST
        new_id = database.add_need(content=post.get('content'), color=int(post.get('color')))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(new_id)


class LikePage(webapp2.RequestHandler):
    def post(self):
        path_url = self.request.path_url
        need_id = path_url.split("/")[-1]
        new_rating = database.like_need(int(need_id))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(new_rating)


class ClearPage(webapp2.RequestHandler):
    def post(self):
        database.clear()
        self.response.headers['Content-type'] = 'text/plain'
        self.response.write(self.request)


def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A server error occurred!')
    response.set_status(500)


app = webapp2.WSGIApplication([
    ('/all', AllPage),
    ('/help', HelpPage),
    ('/add', AddPage),
    ('/like/.*', LikePage),
    ('/clear', ClearPage)
], debug=True)

app.error_handlers[500] = handle_500
