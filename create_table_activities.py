import sqlite3

conn = sqlite3.connect("sqlite3/database.db")
query = conn.cursor()

sql = '''
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        type TEXT NOT NULL,
        reps INTEGER NOT NULL,
        id_act INTEGER NOT NULL,
        totalTime INTEGER NOT NULL,
        weight INTEGER NOT NULL
    )'''

if (query.execute(sql)):
    print("Table created successfully")
else:
    print("An error has ocurred")

query.close()

conn.commit()

conn.close()
