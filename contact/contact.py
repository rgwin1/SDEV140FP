"""
contact.py

creates and manages the contact page frame for the Family Tracker app.
currently contains placeholder UI elements for future implementation.
"""

import tkinter as tk

class Contact():
    """
    represents the contact page frame.
    """

    def __init__(self, window_frame):
        """
        initializes the contact page frame.

        :param window_frame: parent frame where contact UI elements will be placed.
        """

        self.contact_frame = tk.Frame(window_frame, bg='blue', borderwidth=2, relief='solid')

        
        self.contact_frame.grid(column=0, row=0, sticky='nsew')

        self.label = tk.Label(self.contact_frame, text="Contact Feature Coming Soon!", font=("Arial", 20, "bold"))
        self.label.pack(anchor="center", pady=5)