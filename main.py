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

import logging
import webapp2
from handlers import selection_handlers
from handlers import need_handlers
from handlers import user_handlers


class HelpPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Help, I\'m inside this green robot!')


def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A server error occurred!')
    response.set_status(500)


app = webapp2.WSGIApplication([
    ('/help', HelpPage),
    # needs
    ('/need/all', need_handlers.All),
    ('/need/(\d+)', need_handlers.ById),
    ('/need/add', need_handlers.Add),
    ('/need/like/(\d+)', need_handlers.Like),
    ('/need/close/(\d+)', need_handlers.Close),
    ('/need/remove/(\d+)', need_handlers.Remove),
    ('/need/clear', need_handlers.Clear),
    # users
    ('/user/all', user_handlers.All),
    ('/user/(\d+)', user_handlers.ById),
    ('/user/add', user_handlers.Add),
    ('/user/remove/(\d+)', user_handlers.ById),
    ('/user/clear', user_handlers.Clear),
    # selections
    ('/selection/by_user/(\d+)', selection_handlers.ByUser),
    ('/selection/by_need/(\d+)', selection_handlers.ByNeed),
    ('/selection/add', selection_handlers.Add),
    ('/selection/remove', selection_handlers.Remove),
    ('/selection/clear', selection_handlers.Clear),
], debug=True)

app.error_handlers[500] = handle_500
