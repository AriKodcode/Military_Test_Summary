import sqlite3

def connection():
    conn = sqlite3.connect("base.db")
    return conn