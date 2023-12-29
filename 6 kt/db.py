import sqlite3
import os

DB_NAME = "dbase.db"

def create_tables(conn):
    cursor = conn.cursor()

    # Создание таблицы Покупатель
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Buyer (
            id INTEGER PRIMARY KEY,
            name TEXT,
            dog_id INTEGER,
            FOREIGN KEY (dog_id) REFERENCES Dog(id)
        )
    """)

    # Создание таблицы Питомник
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Kennel (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)

    # Создание таблицы Собака
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Dog (
            id INTEGER PRIMARY KEY,
            name TEXT,
            kennel_id INTEGER,
            buyer_id INTEGER,
            FOREIGN KEY (kennel_id) REFERENCES Kennel(id),
            FOREIGN KEY (buyer_id) REFERENCES Buyer(id)
        )
    """)

    conn.commit()

def db_connection():
    db_exists = os.path.isfile(DB_NAME)
    conn = sqlite3.connect(DB_NAME)

    if not db_exists:
        create_tables(conn)

    return conn