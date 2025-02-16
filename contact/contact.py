import tkinter as tk
from tkinter import ttk


class Contact():
    def __init__(self, window_frame):
        self.frame = tk.Frame(window_frame, bg='yellow', borderwidth=2, relief='solid')
        self.frame.grid(column=0, row=0, sticky='nsew')
