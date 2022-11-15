import sqlite3


def create_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query = '''CREATE TABLE IF NOT EXISTS Score(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(80) UNIQUE,
        AI_EASY_GAMES INT,
        AI_EASY_WINS INT,
        AI_MEDIUM_GAMES INT,
        AI_MEDIUM_WINS INT,
        AI_HARD_GAMES INT,
        AI_HARD_WINS INT,
        PVP_GAMES INT,
        PVP_WINS INT
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

    query = '''SELECT * FROM Score WHERE name = "Luis"'''
    cursor.execute(query)
    alumno_mostrar = cursor.fetchall()
    connection.commit()

    print("El alumno buscado es:", alumno_mostrar[0][1], alumno_mostrar[0][2])

    cursor.close()
    connection.close()