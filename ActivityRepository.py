import sqlite3
from activity import Activity

def create(activity):
    conn = sqlite3.connect("sqlite3/database.db")
    query = conn.cursor()

    arguments = (
        activity.type,
        activity.reps,
        activity.id_act,
        activity.totalTime,
        activity.weight
    )

    sql = '''
        INSERT INTO activities (type, reps, id_act, totalTime, weight)
        VALUES (?, ?, ?, ?, ?)
    '''

    if (query.execute(sql, arguments)):
        query.close()
        conn.commit()
        conn.close()
        return "Activity created successfully"
    else:
        return "An error has ocurred"

def get_all():
    conn = sqlite3.connect("sqlite3/database.db")
    query = conn.cursor()

    sql = 'SELECT * FROM activities'

    if (query.execute(sql)):
        rows = query.fetchall()
        activities =[]

        for row in rows:
            activity = Activity(row[1],row[2],row[3],row[4],row[5])
            activities.append(activity)

        query.close()
        conn.commit()
        conn.close()
        return activities
    else:
        return "An error has ocurred"

def get_by(id_act):
    conn = sqlite3.connect("sqlite3/database.db")
    query = conn.cursor()

    sql = 'SELECT * FROM activities WHERE id_act = %s' % id_act

    if (query.execute(sql)):
        row = query.fetchone()
        if not row:
            return None

        activity = Activity(row[1],row[2],row[3],row[4],row[5])

        query.close()
        conn.commit()
        conn.close()
        return activity
    else:
        return "An error has ocurred"

def remove(activity):
    conn = sqlite3.connect("sqlite3/database.db")
    query = conn.cursor()

    sql = 'DELETE FROM activities WHERE id_act = %s' % activity.id_act

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
        activity.id_act
    )

    sql = '''
        UPDATE activities SET
        type = ?, reps = ?, totalTime = ?, weight = ?
        WHERE id_act = ?
    '''

    if (query.execute(sql, arguments)):
        query.close()
        conn.commit()
        conn.close()
