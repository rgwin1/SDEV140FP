import tkinter as tk
from tkinter import ttk
from family.familymember import FamilyMemberUI



class Family():
    def __init__(self, family_window_frame):
        #using canvas and putting it into the family_window_frame that is created in navbar.py
        self.family_tree_canvas = tk.Canvas(family_window_frame, width=400, height=200, bg="white")
        self.family_tree_canvas.pack(fill="both", expand=True)

        #instantiating a family member object
        self.family_member_object = FamilyMemberUI(self.family_tree_canvas)
        self.family_member_frame = self.family_member_object.get_family_member_frame()
        self.family_tree_canvas.create_window(300, 200, window=self.family_member_frame)

        # self.family_member_object.get_family_member_frame().pack()

