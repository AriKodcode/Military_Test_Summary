import csv
from connrction.conn import connection

def soldiers_table():
    conn = connection()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS soldiers (personal_number INTEGER, first_name TEXT, last_name TEXT, gender TEXT, city TEXT, distance_from_base INTEGER)")

    with open("C:/Users/internet/Desktop/Military Test Summary/data/soldiers.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        cur.executemany("INSERT INTO soldiers VALUES (?, ?, ?, ?, ?, ?)", reader)

    conn.commit()
    conn.close()
soldiers_table()