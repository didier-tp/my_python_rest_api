import sqlite3

with sqlite3.connect("devises.db") as connection:
    cursor = connection.cursor()
    '''
    cursor.execute(
        "CREATE TABLE devise (code TEXT PRIMARY KEY ,name TEXT, change DOUBLE)")
    connection.commit()

    cursor.execute(
        "INSERT INTO devise(code, name, change) VALUES('CCC', 'devise_ccc', 123.456)")
    connection.commit()
    '''
    rows = cursor.execute(
        "SELECT * FROM devise").fetchall() #or .fetchone()
    print(rows)