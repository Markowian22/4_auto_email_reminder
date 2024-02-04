import sqlite3
from dotenv import load_dotenv
from os import getenv


class Database:
    """
    The Database class is responsible for managing the connection to an
    SQLite3 database and performing operations on the data.
    """
    def __init__(self):
        load_dotenv()
        self.connection = sqlite3.connect(getenv('DB_NAME'))
        self.cursor = self.connection.cursor()

    def __del__(self):
        try:
            self.connection.close()
        except Exception as e:
            print('error during function call - __del__', e)

    def insert_data(self, email: str, name: str,
                    book_title: str, return_at: str):
        """
        Inserts user data into the database.

        Args:
            email (str): The email of the user.
            name (str): The name of the user.
            book_title (str): The title of the book the user is borrowing.
            return_at (str): The date when the book is to be returned.
        """
        try:
            sql = 'INSERT INTO users_data VALUES(null, ?, ?, ?, ?)'
            self.cursor.execute(sql, (email, name, book_title, return_at))
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(e)

    def delete_data(self, id: int):
        """
        Deletes user data from the database based on the provided id.

        Args:
            id (int): The id of the user whose data is to be deleted.
        """
        try:
            sql = 'DELETE FROM users_data WHERE id=?'
            self.cursor.execute(sql, (id,))
            self.connection.commit()
        except Exception as e:
            print('error while deleting data', e)

    def check_users_book_return_date(self):
        try:
            sql = '''SELECT *,
                    JULIANDAY(return_at) - JULIANDAY(DATE('now')) as DATE_DIFF
                    FROM users_data
                    WHERE return_at < DATE('now')
                    '''
            return self.cursor.execute(sql).fetchall()
        except Exception as e:
            print('error during function call check_users_book_return_date', e)

    def _get_all_user_id(self):
        try:
            sql = "select id from users_data"
            result = self.cursor.execute(sql).fetchall()
            return [element[0] for element in result]
        except Exception as e:
            print('error during function call', e)
