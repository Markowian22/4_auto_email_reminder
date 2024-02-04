import tkinter as tk
from tkinter.ttk import Label
from tkinter.messagebox import showerror, showwarning, showinfo


root = tk.Tk()
# zmiana tytułu okienka
root.title('create_data')

# napisanie tekstu w okienku
message = tk.Label(root, text='hello')
message.pack()



window_width = 300
window_height = 200

# lokalizacja okienka
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# funckja która znajduje środek ekranu
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# dodanie ikonki do nagłówka 
root.iconbitmap('./assets/pythontutorial.ico') 


# stworzenie przycisku
def button_clicked():
    print('Button clicked')

button = tk.Button(root, text='Click Me', command=button_clicked)


button.pack()

# dodanie zdjecia do okienka
'''photo = tk.PhotoImage(file='./assets/python.png')'''

# stworzenie etykiety - tutaj mozemy zmienic czcionke, tlo itp
label = Label(root, text='This is a label', font=("Helvetica", 10))
# lokalizacja etykiety
label.pack(ipadx=10, ipady=10)

# przycisk Exit
exit_button = tk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)   

# exit_button.pack()
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# stworzenie pola do wpisywania hasła
password = tk.StringVar()
password_entry = tk.Entry(
    root,
    textvariable=password,
    show='*' # ta opcja powoduje ze hasło jest niewidoczne przy wpisywaniu
)
password_entry.pack()

# stworzenie przycisku ktory pokazuje error
tk.Button(
root,
text='Show an error message',
command=lambda: showerror(
    title='Error',
    message='This is an error message.')
).pack()

# stworzenie przycisku ktory pokazuje info
tk.Button(
root,
text='Show an information message',
command=lambda: showinfo(
    title='Information',
    message='This is an information message.')
).pack()




root.mainloop() 