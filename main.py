from os import getenv

from dotenv import load_dotenv

from database_creator import init_db
from database_manager import Database
from email_reminder import MailMessage
from user_interface import Gui

if __name__ == "__main__":
    load_dotenv()
    db = Database(getenv("DB_NAME"))
    init_db(db.cursor)
    tk_inter = Gui(db)
    mail = MailMessage("smtp.gmail.com", 465, getenv("EMAIL"), getenv("PASSWORD"))

    def send_email():
        db_reminder = db.check_users_book_return_date()

        return mail.send_reminder_emails_to_overdue_users(
            getenv("EMAIL"), db_reminder=db_reminder
        )

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
        send_email,
        3,
        4,
    )

    tk_inter.mainloop()
