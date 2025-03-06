import tkinter as tk
from tkinter import filedialog, messagebox
from database.db import family_collection
from utils.utils import center_window
from family.models import FamilyMember
import base64
import pymongo 

class AddFamilyMember():
    #look at Login modal to see what it does in its constructor
    #parent is the parent frame that the Toplevel will go into when instantiated in family_page, yes.  So this parent frame needs to be from....familypage.py, at the moment of instantiation, i believe, it gets instantiated in familymember.py, in 'add_family_member()' function

    def __init__(self, parent_family_tree_window_frame):
        self.family_tree_window_frame = parent_family_tree_window_frame
        self.add_family_member_window = tk.Toplevel(self.family_tree_window_frame)
        self.add_family_member_window.title("Add Family Member")
        self.add_family_member_window.transient(self.family_tree_window_frame)
        self.add_family_member_window.grab_set()
        
        #configure row and column to stretch to fill window
        self.add_family_member_window.columnconfigure(0, weight=1)
        self.add_family_member_window.rowconfigure(0, weight=1)

        #create add_family_member frame
        self.add_family_member_window_frame = tk.Frame(self.add_family_member_window, bg='brown') #brown for now
        self.add_family_member_window_frame.grid(row=0, column=0, sticky='nsew')

        #create and place form widgets: get these from FamilyMember class?
        #firstname label
        self.first_name_label = tk.Label(self.add_family_member_window_frame, text="First Name: ")
        self.first_name_label.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        #firstname entry
        self.first_name_entry = tk.Entry(self.add_family_member_window_frame, font=("Arial", 12))
        self.first_name_entry.grid(row=0, column=1, sticky='ew', padx=5, pady=5, columnspan=2)
        #middlename label
        self.middle_name_label = tk.Label(self.add_family_member_window_frame, text="Middle Name: ")
        self.middle_name_label.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        #middlename entry
        self.middle_name_entry = tk.Entry(self.add_family_member_window_frame, font=("Arial", 12))
        self.middle_name_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=5, columnspan=2)
        #lastname label
        self.last_name_label = tk.Label(self.add_family_member_window_frame, text="Last Name: ")
        self.last_name_label.grid(row=2, column=0, sticky='ew', padx=5, pady=5)

        #lastname entry
        self.last_name_entry = tk.Entry(self.add_family_member_window_frame, font=("Arial", 12))
        self.last_name_entry.grid(row=2, column=1, sticky='ew', padx=5, pady=5, columnspan=2)

        #dob label
        self.dob = tk.Label(self.add_family_member_window_frame,text='Date of Birth:')
        self.dob.grid(row=3, column=0, sticky='ew', padx=5, pady=5)

        #dob entry
        self.dob_entry = tk.Entry(self.add_family_member_window_frame, font=("Arial", 12))
        self.dob_entry.grid(row=3, column=1, sticky='ew', padx=5, pady=5, columnspan=2)

        #photo upload label?
        self.photo_label = tk.Label(self.add_family_member_window_frame, text='Add a Photo: ')
        self.photo_label.grid(row=4, column=0, sticky='ew', padx=5, pady=5)

        #photo upload entry that pops up a photo uploader box or whatever, that shit'll be hard
        self.photo_label_frame = tk.Frame(self.add_family_member_window_frame, bg='brown')
        self.photo_label_frame.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        #create Entry field and add_photo_button to photo_label_frame
        self.add_photo_entry = tk.Entry(self.photo_label_frame, font=("Arial", 12))
        self.add_photo_entry.grid(row=0, column=0)


        #create add photo button and add to photolabel frame
        self.add_photo_button = tk.Button(self.photo_label_frame, text='+', width=2, height=1, command=self.add_photo, borderwidth=1, padx=0, pady=0)
        self.add_photo_button.grid(row=0, column=1) 

        #add submit button
        self.submit_button = tk.Button(self.add_family_member_window_frame, text="Submit", command=self.submit)
        self.submit_button.grid(row=5, column=1, sticky='ew', padx=5, pady=5)
        
        #center modal window
        center_window(400, 200, self.add_family_member_window)
    #gets the photo of the family member and returns it to the file_path variable
    def add_photo(self):
        #this doesn't update a global variable/class variable?
        self.photo_file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg")])
        
        if self.photo_file_path:
            messagebox.showinfo("Success", self.photo_file_path)

    def submit(self):
        #get entry values for database injection
        self.first_name_entry_value = self.first_name_entry.get()
        self.middle_name_entry_value = self.middle_name_entry.get()
        self.last_name_entry_value = self.last_name_entry.get()
        self.dob_entry_value = self.dob_entry.get()
        #instantiate new FamilyMember object with firstname, middlename, lastname, dob, and photo
        self.new_family_member = FamilyMember(self.first_name_entry_value, self.last_name_entry_value, self.dob_entry_value, self.middle_name_entry_value, self.photo_file_path)

        #convert photo to base64, and store it into family_member_data below
        with open(self.photo_file_path, 'rb') as self.image_file: #will probably have to convert to str or something
             self.photo_conversion = base64.b64encode(self.image_file.read())
        #get data from familymember object
        self.family_member_data = {
            "first_name": self.new_family_member.first_name,
            "middle_name": self.new_family_member.middle_name,
            "last_name": self.new_family_member.last_name,
            "dob": self.new_family_member.dob,
            "photo": self.photo_conversion
        }

        #send data to db        
        try:
            family_collection.insert_one(self.family_member_data)
            messagebox.showinfo("Success", "Family member successfully added")
            self.add_family_member_window.destroy()
        except (pymongo.errors.PyMongoError, ValueError) as e:
            messagebox.showerror("Error, please address the error and try again")