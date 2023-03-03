import sqlite3


def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn


def add_project(conn, project):
   """
   Create a new project into the projects table if it does not already exist
   :param conn:
   :param project:
   :return: project id
   """
   sql = '''SELECT id FROM projects WHERE name = ? AND start_date = ? AND end_date = ?'''
   cur = conn.cursor()
   cur.execute(sql, project)
   row = cur.fetchone()
   if row is not None:
       return row[0]
   else:
       sql = '''INSERT INTO projects(name, start_date, end_date)
                VALUES(?,?,?)'''
       cur = conn.cursor()
       cur.execute(sql, project)
       conn.commit()
       return cur.lastrowid


def add_task(conn, task):
    """
    Create a new task into the tasks table
    :param conn:
    :param task:
    :return: task id
    """
    sql = '''INSERT INTO tasks(project_id, name, description, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":
    project = (("Повторення англійської", "2020-05-08 00:00:00", "2020-05-10 00:00:00"),
               ("PushUps", "2020-05-11 00:00:00", "2020-05-13 00:00:00"))

    conn = create_connection("database.db")
    pr_id = 0
    for p in project:
        pr_id = add_project(conn, p)

    task = (
        (pr_id, "Правильні дієслова", "Запам’ятай дієслова на сторінці 30", "ended", "2020-05-11 12:00:00", "2020-05-11 15:00:00"),
        (pr_id, "Правильні дієслова", "Запам’ятай дієслова на сторінці 31", "started", "2020-05-11 12:00:00", "2020-05-11 15:00:00"),
        (pr_id, "100 PushUps", "4x25", "started", "2020-05-12 12:00:00", "2020-05-12 15:00:00")
    )

    for t in task:
        task_id = add_task(conn, t)

    print(pr_id, task_id)
    conn.close()
