import sqlite3
from activity import Activity

def create(activity):
    conn = sqlite3.connect("sqlite3/database.db")
    query = conn.cursor()

    arguments = (
        activity.type,
        activity.reps,
        activity.totalTime,
        activity.weight,
        activity.date,

    )

    sql = '''
        INSERT INTO activities (type, reps, totalTime, weight, date)
        VALUES (?, ?, ?, ?, ?)
    '''

    if (query.execute(sql, arguments)):
        query.close()
        conn.commit()
        conn.close()

def get_by_date(date):
    conn = sqlite3.connect("sqlite3/database.db")
    query = conn.cursor()

    sql = 'SELECT * FROM activities WHERE date = %s' % date

    if (query.execute(sql)):
        rows = query.fetchall()
        activities =[]

        for row in rows:
            activity = Activity(row[0], row[1], row[2], row[3], row[4], row[5])
            activities.append(activity)

        query.close()
        conn.commit()
        conn.close()
        return activities
    else:
        return "An error has ocurred"

def get_by_type(type):
    conn = sqlite3.connect("sqlite3/database.db")
    query = conn.cursor()

    sql = 'SELECT * FROM activities WHERE type = %s' % type

    if (query.execute(sql)):
        rows = query.fetchall()
        activities =[]

        for row in rows:
            activity = Activity(row[0], row[1], row[2], row[3], row[4], row[5])
            activities.append(activity)

        query.close()
        conn.commit()
        conn.close()
        return activities
    else:
        return "An error has ocurred"

def get_by(id):
    conn = sqlite3.connect("sqlite3/database.db")
    query = conn.cursor()

    sql = 'SELECT * FROM activities WHERE id = %s' % id

    if (query.execute(sql)):
        row = query.fetchone()
        if not row:
            return None

        activity = Activity(row[0], row[1], row[2], row[3], row[4], row[5])

        query.close()
        conn.commit()
        conn.close()
        return activity
    else:
        return "An error has ocurred"

def remove(activity):
    conn = sqlite3.connect("sqlite3/database.db")
    query = conn.cursor()

    sql = 'DELETE FROM activities WHERE id = %s' % activity.id

    if (query.execute(sql)):
        query.close()
        conn.commit()
        conn.close()

def edit(activity):
    conn = sqlite3.connect("sqlite3/database.db")
    query = conn.cursor()

    arguments = (
        activity.type,
        activity.reps,
        activity.totalTime,
        activity.weight,
        activity.id
    )

    sql = '''
        UPDATE activities SET
        type = ?, reps = ?, totalTime = ?, weight = ?
        WHERE id = ?
    '''

    if (query.execute(sql, arguments)):
        query.close()
        conn.commit()
        conn.close()
