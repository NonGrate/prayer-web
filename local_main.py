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

import json
import database


def all():
    needs = database.get_all()

    print (json.dumps([ob.__dict__ for ob in needs]))


def add(content, color):
    new_id = database.add_need(content, color)

    print (new_id)


def like_need(need_id):
    new_rating = database.like_need(need_id)

    print (new_rating)


def clear():
    database.clear()
