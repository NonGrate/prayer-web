from flask import Flask
from popos import JsonEncoder

app = Flask(__name__)
app.json_encoder = JsonEncoder

from handlers import user_handlers
from handlers import need_handlers
from handlers import selection_handlers
from handlers import closed_need_handlers

@app.route('/')
def main():
    return "Hello World!"


@app.route('/help')
def help():
    return 'Help, I\'m inside this green robot!'

app.add_url_rule('/help', view_func=help)
# needs
app.add_url_rule('/need/all', view_func=need_handlers.all)
app.add_url_rule('/need/<int:need_id>', view_func=need_handlers.by_id)
app.add_url_rule('/need/add', view_func=need_handlers.add)
app.add_url_rule('/need/like/<int:need_id>', view_func=need_handlers.like)
app.add_url_rule('/need/close/<int:need_id>', view_func=need_handlers.close)
app.add_url_rule('/need/remove/<int:need_id>', view_func=need_handlers.remove)
app.add_url_rule('/need/clear', view_func=need_handlers.clear)
# closed needs
app.add_url_rule('/need/closed/all', view_func=closed_need_handlers.all)
app.add_url_rule('/need/closed/<int:need_id>', view_func=closed_need_handlers.byId)
app.add_url_rule('/need/closed/revert/<int:need_id>', view_func=closed_need_handlers.revert)
app.add_url_rule('/need/closed/remove/<int:need_id>', view_func=closed_need_handlers.remove)
app.add_url_rule('/need/closed/clear', view_func=closed_need_handlers.clear)
# users
app.add_url_rule('/user/all', view_func=user_handlers.all)
app.add_url_rule('/user/<int:need_id>', view_func=user_handlers.by_id)
app.add_url_rule('/user/add', view_func=user_handlers.add)
app.add_url_rule('/user/remove/<int:need_id>', view_func=user_handlers.remove)
app.add_url_rule('/user/clear', view_func=user_handlers.clear)
# selections
app.add_url_rule('/selection/by_user/<int:need_id>', view_func=selection_handlers.by_user)
app.add_url_rule('/selection/by_need/<int:need_id>', view_func=selection_handlers.by_need)
app.add_url_rule('/selection/add', view_func=selection_handlers.add)
app.add_url_rule('/selection/remove', view_func=selection_handlers.remove)
app.add_url_rule('/selection/clear', view_func=selection_handlers.clear)

if __name__ == '__main__':
    app.run(debug=True)
