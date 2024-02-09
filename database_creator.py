def init_db(db_cursor: str):
    """
    Initializes the database by creating a new
    table if it doesn't already exist.

    Args:
        db_cursor (str): The cursor object
        that interacts with the SQLite database.

    The table, named 'users_data', has the following columns:
        - id: An integer that serves as the primary key.
        - email: A text field to store the user's email.
        - name: A text field to store the user's name.
        - book_title: A text field to store the title of the book.
        - return_at: A date field to store the return date of the book.

    The combination of 'email', 'name', and 'book_title' is unique,
    meaning there can't be two entries
    with the same email, name, and book title.
    """
    db_cursor.execute(
        """
                        CREATE TABLE IF NOT EXISTS users_data
                        (id INTEGER PRIMARY KEY,
                        email TEXT,
                        name TEXT,
                        book_title TEXT,
                        return_at DATE,
                        UNIQUE(email, name, book_title )
                            )
                    """
    )
