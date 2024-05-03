# model/db.py
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "entrypass",
    "port": 3306
}

def get_db():
    db = mysql.connector.connect(**db_config)
    return db
    '''
    cursor = db.cursor()
    try:
        yield cursor
    finally:
        cursor.close()
        db.close()
    '''
