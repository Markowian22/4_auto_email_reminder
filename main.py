from database_manager import Database
from email_reminder import MailMessage
from user_interface import Gui
from os import getenv





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


if __name__ == "__main__":

    db = Database()
    init_db(db.cursor)
    tk_inter = Gui(db)
    mail = MailMessage("smtp.gmail.com", 465)

    tk_inter.create_button(
        "Insert Data",
        lambda: db.insert_data(
            tk_inter.entry1.get(),
            tk_inter.entry2.get(),
            tk_inter.entry3.get(),
            tk_inter.entry4.get(),
        ),
        0,
        4,
    )

    tk_inter.create_button(
        "Delete Data",
        lambda: db.delete_data(
            tk_inter.combobox.get(),
        ),
        2,
        4,
    )

    tk_inter.create_button(
        "send reminder",
        mail.send_reminder_emails_to_overdue_users(getenv("EMAIL"), db),
        3,
        4,
    )

    tk_inter.mainloop()
