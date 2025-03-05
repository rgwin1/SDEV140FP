from datetime import datetime
import os

#create Family member model class
class FamilyMember:
    #class level variables
    base_dir = os.path.dirname(os.path.abspath(__file__))
    default_photo = os.path.join(base_dir, "..", "assets", "defaultprofile.png")

    def __init__(self, first_name, last_name, dob, middle_name=None, photo=None, additional_info=None):
        #placeholders
        self._first_name = None
        self._last_name = None
        self._dob = None
        self._photo = None
        #call setters
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.photo = photo
        #ensure middle_name is initialized
        self._middle_name = middle_name
        #ensure additional_info is initialized, and defaults to empty dictionary
        self.additional_info = additional_info if additional_info else {}

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if not value:
            raise ValueError("First name cannot be empty")
        self._first_name = value.strip().title() 

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if not value:
            raise ValueError("Last name cannot be empty")
        self._last_name = value.strip().title()
    
    @property
    def middle_name(self):
        return self._middle_name
    
    @property
    def dob(self):
        return self._dob
    
    @dob.setter
    def dob(self, value):
        try:
            self._dob = datetime.strptime(value,"%Y-%m-%d").date() #convert string to date
        except ValueError:
            raise ValueError("DOB must be in YYYY-MM-DD format.")
        
    @property
    def photo(self):
            return self._photo if self._photo else self.default_photo #will return a photo unless none provided, then provides default profile photo
        
    
    @photo.setter
    def photo(self, value):
        if value and not value.lower().endswith((".png", ".jpg", ".jpeg")):
            raise ValueError("Photo must be a .png, .jpg, or .jpeg file.")
        self._photo = value