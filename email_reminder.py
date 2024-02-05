import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv

from dotenv import load_dotenv

from database_manager import Database


class MailMessage:
    """
    The MailMessage class is responsible for managing the email application,
    including sending reminder emails to users.
    """

    def __init__(self, smtp_server: str, port: int):
        """
        Initializes the Aplication class by setting up the SMTP
        server and logging in.

        Args:
            smtp_server (str): The address of the SMTP server to connect to.
            port (int): The port to use for the SMTP connection.
        """
        self.smtp_server = smtp_server
        self.port = port
        load_dotenv()

        self.context = ssl.create_default_context()
        self.context.check_hostname = False
        self.context.verify_mode = ssl.CERT_NONE

        self.server = smtplib.SMTP_SSL(
            self.smtp_server, self.port, context=self.context
        )
        self.server.login(getenv("EMAIL"), getenv("PASSWORD"))

    def send_reminder_emails_to_overdue_users(self, sender: str, db: Database):
        """
        Sends reminder emails to users who have overdue books.

        Args:
            sender (str): The email address from which the reminders are sent.
            db (Database): The database object to use for fetching user data.
        """
        reminder = db.check_users_book_return_date()
        for id, email, name, book_title, return_at, date_diff in reminder:
            text = f"""Hey {name},<br>
            you are <b>{int(date_diff)}</b> days overdue for your book.<br>
            ID: <b>{id}</b>"""

            try:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = "Przypomnienie"
                msg["From"] = sender
                msg["To"] = email

                html = f"""\
                <html>
                <body>
                    <p>{text}</p>
                </body>
                </html>
                """
                part = MIMEText(html, "html")
                msg.attach(part)

                self.server.sendmail(sender, email, msg.as_string())
            except Exception as e:
                print(f"Błąd wysyłania wiadomości: {e}")
