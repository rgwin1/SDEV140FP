"""
models.py

defines the FamilyMember class, which represents a family member object.
includes validation for names, date of birth, and photo format.
"""

from datetime import datetime
import os

class FamilyMember:
    """
    represents a family member with personal details.
    """

    #class-level variables for default values
    base_dir = os.path.dirname(os.path.abspath(__file__)) #get base directory of the file
    default_photo = os.path.join(base_dir, "..", "assets", "defaultprofile.png") #default profile photo path

    def __init__(self, first_name, last_name, dob, middle_name=None, photo=None, additional_info=None):
        """
        initializes a family member object.

        :param first_name: first name of the family member.
        :param last_name: last name of the family member.
        :param dob: date of birth in MM/DD/YYYY format.
        :param middle_name: (optional) middle name of the family member.
        :param photo: (optional) path to the family member's photo.
        :param additional_info: (optional) dictionary of extra details.
        """
        self._first_name = None
        self._last_name = None
        self._dob = None
        self._photo = None

        #initialize attributes using property setters (enforces validation)
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self._middle_name = middle_name #middle name is optional, no setter needed
        self.photo = photo

        #ensure additional_info is initialized, defaulting to an empty dictionary
        self.additional_info = additional_info if additional_info else {}

    @property
    def first_name(self):
        """returns the first name of the family member."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """
        sets and validates the first name.

        :param value: first name string.
        :raises ValueError: if first name is empty.
        """
        if not value:
            raise ValueError("First name cannot be empty")
        self._first_name = value.strip().title()

    @property
    def middle_name(self):
        """returns the middle name of the family member (if any)."""
        return self._middle_name

    @property
    def last_name(self):
        """returns the last name of the family member."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        sets and validates the last name.

        :param value: last name string.
        :raises ValueError: if last name is empty.
        """
        if not value:
            raise ValueError("Last name cannot be empty")
        self._last_name = value.strip().title()

    @property
    def dob(self):
        """returns the date of birth of the family member."""
        return self._dob

    @dob.setter
    def dob(self, value):
        """
        sets and validates the date of birth.

        :param value: date of birth string in MM/DD/YYYY format.
        :raises ValueError: if date format is incorrect.
        """
        try:
            self._dob = datetime.strptime(value, "%m/%d/%Y")
        except ValueError:
            raise ValueError("DOB must be in MM/DD/YYYY format.")

    @property
    def photo(self):
        """returns the path to the family member's photo or a default photo."""
        return self._photo if self._photo else self.default_photo

    @photo.setter
    def photo(self, value):
        """
        sets and validates the photo path.

        :param value: path to the image file.
        :raises ValueError: if the file is not a supported image format.
        """
        if value and not value.lower().endswith((".png", ".jpg", ".jpeg")):
            raise ValueError("Photo must be a .png, .jpg, or .jpeg file.")
        self._photo = value
