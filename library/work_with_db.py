import sqlite3


def read_info_ship():
    con = sqlite3.connect('library/DataGame.db')
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM info_player""").fetchall()
    con.commit()
    con.close()
    return list(result[0])


def read_score():
    con = sqlite3.connect('DataGame.db')
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM Height_score""").fetchall()
    con.commit()
    con.close()
    return list(result[0])


def update_cell(id, name_cell, object):
    con = sqlite3.connect('library/DataGame.db')
    cur = con.cursor()
    cur.execute(f"""UPDATE info_player SET {name_cell} == {object} WHERE id == {id}""")
    con.commit()
    con.close()


def add_cell(name, score):
    con = sqlite3.connect('library/DataGame.db')
    cur = con.cursor()
    cur.execute(f"""INSERT INTO Height_score(NamePlayer, score)
                    VALUES ('{name}', {score})""")
    con.commit()
    con.close()


print(read_score())