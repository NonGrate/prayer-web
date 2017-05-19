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
from webapp2_extras import json


class AllPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        # response = {
        #     'id': 123,
        #     'content': "content",
        #     'rating': 2,
        #     'color': 16711935
        # }
        self.response.out.write('[{"id": 123, "content": "content", "rating": 2, "color": 16711935}]')


class HelpPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Help, I\'m inside this green robot!')


app = webapp2.WSGIApplication([
    ('/all', AllPage),
    ('/help', HelpPage),
    # ('/add', AddPage),
    # ('/like', LikePage)
], debug=True)
