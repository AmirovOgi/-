import sqlite3
import pytest
from db import *

# Тестовые данные
BUYER_NAME = "Alice Smith"
KENNEL_NAME = "Cozy Kennels"
DOG_NAME = "Max"


@pytest.fixture(scope='session')
def db_connection():
    connection = db_connection()
    print('Initializing Database')
    yield connection
    connection.close()
    print('Finalizing Database')


@pytest.fixture(scope='function')
def initialized_db():
    """Инициализирует базу данных и создает необходимые таблицы."""
    conn = sqlite3.connect(DB_NAME)
    create_tables(conn)
    yield conn
    conn.close()


def test_insert_data(initialized_db):
    """Тестирует операцию вставки данных в таблицы."""
    cursor = initialized_db.cursor()
    cursor.execute("INSERT INTO Buyer (name, dog_id) VALUES (?, ?)", (BUYER_NAME, 1))
    cursor.execute("INSERT INTO Kennel (name) VALUES (?)", (KENNEL_NAME,))
    cursor.execute("INSERT INTO Dog (name, kennel_id, buyer_id) VALUES (?, ?, ?)", (DOG_NAME, 1, None))
    cursor.execute("SELECT * FROM Buyer WHERE name=?", (BUYER_NAME,))
    
    initialized_db.commit()
    result = cursor.fetchone()
    
    assert result is not None
    assert result[1] == "Alice Smith"


def test_select_data(initialized_db):
    """Тестирует операцию выборки данных из таблицы Dog."""
    cursor = initialized_db.cursor()
    cursor.execute("SELECT * FROM Dog")
    result = cursor.fetchall()
    
    assert len(result) > 0


def test_update_data(initialized_db):
    """Тестирует операцию обновления данных в таблице Buyer."""
    cursor = initialized_db.cursor()
    cursor.execute("UPDATE Buyer SET name=? WHERE id=?", ("New Buyer Name", 1))
    cursor.execute("SELECT name FROM Buyer WHERE id=?", (1,))
    result = cursor.fetchone()
    
    assert result is not None


def test_delete_data(initialized_db):
    """Тестирует операцию удаления данных из таблиц Buyer, Dog и Kennel."""
    cursor = initialized_db.cursor()
    cursor.execute("DELETE FROM Buyer WHERE name=?", (BUYER_NAME,))
    cursor.execute("DELETE FROM Dog WHERE name=?", (DOG_NAME,))
    cursor.execute("DELETE FROM Kennel WHERE name=?", (KENNEL_NAME,))

    initialized_db.commit()
    
    # Проверка удаления данных
    for table in ["Buyer", "Dog", "Kennel"]:
        cursor.execute(f"SELECT * FROM {table}")
        result = cursor.fetchone()
        assert result is None
