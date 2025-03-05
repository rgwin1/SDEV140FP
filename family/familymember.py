import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from models import FamilyMember
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
default_image = os.path.join(base_dir, "..", "assets", "defaultprofile.png")

class FamilyMemberUI():

#, first_name="", last_name="", dob="", relationship=None, photo=None --- removing for now, don't think i need it, but I might later

     def __init__(self, family_window_frame):
          self.family_member_frame = tk.Frame(family_window_frame, width=200, height=300, bg='gray', borderwidth=3, relief="raised")
          # self.family_member_frame.pack_propagate(False)
          #create button for adding family member
          self.add_family_member_button = tk.Button(self.family_member_frame, text="Add Family Member", command=self.add_family_member, width=20, height=2)
          self.add_family_member_button.pack(side='bottom', padx=5, pady=5)

          #create sub frame for photo label and blank name label
          self.photo_name_frame = tk.Frame(self.family_member_frame, borderwidth=3, relief="sunken")
          # self.photo_name_frame.pack_propagate(False)
  

          #create photo object, i guess
          self.default_profile_photo = tk.PhotoImage(file=default_image)
          #create photo label
          self.default_profile_photo_label = tk.Label(self.photo_name_frame, image=self.default_profile_photo, borderwidth=2, relief="solid")
          self.default_profile_photo_label.pack(expand=True, fill=None, padx=5, pady=5, side="bottom")

          #create blank name label
          self.blank_name_label = tk.Label(self.photo_name_frame, text="Family Member Name")
          self.blank_name_label.pack(padx=5, pady=5, side="top")

          #place photo_name_frame inside of family_member_frame
          self.photo_name_frame.pack(expand=True, fill=None,padx=10, pady=10)


     def add_family_member(self):
          return None


     def get_family_member_frame(self):
          return self.family_member_frame 


"""
add color coding for each family member, so that when an activity for that person appears on the calendar, it's coded by that color.

"""
        


















































"""Notes:

Categories: Each family member will have basic information like name, dob, ssn, etc.
then, other things that are possible to add can be a categorical add, like, school, work, meds, doctors information,
etc, think like, drop down box, where the user "adds" each chunk of info.  Add/delete family members for functionality. Family relationship.

profile? well, each family member can have their own login, i guess? we'll worry about that later. 

"""