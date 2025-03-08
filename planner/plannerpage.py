"""
planner.py

creates and manages the planner page frame for the Family Tracker app.
currently contains placeholder UI elements for future implementation.
"""

import tkinter as tk
from tkinter import ttk

class Planner():
    """
    represents the planner page frame.
    """

    def __init__(self, window_frame):
        """
        initializes the planner page frame.

        :param window_frame: parent frame where the planner UI elements will be placed.
        """
        self.frame = tk.Frame(window_frame, bg='blue', borderwidth=2, relief='solid')
        self.frame.grid(column=0, row=0, sticky='nsew')

        #future feature placeholder frame
        self.future_feature_frame = tk.Frame(self.frame, bg="lightblue", padx=10, pady=10, height=300, width=300)
        self.future_feature_frame.pack(fill="both", expand=True, padx=5, pady=5)

        #placeholder label
        self.label = tk.Label(self.future_feature_frame, text="Planner Feature Coming Soon", font=("Arial", 20, "bold"))
        self.label.pack(anchor="center", pady=5)
