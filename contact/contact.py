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
        
        self.contact_frame = tk.Frame(window_frame, bg='#0000FF', borderwidth=2, relief='solid')
        self.contact_frame.pack(anchor="center", fill="both", expand=True)

        #future feature placeholder frame
        self.future_feature_frame = tk.Frame(self.contact_frame, bg="#ADD8E6")
        self.future_feature_frame.pack(anchor="center", fill="both", expand=True)

        self.label = tk.Label(self.future_feature_frame, bg="#ADD8E6", text="Contact Feature Coming Soon!", font=("Arial", 20, "bold"))
        self.label.pack(anchor="center", fill="both", expand=True)