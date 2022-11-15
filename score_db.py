import sqlite3


def create_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query = '''CREATE TABLE IF NOT EXISTS Score(
        id SERIAL PRIMARY KEY,
        name VARCHAR(80) UNIQUE,
        ai_easy_games INT,
        ai_easy_wins INT,
        ai_medium_games INT,
        ai_medium_wins INT,
        ai_hard_games INT,
        ai_hard_wins INT,
        pvp_games INT,
        pvp_wins INT
    );'''
    cursor.execute(query)

    cursor.close()
    connection.close()


def insert_data():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query = '''INSERT INTO Alumnos(name, surname) VALUES
    ('Juan', 'Garcia'),
    ('Pedro', 'Podesta'),
    ('Viviana', 'Canosa')'''
    cursor.execute(query)
    connection.commit()

    cursor.close()
    connection.close()


def return_data():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query = '''SELECT * FROM Alumnos WHERE name = "Luis"'''
    cursor.execute(query)
    alumno_mostrar = cursor.fetchall()
    connection.commit()

    print("El alumno buscado es:", alumno_mostrar[0][1], alumno_mostrar[0][2])

    cursor.close()
    connection.close()