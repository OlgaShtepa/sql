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

def delete_last_task(conn):
   """
   Delete the last row from the tasks table
   :param conn: Connection object
   :return:
   """
   sql = 'DELETE FROM tasks WHERE id = (SELECT MAX(id) FROM tasks);'
   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()

if __name__ == "__main__":
    conn = create_connection("database.db")
    delete_last_task(conn)
    conn.close()
