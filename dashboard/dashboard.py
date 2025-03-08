"""
dashboard.py

creates and manages the dashboard page UI, including calendar, to-do list, and notes widgets.
"""

import tkinter as tk
from datetime import datetime

class DashBoard:
    def __init__(self, parent):
        self.parent = parent #reference to parent frame

        self.parent.columnconfigure(0, weight=1) #to-do list (left column)
        self.parent.columnconfigure(1, weight=2) #calendar (middle column, wider)
        self.parent.columnconfigure(2, weight=1) #notes (right column)

        #to-do list widget setup
        self.to_do_frame = tk.Frame(self.parent, bg='#A52A2A', padx=10, pady=10)
        self.to_do_frame.grid(row=0, column=0, sticky='nsew')

        self.to_do_label = tk.Label(self.to_do_frame, text='To-Do List', font=('Arial', 14, 'bold')) #to-do list title label
        self.to_do_label.pack(anchor='center', pady=5)

        self.add_task_button = tk.Button(self.to_do_frame, text='Add Task', command=self.add_task) #button to add a task
        self.add_task_button.pack(anchor='center', pady=5)

        #calendar (middle column)
        self.calendar_frame = tk.Frame(self.parent, bg='#FFA500', padx=10, pady=10)
        self.calendar_frame.grid(row=0, column=1, sticky='nsew')

        self.calendar_label = tk.Label(self.calendar_frame, text="Today's Schedule", font=('Arial', 16, 'bold')) #calendar header label
        self.calendar_label.pack(anchor='center', pady=5)

        today = datetime.today().strftime('%A %m/%d/%Y') #formatted date string
        self.date_label = tk.Label(self.calendar_frame, text=today, font=('Arial', 12)) #today's date label
        self.date_label.pack(anchor='center', pady=5)

        self.add_event_button = tk.Button(self.calendar_frame, text='Add Event', command=self.add_event) #button to add event
        self.add_event_button.pack(anchor='center', pady=5)

        #notes (right column)
        self.notes_frame = tk.Frame(self.parent, bg='#A52A2A', padx=10, pady=10)
        self.notes_frame.grid(row=0, column=2, sticky='nsew')

        self.notes_label = tk.Label(self.notes_frame, text='Notes', font=('Arial', 14, 'bold')) #notes section label
        self.notes_label.pack(anchor='center', pady=5)

        self.add_notes_button = tk.Button(self.notes_frame, text='Add Note', command=self.add_note) #button to add note
        self.add_notes_button.pack(anchor='center', pady=5)

    def add_task(self):
        """handles adding a task (to be implemented)."""
        print("Add Task button clicked")

    def add_event(self):
        """handles adding an event (to be implemented)."""
        print("Add Event button clicked")

    def add_note(self):
        """handles adding a note (to be implemented)."""
        print("Add Note button clicked")