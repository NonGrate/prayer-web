from app.popos import Need
from app.popos import ClosedNeed
import sqlite3


def connect():
    # Connect to the DB file and prepare a table for work
    sqlite = sqlite3.connect('needs.db')
    sqlite.row_factory = dict_factory

    return sqlite


def dict_factory(cursor, row):
    d = {}

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def all(query, parameters=()):
    sqlite = connect()
    cursor = sqlite.cursor()
    cursor.execute(query, parameters)

    result = cursor.fetchall()

    cursor.close()
    sqlite.close()

    return result


def one(query, parameters=()):
    sqlite = connect()
    cursor = sqlite.cursor()
    cursor.execute(query, parameters)

    result = cursor.fetchone()

    cursor.close()
    sqlite.close()

    return result


def update(query, parameters=()):
    sqlite = connect()
    cursor = sqlite.cursor()
    cursor.execute(query, parameters)

    sqlite.commit()
    last_row_id = cursor.lastrowid

    cursor.close()
    sqlite.close()

    return last_row_id


one(
    "CREATE TABLE IF NOT EXISTS needs (content TEXT, rating INTEGER, color INTEGER, date DATETIME DEFAULT CURRENT_TIMESTAMP)")
one(
    "CREATE TABLE IF NOT EXISTS closed_needs (content TEXT, rating INTEGER, color INTEGER, date DATETIME, "
    "update_date DATETIME DEFAULT CURRENT_TIMESTAMP)")


def get_all():
    needs = all("SELECT rowid AS id, content, rating, color, date FROM needs")
    return needs


def get_by_id(need_id):
    need = one("SELECT rowid AS id, content, rating, color, date FROM needs WHERE rowid=?", (need_id,))
    return need


def add_need(content, color):
    last_row_id = update("INSERT INTO needs(content, rating, color) VALUES (?, ?, ?)", (content, 0, color,))
    return {"id": last_row_id}


def like_need(need_id):
    last_row_id = update("UPDATE needs SET rating=rating+1 WHERE rowid=?", (need_id,))
    return get_by_id(need_id)


def close_need(need_id):
    need = get_by_id(need_id)
    remove_need(need_id)
    last_row_id = update("INSERT INTO needs(rowid, content, rating, color, date) VALUES (?, ?, ?, ?, ?)",
                         (need.id, need.content, need.rating, need.color, need.date))
    return {"id": last_row_id}


def remove_need(need_id):
    update("DELETE FROM needs WHERE rowid=?", (need_id,))
    return "", 200


def clear():
    update("DELETE FROM needs")
    return "", 200
