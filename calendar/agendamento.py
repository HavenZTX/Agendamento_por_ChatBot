import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def select_date():
    selected_date = cal.get_date()
    print("Data selecionada:", selected_date)

def schedule_event():
    event = event_entry.get()
    date = cal.get_date()
    print("Evento agendado para", date + ":", event)

root = tk.Tk()
root.title("Sistema de Agendamento")

cal = Calendar(root, selectmode="day")
cal.pack(pady=20)

date_button = ttk.Button(root, text="Selecionar Data", command=select_date)
date_button.pack()

event_label = ttk.Label(root, text="Evento:")
event_label.pack()
event_entry = ttk.Entry(root)
event_entry.pack()

schedule_button = ttk.Button(root, text="Agendar Evento", command=schedule_event)
schedule_button.pack()

root.mainloop()
