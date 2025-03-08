"""
familypage.py

creates the family tree canvas and loads family members dynamically.
handles the add family member button, which opens a modal for user input.
"""

import tkinter as tk
from family.familymember import FamilyMemberUI
from database.db import family_collection
from utils.utils import calculate_x_position, calculate_y_position
from family.addfamilymembermodal import AddFamilyMember

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
            family_member_object = FamilyMemberUI(self.family_tree_canvas, family_member_dict)

            #retrieve the frame containing family member details
            family_member_frame = family_member_object.get_family_member_frame()

            #add family member UI to canvas at calculated position
            self.family_tree_canvas.create_window(x, y, window=family_member_frame)

            #force UI update to reflect changes
            self.family_tree_canvas.update_idletasks()