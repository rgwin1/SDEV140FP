"""
planner.py

creates and manages the planner page frame for the Family Tracker app.
currently contains placeholder UI elements for future implementation.
"""

import tkinter as tk

class Planner():
    """
    represents the planner page frame.
    """

    def __init__(self, window_frame):
        """
        initializes the planner page frame.

        :param window_frame: parent frame where the planner UI elements will be placed.
        """
        # window_frame.columnconfigure(0, weight=1)
        # window_frame.rowconfigure(0, weight=1)
        # window_frame.update_idletasks()
        self.planner_frame = tk.Frame(window_frame, bg='blue', borderwidth=2, relief='solid')
        self.planner_frame.pack(anchor="center", fill="both", expand=True)
     

        #future feature placeholder frame
        self.future_feature_frame = tk.Frame(self.planner_frame, bg="lightblue", padx=10, pady=10)
        self.future_feature_frame.pack(anchor="center", fill="both", expand=True)
        #placeholder label
        self.label = tk.Label(self.future_feature_frame, bg="lightblue", text="Planner Feature Coming Soon!", font=("Arial", 20, "bold"))
        self.label.pack(anchor="center", fill="both", expand=True)
