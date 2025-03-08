"""
addfamilymembermodal.py

modal form UI for adding new family members to the Family Tracker app.
handles photo uploads and submits new family member data to MongoDB.
"""

import tkinter as tk
import os
from tkinter import filedialog, messagebox
from database.db import family_collection
from utils.utils import center_window
from family.models import FamilyMember
import base64
import pymongo 

class AddFamilyMember():
    """
    modal window for adding a new family member.
    """
    def __init__(self, parent, parent_family_tree_window_frame):
        """
        initializes the add family member modal.

        :param parent: parent window that triggered this modal.
        :param parent_family_tree_window_frame: frame where the modal will be attached.
        """
        self.parent = parent #reference to parent class (family page)
        self.family_tree_window_frame = parent_family_tree_window_frame

        #create modal window for adding family members
        self.add_family_member_window = tk.Toplevel(self.family_tree_window_frame)
        self.add_family_member_window.title('Add Family Member')
        self.add_family_member_window.transient(self.family_tree_window_frame)
        self.add_family_member_window.grab_set()

        #configure modal window grid
        self.add_family_member_window.columnconfigure(0, weight=1)
        self.add_family_member_window.rowconfigure(0, weight=1)

        #frame containing form widgets
        self.add_family_member_window_frame = tk.Frame(self.add_family_member_window, bg='brown') #temporary brown background
        self.add_family_member_window_frame.grid(row=0, column=0, sticky='nsew')

        #first name label and entry
        self.first_name_label = tk.Label(self.add_family_member_window_frame, text='First Name:')
        self.first_name_label.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

        self.first_name_entry = tk.Entry(self.add_family_member_window_frame, font=('Arial', 12))
        self.first_name_entry.grid(row=0, column=1, sticky='ew', padx=5, pady=5, columnspan=2)

        #middle name label and entry
        self.middle_name_label = tk.Label(self.add_family_member_window_frame, text='Middle Name:')
        self.middle_name_label.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        self.middle_name_entry = tk.Entry(self.add_family_member_window_frame, font=('Arial', 12))
        self.middle_name_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=5, columnspan=2)

        #last name label and entry
        self.last_name_label = tk.Label(self.add_family_member_window_frame, text='Last Name:')
        self.last_name_label.grid(row=2, column=0, sticky='ew', padx=5, pady=5)

        self.last_name_entry = tk.Entry(self.add_family_member_window_frame, font=('Arial', 12))
        self.last_name_entry.grid(row=2, column=1, sticky='ew', padx=5, pady=5, columnspan=2)

        #date of birth label and entry
        self.dob_label = tk.Label(self.add_family_member_window_frame, text='Date of Birth:')
        self.dob_label.grid(row=3, column=0, sticky='ew', padx=5, pady=5)

        self.dob_entry = tk.Entry(self.add_family_member_window_frame, font=('Arial', 12))
        self.dob_entry.grid(row=3, column=1, sticky='ew', padx=5, pady=5, columnspan=2)

        #photo upload label and button frame
        self.photo_label = tk.Label(self.add_family_member_window_frame, text='Add a Photo:')
        self.photo_label.grid(row=4, column=0, sticky='ew', padx=5, pady=5)

        self.photo_label_frame = tk.Frame(self.add_family_member_window_frame, bg='brown')
        self.photo_label_frame.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        #photo file path entry
        self.add_photo_entry = tk.Entry(self.photo_label_frame, font=('Arial', 12))
        self.add_photo_entry.grid(row=0, column=0)

        #button to trigger file upload
        self.add_photo_button = tk.Button(self.photo_label_frame, text='+', width=2, height=1, command=self.add_photo, borderwidth=1, padx=0, pady=0)
        self.add_photo_button.grid(row=0, column=1)

        #submit button to save new family member
        self.submit_button = tk.Button(self.add_family_member_window_frame, text='Submit', command=self.submit)
        self.submit_button.grid(row=5, column=1, sticky='ew', padx=5, pady=5)

        #center modal window
        center_window(400, 200, self.add_family_member_window)

    #opens file dialog to select and upload photo
    def add_photo(self):
        """
        opens dialog box for user to add photo
        """
        self.photo_file_path = filedialog.askopenfilename(
            title='Select an Image',
            filetypes=[('PNG Files', '*.png'), ('JPEG Files', '*.jpg;*.jpeg')]
        )

        if self.photo_file_path:
            messagebox.showinfo('Success', f'Photo selected: {self.photo_file_path}')

    #collects data from entries and submits to MongoDB
    def submit(self):
        """
        handles submission of the family member form.
        validates input and saves data to the database.
        """
        #retrieve entry values
        first_name = self.first_name_entry.get()
        middle_name = self.middle_name_entry.get()
        last_name = self.last_name_entry.get()
        dob = self.dob_entry.get()

        #instantiate FamilyMember object
        new_family_member = FamilyMember(first_name, last_name, dob, middle_name, self.photo_file_path)

        # Ensure the selected file exists
        if not self.photo_file_path or not os.path.exists(self.photo_file_path):
            messagebox.showerror("Error", "Selected photo file does not exist.")
            return

        # Ensure the file is a valid image type
        if not self.photo_file_path.lower().endswith((".png", ".jpg", ".jpeg")):
            messagebox.showerror("Error", "Invalid file type. Please select a PNG or JPG image.")
            return

        #encode selected photo to base64 for storage
        try:
            with open(self.photo_file_path, 'rb') as image_file:
                self.photo_conversion = base64.b64encode(image_file.read()).decode("utf-8")
        except Exception as e:
            messagebox.showerror("Error", "Invalid image file selected.")
            return

        #prepare data for database insertion
        self.family_member_data = {
            'first_name': new_family_member.first_name,
            'middle_name': new_family_member.middle_name,
            'last_name': new_family_member.last_name,
            'dob': new_family_member.dob,
            'photo': self.photo_conversion
        }

        #insert data into MongoDB
        try:
            family_collection.insert_one(self.family_member_data)
            messagebox.showinfo('Success', 'Family member successfully added')
            self.parent.populate_family_members() #refreshes family tree UI
            self.add_family_member_window.destroy()
        except (pymongo.errors.PyMongoError, ValueError) as e:
            messagebox.showerror('Error', f'An error occurred: {e}')