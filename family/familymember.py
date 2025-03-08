"""
familymember.py

creates UI elements representing a family member for display on the Family Information page.
includes logic to handle default profiles and loading/storing images from MongoDB.
"""

import tkinter as tk
from tkinter import PhotoImage
from utils.tooltip import ToolTip
from PIL import Image, ImageTk
import os
import base64
import io

base_dir = os.path.dirname(os.path.abspath(__file__))
default_image = os.path.join(base_dir, "..", "assets", "defaultprofile.png")



class FamilyMemberUI():
     """
     represents a UI component for displaying a family member's information.
     """
     def __init__(self, parent_family_tree_window_frame, family_member_info):
          """
        initializes the UI for a family member.

        :param parent_family_tree_window_frame: parent frame where the family member UI is placed.
        :param family_member_info: dictionary containing family member details.
        """
          #reference to parent frame, used to place UI elements
          self.family_member_frame_container = parent_family_tree_window_frame
          #holds data dictionary for family member (from database)
          self.family_member_data = family_member_info
          
          #generate UI components based on family member data
          if type(self.family_member_data) != None:
               self.create_family_member(self.family_member_data)
 
     #populate family member details from database data
     def create_family_member(self, family_member_data):

          #extract family member details
          self.family_data = family_member_data
          self.first_name = self.family_data["first_name"]
          self.last_name = self.family_data["last_name"]
          self.dob = self.family_data["dob"]
          self.middle_name = self.family_data["middle_name"]
          self.photo = self.family_data["photo"]

          #decode and convert photo from base64 or use default
          if self.family_data["photo"]:
               self.photo_object = base64.b64decode(self.family_data["photo"]) #decode image from base64
               self.pil_photo_image = Image.open(io.BytesIO(self.photo_object))
          else:
               self.photo_object = default_image

          #full name
          self.full_name = self.first_name + " " + self.middle_name + " " + self.last_name

          #family member main container
          self.family_member_frame = tk.Frame(self.family_member_frame_container, width=200, height=300, bg='#808080', borderwidth=3, relief="raised")

          #frame for photo and name
          self.photo_name_frame = tk.Frame(self.family_member_frame, borderwidth=3, relief="sunken")
          self.photo_name_frame.pack(expand=True, fill=None, padx=10, pady=10)

          #name label
          self.name_label = tk.Label(self.photo_name_frame, text=self.full_name, border=1, relief="sunken", font=("Times New Roman", 14))
          self.name_label.pack(padx=5, pady=5, side="top")

          #photo label
          self.photo_image_label = tk.Label(self.photo_name_frame, borderwidth=2, relief="solid")
          self.photo_image_label.pack(expand=True, fill=None, padx=5, pady=5, side="bottom")

          #resize and assign photo to label
          self.photo_image_resized = self.pil_photo_image.resize((165, 200), Image.LANCZOS)
          self.photo_image = ImageTk.PhotoImage(self.photo_image_resized)
          self.photo_image_label.config(image=self.photo_image)
          #apply tooltip (alternate text)
          ToolTip(self.photo_image_label, "Profile Photo")

          #show more details button
          self.show_more_button = tk.Button(self.family_member_frame, text="[+]", command=self.show_more, width=3, height=1)
          self.show_more_button.pack(padx=5, pady=5, side="bottom")
     
     def get_family_member_frame(self):
          """
          retrieves the main frame containing the family member's UI components.
          this frame is used when adding the family member to the family tree canvas.
          
          :return: the tkinter Frame object representing the family member.
          """
          return self.family_member_frame
     
     #feature to come, will show more information about each family member when called
     def show_more(self):
          return
     