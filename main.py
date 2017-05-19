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

class Need:
    id = 0
    content = ""
    rating = 0
    color = 0


needs_list = []


class AllPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write('[{"id": 123, "content": "content", "rating": 2, "color": 16711935}]')


class HelpPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Help, I\'m inside this green robot!')


class AddPage(webapp2.RequestHandler):
    def post(self):
        need = Need()
        need.rating = 0
        need.id = len(needs_list)
        need.content = ""
        need.color = ""

        # needs_list.append(need)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)


class LikePage(webapp2.RequestHandler):
    def post(self):
        need_id = self.response.get('id')
        self.like_need(need_id)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Help, I\'m inside this green robot!')

    @staticmethod
    def like_need(need_id):
        for index, need in needs_list:
            if need.id == need_id:
                need.rating += 1
                needs_list[index] = need
                break


class ClearPage(webapp2.RequestHandler):
    def post(self):
        global needs_list
        needs_list = []
        self.response.headers['Content-type'] = 'text/plain'
        self.response.write(self.request)


app = webapp2.WSGIApplication([
    ('/all', AllPage),
    ('/help', HelpPage),
    ('/add', AddPage),
    ('/like', LikePage)
    ('/clear', ClearPage)
], debug=True)
