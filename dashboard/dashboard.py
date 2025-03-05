import tkinter as tk
from tkinter import ttk


class DashBoard():
    def __init__(self, dashboard_window_frame):
        #first argument is the parent container, in this case the window_frame that will get
        #changed with each button click
        self.dashboard_frame = tk.Frame(dashboard_window_frame, bg='green', borderwidth=2, relief='solid')
        self.dashboard_frame.grid(column=0, row=0, sticky='nsew')

