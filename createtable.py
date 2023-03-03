import sqlite3
from sqlite3 import Error
import os

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
    except Error as e:
        print(e)

    return conn

def execute_sql(conn, sql):
    """ Execute sql
    :param conn: Connection object
    :param sql: a SQL script
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

if __name__ == "__main__":

    create_projects_sql = """
    -- projects table
    CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMARY KEY,
        name text NOT NULL,
        start_date text,
        end_date text
    );
    """

    create_tasks_sql = """
    -- tasks table
    CREATE TABLE IF NOT EXISTS tasks (
        id integer PRIMARY KEY,
        project_id integer NOT NULL,
        name VARCHAR(250) NOT NULL,
        description TEXT,
        status VARCHAR(15) NOT NULL,
        start_date text NOT NULL,
        end_date text NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """

    insert_project_1_sql = """
    -- insert project 1
    INSERT INTO projects(id, name, start_date, end_date)
    VALUES (1,
            "Виконай завдання",
            "2020-05-08 00:00:00",
            "2020-05-10 00:00:00");
    """

    insert_project_2_sql = """
    -- insert project 2
    INSERT INTO projects(name, start_date, end_date)
    VALUES ("Виконай завдання 2",
            "2020-05-08 00:00:00",
            "2020-05-10 00:00:00");
    """

    db_file = "database.db"

    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_projects_sql)
        execute_sql(conn, create_tasks_sql)
        execute_sql(conn, insert_project_1_sql)
        execute_sql(conn, insert_project_2_sql)
        conn.commit()  # add commit here to save changes to the database
        conn.close()
        print("Data inserted successfully")
    else:
        print("Error: Could not create database connection")