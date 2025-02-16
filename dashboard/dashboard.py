import tkinter as tk
from tkinter import ttk

class DashBoard():
    def __init__(self, window_frame):
        #first argument is the parent container, in this case the window_frame that will get
        #changed with each button click
        self.frame = tk.Frame(window_frame, bg='green', borderwidth=2, relief='solid')



        self.frame.grid(column=0, row=0, sticky='nsew')
        
        
        # self.frame = tk.Frame(container, bg='orange')

        # self.frame.rowconfigure(0, weight=1)
        # self.frame.columnconfigure(0, weight=1)

        # self.frame.grid(row=0, column=0, sticky='nsew')



