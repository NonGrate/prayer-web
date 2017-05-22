import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Connect to the DB file and prepare a table for work
sqlite = sqlite3.connect('needs.db')
sqlite.row_factory = dict_factory

create = sqlite.cursor()
create.execute("CREATE TABLE IF NOT EXISTS needs (content TEXT, rating INTEGER, color INTEGER)")
create.close()


def get_all():
    cursor = sqlite.cursor()
    cursor.execute("SELECT rowid AS id, content, rating, color FROM needs")
    needs = cursor.fetchall()
    cursor.close()

    return needs


def get_by_id(need_id):
    cursor = sqlite.cursor()
    cursor.execute("SELECT rowid AS id, content, rating, color FROM needs WHERE rowid=?", (need_id, ))
    need = cursor.fetchone()
    cursor.close()

    return need


def add_need(content, color):
    cursor = sqlite.cursor()
    cursor.execute("INSERT INTO needs VALUES (?, ?, ?)", (content, 0, color, ))
    sqlite.commit()
    last_row_id = cursor.lastrowid
    cursor.close()

    return last_row_id


def like_need(need_id):
    cursor = sqlite.cursor()
    cursor.execute("UPDATE needs SET rating=rating+1 WHERE rowid=?", (need_id, ))
    sqlite.commit()
    cursor.close()

    rating = get_by_id(need_id)["rating"]

    return rating


def clear():
    cursor = sqlite.cursor()
    cursor.execute("DELETE FROM needs")
