import tkinter as tk
from tkinter import ttk
from dashboard.dashboard import DashBoard
from family.familypage import Family
from contact.contact import Contact
from planner.plannerpage import Planner


class NavBar():
    """creates the navbar object"""
    def __init__(self, container, window_frame):

    # Initialize the navbar, set up the frame, and store any necessary references
        # self.frame = tk.Frame(container, bg='red', height=25)
        self.navbar_frame = tk.Frame(container, bg='blue')
        self.window_frame = window_frame
 
        # Create the navigation buttons and add them to the navbar
        #dashboard button
        self.dash_button = tk.Button(self.navbar_frame, text="Dashboard", command=self.go_to_dashboard, width=20, height=2)
        self.dash_button.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)

        #Family button
        self.family_button = tk.Button(self.navbar_frame, text="Family", command=self.go_to_family, width=20, height=2)
        self.family_button.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

        #Contact Button
        self.contact_button = tk.Button(self.navbar_frame, text="Contact", command=self.go_to_contact, width=20, height=2)
        self.contact_button.grid(row=0, column=2, sticky='ew', padx=5, pady=5)

        #Planner Button
        self.planner_button = tk.Button(self.navbar_frame, text="Planner", command=self.go_to_planner, width=20, height=2)
        self.planner_button.grid(row=0, column=3, sticky='ew', padx=5, pady=5)

        #revisit these now that I have a better understanding how the row/col configuring works
        self.navbar_frame.rowconfigure(0, weight=1)
        self.navbar_frame.grid(row=0, column=0, padx=5, pady=5)
        

    # Define the functions for handling button clicks and navigation logic
    # dashboard
    def go_to_dashboard(self):
        #clear the current window
        for widget in self.window_frame.winfo_children():
            widget.destroy()
        #instantiate a dashframe object
        self.dashboard = DashBoard(self.window_frame)

   #family
    def go_to_family(self):
        for widget in self.window_frame.winfo_children():
            widget.destroy()
        self.family = Family(self.window_frame)

    #contact
    def go_to_contact(self):
        for widget in self.window_frame.winfo_children():
            widget.destroy()
        self.contact = Contact(self.window_frame)

    #planner
    def go_to_planner(self):
        for widget in self.window_frame.winfo_children():
            widget.destroy()
        self.contact = Planner(self.window_frame)

    # Apply any styling, customization options, or layout settings
    
    # (Optional) If needed, set up methods to modify the navbar dynamically (e.g., show/hide, update styles)
