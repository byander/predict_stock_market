import mysql.connector

def connect():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        db="acoes"
    )
    return con


