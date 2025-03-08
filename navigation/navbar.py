"""
navbar.py

creates a navigation bar for switching between different sections of the Family Tracker application.
handles navigation to the Dashboard, Family page, Contact page, and Planner.
"""

import tkinter as tk
from dashboard.dashboard import DashBoard
from family.familypage import Family
from contact.contact import Contact
from planner.plannerpage import Planner

class NavBar():
    """
    creates the navigation bar.

    :param nav_frame: the frame that holds the navbar (passed from main.py).
    :param parent_main_window_frame: the main content frame where different pages will be displayed.
    """

    def __init__(self, nav_frame, parent_main_window_frame, parent_root):
        """
        initializes the navbar, sets up the navigation buttons, and stores necessary references.

        :param nav_frame: parent frame that holds the navbar.
        :param parent_main_window_frame: main window frame where content will be loaded.
        """
        #navbar frame holds the navigation buttons
        self.navbar_frame = tk.Frame(nav_frame, bg='#008000')

        #store reference to the main window frame
        self.main_window_frame = parent_main_window_frame

        #create navigation buttons
        self.create_nav_buttons()

        #configure navbar frame layout
        self.navbar_frame.rowconfigure(0, weight=1)
        self.navbar_frame.grid(row=0, column=0, padx=5, pady=5)

        #added root for exit button
        self.root = parent_root

    def create_nav_buttons(self):
        """
        creates the navigation buttons and adds them to the navbar.
        """
        #dashboard button
        self.dash_button = tk.Button(self.navbar_frame, text="Dashboard", command=self.go_to_dashboard, width=20, height=2)
        self.dash_button.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)

        #family button
        self.family_button = tk.Button(self.navbar_frame, text="Family", command=self.go_to_family, width=20, height=2)
        self.family_button.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

        #contact button
        self.contact_button = tk.Button(self.navbar_frame, text="Contact", command=self.go_to_contact, width=20, height=2)
        self.contact_button.grid(row=0, column=2, sticky='ew', padx=5, pady=5)

        #planner button
        self.planner_button = tk.Button(self.navbar_frame, text="Planner", command=self.go_to_planner, width=20, height=2)
        self.planner_button.grid(row=0, column=3, sticky='ew', padx=5, pady=5)

        self.exit_button = tk.Button(self.navbar_frame, text="Exit Program", command=self.exit_program, width=20, height=2)
        self.exit_button.grid(row=0, column=4, sticky='ew', padx=5, pady=5)

    def go_to_dashboard(self):
        """
        navigates to the Dashboard.
        clears the current window and loads the dashboard UI.
        """
        self.clear_window()
        self.dashboard = DashBoard(self.main_window_frame)

    def go_to_family(self):
        """
        navigates to the Family page.
        clears the current window and loads the family tree UI.
        """
        self.clear_window()
        self.family = Family(self.main_window_frame)

    def go_to_contact(self):
        """
        navigates to the Contact page.
        clears the current window and loads the contact UI.
        """
        self.clear_window()
        self.contact = Contact(self.main_window_frame)

    def go_to_planner(self):
        """
        navigates to the Planner page.
        clears the current window and loads the planner UI.
        """
        self.clear_window()
        self.planner = Planner(self.main_window_frame)

    def clear_window(self):
        """
        clears all widgets from the main content frame.
        used before loading a new page.
        """
        for widget in self.main_window_frame.winfo_children():
            widget.destroy()
    
    def exit_program(self):
        """
        allows user to exit the program entirely
        """
        self.root.destroy()