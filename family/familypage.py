"""
familypage.py

creates the family tree canvas and loads family members dynamically.
handles the add family member button, which opens a modal for user input.
"""

import tkinter as tk
from family.familymember import FamilyMemberUI
from database.db import family_collection
from utils.utils import calculate_x_position, calculate_y_position
from utils.tooltip import ToolTip
from family.addfamilymembermodal import AddFamilyMember
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
default_image = os.path.join(base_dir, "..", "assets", "defaultprofile.png")


class Family():
    """
    family tree UI container that loads inside the main application frame.
    manages canvas where family members are displayed.
    """
    
    def __init__(self, parent_family_window_frame):
        """
        initializes the family tree UI.

        :param parent_family_window_frame: parent frame where the family tree will be placed.
        """
        #reference to parent frame (passed from navbar when "Family" button is clicked)
        self.family_window_frame = parent_family_window_frame
        
        #canvas for rendering family tree
        self.family_tree_canvas = tk.Canvas(self.family_window_frame, width=400, height=200, bg="white")
        self.family_tree_canvas.pack(fill="both", expand=True)

        #add family member button (instantiated once when Family() is created)
        self.add_family_member_button = tk.Button(self.family_tree_canvas, text="Add Family Member", command=self.add_family_member, width=20, height=2)
        self.add_family_member_button.pack(side='bottom', padx=5, pady=5)

        #populate existing family members

        if not family_collection.find_one():
            self.show_default_object()
        else:
            self.populate_family_members()
    
    #opens the add family member modal
    def add_family_member(self):
        """
        creates a modal window for adding a family member.
        modal attaches to the family tree canvas.
        """
        self.add_family_member_modal = AddFamilyMember(self, self.family_tree_canvas)

    #loads family members from database and adds them to the UI
    def populate_family_members(self):
        """
        retrieves all family members from the database, creates UI elements for them,
        and places them dynamically inside the canvas.
        """
        self.family_tree_canvas.delete("all") #clear previous family members

        #retrieve all family members from MongoDB
        family_member_info = list(family_collection.find())

        #loop through each stored family member and place them in the UI
        for index, family_member_dict in enumerate(family_member_info):
            x = calculate_x_position(index) #calculate x coordinate dynamically
            y = calculate_y_position(index) #calculate y coordinate dynamically
            
            #create a FamilyMemberUI object
            self.family_member_object = FamilyMemberUI(self.family_tree_canvas, family_member_dict)

            #retrieve the frame containing family member details
            self.family_member_frame = self.family_member_object.get_family_member_frame()

            #add family member UI to canvas at calculated position
            self.family_tree_canvas.create_window(x, y, window=self.family_member_frame)

            #force UI update to reflect changes
            self.family_tree_canvas.update_idletasks()


        
    def show_default_object(self):
        #main container frame
        self.family_member_frame = tk.Frame(self.family_tree_canvas, width=200, height=300, bg='gray', borderwidth=3, relief="raised")
        self.family_tree_canvas.create_window(200, 200, window=self.family_member_frame)

        #subframe for photo and name labels
        self.photo_name_frame = tk.Frame(self.family_member_frame, borderwidth=3, relief="sunken")
        #pack photo and name frame
        self.photo_name_frame.pack(expand=True, fill=None, padx=10, pady=10)

        #default profile photo
        self.default_profile_photo = tk.PhotoImage(file=default_image)

        #label for profile photo
        self.default_profile_photo_label = tk.Label(self.photo_name_frame, image=self.default_profile_photo, borderwidth=2, relief="solid")
        self.default_profile_photo_label.pack(expand=True, fill=None, padx=5, pady=5, side="bottom")

        #blank placeholder name label
        self.blank_name_label = tk.Label(self.photo_name_frame, text="Family Member Name") #placeholder name label
        self.blank_name_label.pack(padx=5, pady=5, side="top")

        #show more details button
        self.show_more_button = tk.Button(self.family_member_frame, text="[+]", command=self.show_more, width=3, height=1)
        self.show_more_button.pack(side='bottom', padx=5, pady=5)

        ToolTip(self.default_profile_photo_label, "Default Profile Photo")

    #placeholder for future detail expansion functionality
    def show_more(self):
        return None