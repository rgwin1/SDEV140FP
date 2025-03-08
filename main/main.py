"""
main.py

launches the Family Tracker application.
creates the main window, navigation bar, and page frames.
handles user login before displaying the main interface.
"""

import sys
import os

#dynamically add the project root to sys.path to allow module imports from any directory.
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import tkinter as tk
from tkinter import ttk
from navigation.navbar import NavBar
from utils.utils import center_main
from login.login import LoginModal

#define navbar frame
def create_nav_frame(container):
    """
    creates a navigation frame inside the main window.
    """
    nav_frame = tk.Frame(container, bg='blue', height=300)
    return nav_frame

#define main content frame where different pages will be displayed
def create_window_frame(container):
    """
    creates the primary content frame for displaying different pages (dashboard, family, planner, etc.).
    """
    window_frame = tk.Frame(container, bg='orange')
    window_frame.grid(column=0, row=1, sticky='nsew')
    return window_frame

#create and initialize the main application window
def create_main_window():
    """
    initializes the main application window, handles login, and sets up navigation and content frames.
    """
    DEBUG_MODE = False  #set to True to disable login for debugging purposes

    root = tk.Tk()
    root.title('Family Tracker')

    #if not in debug mode, show login modal before displaying main application
    if not DEBUG_MODE:
        root.withdraw() #hide main window until login is successful
        login_modal = LoginModal(root)
        root.wait_window(login_modal.login_window) #wait for login window to close
        root.deiconify() #restore main window after successful login

    #configure main window layout
    root.columnconfigure(0, weight=1) #expand to full width
    root.rowconfigure(1, weight=1) #content frame expands to fill remaining space

    #set window size and center on screen
    center_main(root)

    #instantiate content frame (holds different pages)
    main_window_frame = create_window_frame(root)
    main_window_frame.rowconfigure(0, weight=1)
    main_window_frame.columnconfigure(0, weight=1)
    main_window_frame.grid(column=0, row=1) #navbar is row 0, content frame is row 1

    #instantiate navigation bar frame
    nav_frame = create_nav_frame(root)
    nav_frame.columnconfigure(0, weight=1)
    nav_frame.rowconfigure(0, weight=1)
    nav_frame.grid(column=0, row=0, sticky='ew') #stretch to full width

    #create and attach navigation bar
    nav = NavBar(nav_frame, main_window_frame, root)

    #start the application loop
    root.mainloop()

#run the application
if __name__ == "__main__":
    create_main_window()

