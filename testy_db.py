import pytest

from database_manager import Database


@pytest.fixture
def create_connection():
    connection = Database(":memory:")
    cursor = connection.cursor
    cursor.execute(
        """
                        CREATE TABLE IF NOT EXISTS users_data
                        (id INTEGER PRIMARY KEY,
                        email TEXT,
                        name TEXT,
                        book_title TEXT,
                        return_at DATE
                        
                            )
                    """
    )

    sample_data = [
        (1, "marekd@gmail.com", "Marek", "pustynia", "2022-12-12"),
        (2, "kamil@gmail.com", "kamil", "pustynia2", "2024-12-12"),
        (3, "kamil@gmail.com", "kamil", "pustynia2", "1998-12-12"),
    ]

    cursor.executemany("INSERT INTO users_data VALUES(?, ?, ?, ?, ?)", sample_data)

    return connection


def test_connection(create_connection):
    connection = create_connection
    users = connection.check_users_book_return_date()
    for user in users:
        print(user)

    users_id = connection._get_all_user_id()
    print(users_id)


# test_connection()
