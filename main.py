from requests import get 
import sqlite3
from sqlite3 import Error
import datetime

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def insert_data(conn, data, sql_task):
    cur=conn.cursor()
    cur.execute(sql_task, data)    
    conn.commit()          
 


def calculate_max_value(rows, i):
    if len(rows) == 0:
        print("ERROR! za mało rekordów w tabeli")
        return None
    max_value = rows[0][i]
    for j in range(1, len(rows)):
        max_value = max(max_value, rows [j][i])
    return max_value






#tasks

def get_data(conn, date):
    select_task = f"""SELECT temp, humidity FROM weather 
                    WHERE date(date) = '{date}'
                            
                            ;"""
    cur = conn.cursor()
    cur.execute(select_task)

    rows = cur.fetchall()
    return rows

     
        


def calculate_max_data():
    conn = create_connection(r"/home/adam/Weatherapp/database.db")
    if conn is None:
        print("Error! cannot create the database connection.")
        return
    date =  datetime.date.today()   
    #print(date)
    
    rows = get_data(conn, date)
    #print(rows)
    max_temp = calculate_max_value(rows, 0)
    max_humidity = calculate_max_value(rows, 1)
    
    data = [max_temp, max_humidity, date]

    sql_task = """INSERT INTO max (max_temp, max_humidity, date)
                VALUES (?, ?, ?)
                ;"""

    insert_data(conn, data, sql_task)

    #print(max_temp, max_humidity)
    
def save_data_from_weather_api():
    city_name = "Tuchola"

    key = "de6cb5fabc397519fe1d678dfe5a87ba"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric"

    r = get(url)
    #print(r.json())

    temp = r.json()["main"]["temp"]
    humidity = r.json() ["main"]["humidity"]

    date = datetime.datetime.today() #data dzisiejsza
    
    data = (temp, humidity, date)
    
    insert_task = f"""INSERT INTO weather (temp, humidity, date)
                     VALUES (?, ?, ?);
                    """
    
    conn = create_connection(r"/home/adam/Weatherapp/database.db")
    if conn is not None:
        insert_data(conn, data, insert_task)
    else:
        print("Error! cannot create the database connection.")
    
    #print(temp)
    #print(humidity)
 
    
    
    conn.close

calculate_max_data()
