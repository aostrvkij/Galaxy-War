import sqlite3

conn = sqlite3.connect('Ships.db')
cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS Ships(shipsid INT PRIMARY KEY, Name TEXT,  Info TEXT,   Speed INTEGER,
# hp INTEGER,   sprite_way TEXT);""")
# cur.execute("""CREATE TABLE IF NOT EXISTS Armor(armorid INT PRIMARY KEY, Name TEXT,  Info TEXT,   type_armour TEXT,
# number INTEGER);""")
# cur.execute("""CREATE TABLE IF NOT EXISTS Gun(gunid INT PRIMARY KEY, Name TEXT,  Info TEXT,   bullet_delay INTEGER,
# hp INTEGER,   sprite_way TEXT);""")
# conn.commit()

