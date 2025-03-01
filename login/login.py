import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.utils import center_window
# import os
# import json
# import hashlib

class LoginModal():
    test_credentials = {
            "admin": "password123"
        }
     
    def __init__(self, parent):
        self.login_window = tk.Toplevel(parent)
        self.parent = parent
        self.login_window.title("Login")
        self.login_window.update_idletasks() #ensures window is fully drawn
        self.login_window.focus_force() #forces login modal to be active window
        self.login_window.grab_set() #locks interaction to this window, preventing users from accessing main window
        self.login_window.resizable(False, False) #prevent login window from being resized, see comment A below
        self.login_window.protocol("WM_DELETE_WINDOW", self.prevent_close)
        self.login_window.bind("<Return>", self.login_command)

        #configure row and column to stretch to fill window
        self.login_window.columnconfigure(0, weight=1)
        self.login_window.rowconfigure(0, weight=1)
        
        #create login frame 
        self.login_frame = tk.Frame(self.login_window, bg='brown')
        self.login_frame.grid(row=0, column=0, sticky="nsew")



        #create and place username label
        self.username_label = tk.Label(self.login_frame, text="Username: ")
        self.username_label.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

        #create and place username input
        self.username_input = tk.Entry(self.login_frame)
        self.username_input.grid(row=0, column=1, sticky='ew', padx=5, pady=5, columnspan=2)
        self.username_input.focus_set()

        #create password_label
        self.password_label = tk.Label(self.login_frame, text="Password: ")
        self.password_label.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        #create password_input
        self.password_input = tk.Entry(self.login_frame, show="*")
        self.password_input.grid(row=1, column=1, sticky='ew', padx=5, pady=5, columnspan=2)

        #create login_button
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login_command, width=15)
        self.login_button.grid(row=2, column=1, padx=5, pady=5)

        #create acount creation button (does nothing for now)
        self.create_account_button = tk.Button(self.login_frame, text="Create Account", command=self.create_account, width=15)
        self.create_account_button.grid(row=2, column=2, padx=5, pady=5)

        #center login relative to parent (dashboard in this case)
        center_window(325, 100, self.login_window)
    #do this later
    def create_account(self):
        return None
    
    def login_command(self, event=None):
        self.username_value = self.username_input.get()
        self.password_value = self.password_input.get()

        if self.test_credentials.get(self.username_value) == self.password_value:
            self.login_window.destroy() #terminates window after successful login
            self.parent.deiconify() #returns dashboard window to the front
            messagebox.showinfo("Login Successful", "Welcome")
        elif self.username_value not in self.test_credentials:
            messagebox.showerror("User not found.")
        else:
            messagebox.showerror("Incorrect username or password")
        
    def prevent_close(self):
        pass
 #A:  may try to make frame within frame and center frame to stretch as login window stretches, determine later
