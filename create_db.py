import sqlite3
from sqlite3 import Error
import datetime


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn



def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():

    create_table_task = """ CREATE TABLE IF NOT EXISTS weather (
                        id integer PRIMARY KEY NOT NULL,
                        temp float NOT NULL,
                        humidity integer NOT NULL, 
                        date DATE NOT NULL
                        ); """

    create_table2_task = """ CREATE TABLE IF NOT EXISTS max (
                        id integer PRIMARY KEY NOT NULL,
                        max_temp float NOT NULL,
                        max_humidity integer NOT NULL, 
                        date DATE NOT NULL
                        ); """


    conn = create_connection(r"/home/adam/Weatherapp/database.db")

    # create tables
    if conn is not None:
    # create projects table
        create_table(conn, create_table_task)
        create_table(conn, create_table2_task)
    else:
        print("Error! cannot create the database connection.")
    conn.close()
main()
