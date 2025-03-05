import sys
sys.path.append('C:/Users/rgwin/OneDrive/Desktop/School/Spring2025/SDEV140FP/FamilyTracker')
import tkinter as tk
from tkinter import ttk
from navigation.navbar import NavBar
from utils.utils import center_main
from login.login import LoginModal

def create_nav_frame(container):
    #define navbar frame
    nav_frame = tk.Frame(container, bg='blue', height=300)
    return nav_frame

def create_window_frame(container):
    window_frame = tk.Frame(container, bg='orange')
    window_frame.grid(column=0, row=1, sticky='nsew')
    return window_frame

#create main window
def create_main_window():
    DEBUG_MODE = True

    root = tk.Tk()
    root.title('Family Tracker')


    if not DEBUG_MODE:
        root.withdraw()
        login_modal = LoginModal(root)
        #withdraw so that login validation can occur
        root.wait_window(login_modal.login_window)
        root.deiconify() 

    #configure main_window rows and columns (this was messed up and prevented me from seeing the window_frame)
    root.columnconfigure(0, weight=1) #stretches across columns, all available space? I think
    root.rowconfigure(1, weight=1) #starts at row 1 and stretches to fill the remaining space, i think, within root

    #set window size
    center_main(root)

    #instantiate window frame and put inside of root window, this frame accepts the different navigation windows, family, dashboard, contact, and planner
    main_window_frame = create_window_frame(root)
    main_window_frame.rowconfigure(0, weight=1)
    main_window_frame.columnconfigure(0, weight=1)
    main_window_frame.grid(column=0, row=1)#navbar is in row 0, windowframe is in row1

    #instantiate nav_frame using root as parent container
    nav_frame = create_nav_frame(root)
    #add nav_frame configuration to allow for stretching within nav_frame
    nav_frame.columnconfigure(0, weight=1)
    nav_frame.rowconfigure(0, weight=1)
    #add to root frame using grid, stretch to fill width
    nav_frame.grid(column=0, row=0, sticky='ew')

    #instantiate navbar object, pass nav_frame as parent_container and main_window_frame so that navbar buttons have a frame to put new frames into
    nav = NavBar(nav_frame, main_window_frame) #nav_frame gets passed as the parent container to the navbar frame. 
    
    root.mainloop()

if __name__ == "__main__":
    create_main_window()


"""
this is just a super rudimentary rough draft.  More functionality to come.

to do list for main.py:
1) add navbar.py: done
2) add frame for dashboard.py: done
3) add frame for Family.py: done
4) add frame for planner.py: done
5) add frame for contacts/emergency contacts: done
6) add frame for menu at the top: NOTDONE
7) Make it so that Dashboard is the first window after loggin in? somehow? instead of main, which is orange background.  or..wait no, maybe consider having Main be a welcome/landing page of some sort, and then user can click on dashboard.


other ideas:

create a function in utils to create a frame object instead of creating the function inside of main.py?
"""