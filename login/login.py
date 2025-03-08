"""
login.py

creates a login modal window that prevents access to the main dashboard until successful login.
includes basic authentication using test credentials (to be replaced with database integration).
"""

import tkinter as tk
from tkinter import messagebox
from utils.utils import center_window

class LoginModal():
    #temporary dictionary storing test credentials (to be replaced with database authentication)
    test_credentials = {
        "admin": "password123"
    } 

    def __init__(self, parent):
        #initialize login modal as a separate top-level window
        self.login_window = tk.Toplevel(parent)
        self.parent = parent #reference to parent window (dashboard)

        #configure login window properties
        self.login_window.title("Login")
        self.login_window.update_idletasks() #ensures window is fully drawn
        self.login_window.focus_force() #forces login modal to be active window
        self.login_window.grab_set() #locks interaction to this window, preventing users from accessing main window
        self.login_window.resizable(False, False) #prevents resizing of login window
        self.login_window.protocol("WM_DELETE_WINDOW", self.prevent_close) #disables manual close button (X)
        self.login_window.bind("<Return>", self.login_command) #bind Enter key to trigger login

        #configure grid layout for login window
        self.login_window.columnconfigure(0, weight=1)
        self.login_window.rowconfigure(0, weight=1)

        #create login frame container
        self.login_frame = tk.Frame(self.login_window, bg='brown')
        self.login_frame.grid(row=0, column=0, sticky="nsew")

        #username label and input field
        self.username_label = tk.Label(self.login_frame, text="Username: ")
        self.username_label.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

        self.username_input = tk.Entry(self.login_frame)
        self.username_input.grid(row=0, column=1, sticky='ew', padx=5, pady=5, columnspan=2)
        self.username_input.focus_set() #set focus to username input on load

        #password label and input field
        self.password_label = tk.Label(self.login_frame, text="Password: ")
        self.password_label.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        self.password_input = tk.Entry(self.login_frame, show="*") #hides password characters
        self.password_input.grid(row=1, column=1, sticky='ew', padx=5, pady=5, columnspan=2)

        #login button
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login_command, width=15)
        self.login_button.grid(row=2, column=1, padx=5, pady=5)

        #account creation button (currently does nothing)
        self.create_account_button = tk.Button(self.login_frame, text="Create Account", command=self.create_account, width=15)
        self.create_account_button.grid(row=2, column=2, padx=5, pady=5)

        #center login window relative to parent window (dashboard)
        center_window(325, 100, self.login_window)

    #placeholder function for future account creation feature
    def create_account(self):
        return None
    
    #handles user login authentication
    def login_command(self, event=None):
        self.username_value = self.username_input.get()
        self.password_value = self.password_input.get()

        #check if entered credentials match test credentials
        if self.test_credentials.get(self.username_value) == self.password_value:
            self.login_window.destroy() #close login modal on successful login
            self.parent.deiconify() #restore access to parent window (dashboard)
            messagebox.showinfo("Login Successful", "Welcome")
        elif self.username_value not in self.test_credentials:
            messagebox.showerror("Error", "User not found.")
        else:
            messagebox.showerror("Error", "Incorrect username or password")

    #prevents login modal from being closed before successful login
    def prevent_close(self):
        pass

