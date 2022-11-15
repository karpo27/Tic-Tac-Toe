import sqlite3


def create_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query = '''CREATE TABLE IF NOT EXISTS Score(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(80) UNIQUE,
        AI_EASY_WINS INT DEFAULT 0,
        AI_EASY_LOSES INT DEFAULT 0,
        AI_EASY_TIES INT DEFAULT 0,
        AI_MEDIUM_WINS INT DEFAULT 0,
        AI_MEDIUM_LOSES INT DEFAULT 0,
        AI_MEDIUM TIES INT DEFAULT 0,
        AI_HARD_WINS INT DEFAULT 0,
        AI_HARD_LOSES INT DEFAULT 0,
        AI_HARD_TIES INT DEFAULT 0,
        PVP_WINS INT DEFAULT 0,
        PVP_LOSES INT DEFAULT 0,
        PVP_TIES INT DEFAULT 0
);'''
    cursor.execute(query)

    cursor.close()
    connection.close()


def insert_player_name(p_name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query = f'''INSERT OR IGNORE INTO Score(NAME) VALUES ('{p_name}');'''
    cursor.execute(query)
    connection.commit()

    cursor.close()
    connection.close()


def return_data():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query_select = f'''SELECT * FROM Score WHERE NAME = '';'''
    cursor.execute(query_select)
    a = cursor.fetchall()
    connection.commit()

    print(a)

    cursor.close()
    connection.close()


def update_player_score(p_name, g_mode, result):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    category = {
        "1": ['AI_EASY_WINS', 'AI_EASY_LOSES', 'AI_EASY_TIES'],
        "2": ['AI_MEDIUM_WINS', 'AI_MEDIUM_LOSES', 'AI_MEDIUM_TIES'],
        "3": ['AI_HARD_WINS', 'AI_HARD_LOSES', 'AI_HARD_TIES'],
        "4": ['PVP_WINS', 'PVP_LOSES', 'PVP_TIES']
    }

    query_update = f'''UPDATE Score SET {category[g_mode][result]} = {category[g_mode][result]} + 1 WHERE NAME = '{p_name}';'''
    cursor.execute(query_update)
    connection.commit()

    cursor.close()
    connection.close()
