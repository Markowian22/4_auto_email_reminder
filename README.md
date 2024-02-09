# Reminder Application

## Overview
The Library Reminder Application is a Python-based application designed to manage a library's user database and send reminder emails to users who have overdue books. The application uses SQLite for database management, SMTP for email notifications, and Tkinter for the graphical user interface.

## Files
The application consists of the following files:

1. `database_manager.py`: Contains the `Database` class for managing the SQLite database.
2. `email_reminder.py`: Contains the `MailMessage` class for sending email notifications.
3. `user_interface.py`: Contains the `Gui` class for managing the graphical user interface.
4. `main.py`: Contains the main function that ties all the components together.

## Classes and Methods
Each file contains a class that encapsulates a specific part of the application:

- `Database`: Manages the SQLite database.
    - `insert_data(email: str, name: str, book_title: str, return_at: str)`: Inserts user data into the database.
    - `delete_data(id: int)`: Deletes user data from the database based on the provided id.
    - `check_users_book_return_date()`: Checks the return dates of all books borrowed by users and returns those that are overdue.

- `MailMessage`: Manages the email notifications.
    - `send_reminder_emails_to_overdue_users(sender: str, db: Database)`: Sends reminder emails to users who have overdue books.

- `Gui`: Manages the graphical user interface.
    - `create_button(text, command, row, column)`: Creates a button widget with the given properties.

## Setup
To run the application, you need to have Python installed on your machine. You also need to install the required dependencies, which can be done by running `pip install -r requirements.txt`.

## Before first run
To run the project you must put your email config to .env file. See example.

## Usage
To start the application, run `python main.py` from the command line.
