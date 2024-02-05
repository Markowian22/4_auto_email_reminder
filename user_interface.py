import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label

from database_manager import Database


class Gui(tk.Tk):
    """
    The Gui class is responsible for managing the graphical user
    interface of the application.
    """

    def __init__(self, db: Database):
        """
        Initializes the App class by setting up the
        window and creating the necessary widgets.

        Args:
            db (Database): The database object to use for fetching user data.
        """
        super().__init__()

        # configure the root window
        self.title("okienko")
        window_width = 600
        window_height = 300

        # window localization
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # function which finds the centre of the screen
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        # text fields
        self.entry1 = tk.Entry(self, width=10)
        self.entry1.grid(row=0, column=0)
        self.entry1.insert(0, "email")
        self.entry1.bind("<FocusIn>", lambda args: self.entry1.delete("0", "end"))

        self.entry2 = tk.Entry(self, width=10)
        self.entry2.grid(row=0, column=1)
        self.entry2.insert(0, "imie")
        self.entry2.bind("<FocusIn>", lambda args: self.entry2.delete("0", "end"))

        self.entry3 = tk.Entry(self, width=10)
        self.entry3.grid(row=0, column=2)
        self.entry3.insert(0, "tytul")
        self.entry3.bind("<FocusIn>", lambda args: self.entry3.delete("0", "end"))

        self.entry4 = tk.Entry(self, width=10)
        self.entry4.grid(row=0, column=3)
        self.entry4.insert(0, "data zwrotu")
        self.entry4.bind("<FocusIn>", lambda args: self.entry4.delete("0", "end"))

        self.combobox = ttk.Combobox(self, values=db._get_all_user_id(), width=5)
        self.combobox.grid(row=2, column=3)
        label = Label(self, text="Select ID")
        # # lokalizacja etykiety
        label.grid(row=2, column=2)

    def create_button(self, text, command, row, column):
        """
        Creates a button widget with the given properties.

        Args:
            text (str): The text to display on the button.
            command (function): The function to execute
            when the button is clicked.
            row (int): The row in which to place the button in the grid.
            column (int): The column in which to place the button in the grid.
        """
        button = tk.Button(self, text=text, command=command)
        button.grid(row=row, column=column)
