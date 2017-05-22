import sqlite3

# Connect to the DB file and prepare a table for work
sqlite = sqlite3.connect('needs.db')

create = sqlite.cursor()
create.execute("CREATE TABLE IF NOT EXISTS needs (content TEXT, rating INTEGER, color INTEGER)")
create.close()


def get_all():
    cursor = sqlite.cursor()
    cursor.execute("SELECT rowid, content, rating, color FROM needs")
    needs = cursor.fetchall()
    cursor.close()

    return needs


def get_by_id(need_id):
    cursor = sqlite.cursor()
    cursor.execute("SELECT rowid, content, rating, color FROM needs WHERE rowid=?", (need_id, ))
    rowid, content, rating, color = cursor.fetchone()
    cursor.close()

    return rowid, content, rating, color


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

    rating = get_by_id(need_id)[2]

    return rating


def clear():
    cursor = sqlite.cursor()
    cursor.execute("DELETE FROM needs")
