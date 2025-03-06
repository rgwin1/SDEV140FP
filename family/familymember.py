import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from family.addfamilymembermodal import AddFamilyMember
import os
from database.db import family_collection

import base64
from PIL import Image, ImageTk
import io


base_dir = os.path.dirname(os.path.abspath(__file__))
default_image = os.path.join(base_dir, "..", "assets", "defaultprofile.png")

class FamilyMemberUI():

#, first_name="", last_name="", dob="", relationship=None, photo=None --- removing for now, don't think i need it, but I might later
     """
     parent_family_tree_window_frame is the parent frame from familymember.py
     """
     def __init__(self, parent_family_tree_window_frame):

          self.family_member_frame_container = parent_family_tree_window_frame
          
                  
          #create button for adding family member, shouldn't get changed at all
          self.add_family_member_button = tk.Button(self.family_member_frame_container, text="Add Family Member", command=self.add_family_member, width=20, height=2)
          self.add_family_member_button.pack(side='bottom', padx=5, pady=5)

          if family_collection.find_one() is None:
               self.show_default_object()
          else:
               self.create_family_member()

     #create function for default object if no family members exist in database
     def show_default_object(self):
          #create main frame for everything to go
          self.family_member_frame = tk.Frame(self.family_member_frame_container, width=200, height=300, bg='gray', borderwidth=3, relief="raised")
          #create sub frame for photo label and blank name label, family_member_frame is parent_frame to photo_name_frame
          self.photo_name_frame = tk.Frame(self.family_member_frame, borderwidth=3, relief="sunken")

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

          #add show more button
          self.show_more_button = tk.Button(self.family_member_frame, text="[+]", command=self.show_more, width=3, height=1)
          self.show_more_button.pack(side='bottom', padx=5, pady=5)
          
     #get family member from database and convert to family_member object///maybe split this into 2 different functions?
     def create_family_member(self):
          #get family member data from mongo database
          self.family_data = family_collection.find_one()
          if self.family_data:
               self.first_name = self.family_data["first_name"],
               self.last_name = self.family_data["last_name"],
               self.dob = self.family_data["dob"],
               self.middle_name=self.family_data["middle_name"],
               self.photo = self.family_data["photo"]
          else:
               pass #do something here, i'm not sure what, error message?


            #get photo
          if self.family_data["photo"]:
               self.photo_object = base64.b64decode(self.family_data["photo"]) #decode from binary
               self.pil_photo_image = Image.open(io.BytesIO(self.photo_object)) #convert to PIL image

          else:
               self.photo_object = default_image



          self.full_name = self.first_name[0] + " " + self.middle_name[0] + " " + self.last_name[0]


          self.family_member_frame = tk.Frame(self.family_member_frame_container, width=200, height=300, bg='gray', borderwidth=3, relief="raised")
          self.photo_name_frame = tk.Frame(self.family_member_frame, borderwidth=3, relief="sunken")
          #place photo_name_frame inside of family_member_frame
          self.photo_name_frame.pack(expand=True, fill=None, padx=10, pady=10)

          # self.full_name = self.first_name + " " + self.middle_name + " " + self.last_name //if i can get it to work
          self.name_label = tk.Label(self.photo_name_frame, text=self.full_name, border=1, relief="sunken", font=("Times New Roman", 14))
          self.name_label.pack(padx=5, pady=5, side="top")
          
          #create photo label and add photo image box to photo_name_frame
          self.photo_image_label = tk.Label(self.photo_name_frame, borderwidth=2, relief="solid")
          self.photo_image_label.pack(expand=True, fill=None, padx=5, pady=5, side="bottom")


          #get photo widget dimensions
          self.widget_width = self.photo_image_label.winfo_width()
          self.widget_height = self.photo_image_label.winfo_height()

          #resize photo
          self.photo_image_resized = self.pil_photo_image.resize((165, 200), Image.LANCZOS) #this wont work
          self.photo_image = ImageTk.PhotoImage(self.photo_image_resized) #convert photo image to Tk image
          self.photo_image_label.config(image=self.photo_image)
  


          
          #add show more button to family_member_frame
          self.show_more_button = tk.Button(self.family_member_frame, text="[+]", command=self.show_more, width=3, height=1)
          self.show_more_button.pack(padx=5, pady=5, side="bottom")
          
         
    
     def add_family_member(self):
          #create the modal
          """"
          AddFamilyMember(parent_frame)....the modal is going to be created within the family_member_frame? but that doesn't make sense, 
          because family_member_frame is where the UI for the family_member_object goes.  The frame that needs to get passed to AddFamilyMember() is the frame where the modal window
          will be created, soo....family_member_window? or the canvas itself? """
          self.add_family_member_modal = AddFamilyMember(self.family_member_frame_container) 
          return self.add_family_member_modal


     def get_family_member_frame(self):
          return self.family_member_frame #why do this?
     
     def show_more(self):
          #create another widget for showing more

          #show dob

          return None


"""
add color coding for each family member, so that when an activity for that person appears on the calendar, it's coded by that color.

just need to add a for loop to dynamically create new family members if more than 1 exist in the database, then done with this

"""
        


















































"""Notes:

Categories: Each family member will have basic information like name, dob, ssn, etc.
then, other things that are possible to add can be a categorical add, like, school, work, meds, doctors information,
etc, think like, drop down box, where the user "adds" each chunk of info.  Add/delete family members for functionality. Family relationship.

profile? well, each family member can have their own login, i guess? we'll worry about that later. 

"""