import sys
sys.path.append('C:/Users/rgwin/OneDrive/Desktop/School/Spring2025/SDEV140FP/FamilyTracker')
import tkinter as tk
from tkinter import ttk
from navigation.navbar import NavBar


def create_nav_frame(container):
    
    #define frame
    frame = tk.Frame(container, bg='blue', height=300)
    #commenting out these for testing
    # frame.columnconfigure(0, weight=1)
    # frame.rowconfigure(0, weight=1)
    return frame

def create_window_frame(container):
    frame = tk.Frame(container, bg='orange')

    frame.grid(column=0, row=1, sticky='nsew')
    # frame.columnconfigure(0, weight=1)
    #frame.rowconfigure(1, weight=1)

    return frame


# def create_dashboard_window():
#     #define window
#     window =tk.Tk()
#     window.title('Dashboard')

#     window.geometry("500x500")

def create_main_window():
    root = tk.Tk()
    root.title('Family Tracker')

    
    #configure main_window rows and columns (this was messed up and prevented me from seeing the window_frame)
    root.columnconfigure(0, weight=1) #stretches across columns, all available space? I think

    root.rowconfigure(1, weight=1) #starts at row 1 and stretches to fill the remaining space, i think, within root

    #set window size
    window_width = 1500
    window_height = 1000

    #get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    #find the center point
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)

    #set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    #instantiate window frame
    window_frame = create_window_frame(root)
    window_frame.rowconfigure(0, weight=1)
    window_frame.columnconfigure(0, weight=1)
    window_frame.grid(column=0, row=1)#navbar is in row 0, windowframe is in row1


    #instantiate nav_frame
    nav_frame = create_nav_frame(root)
    #look at the configuring in a moment, do I need to add it here if it's added in the navbar.py? 
    nav_frame.columnconfigure(0, weight=1)
    nav_frame.rowconfigure(0, weight=1)
    #add to widget using grid
    nav_frame.grid(column=0, row=0, sticky='ew')

    #add to widget using pack
    #nav_frame.pack(anchor="center", pady=10)
    nav = NavBar(nav_frame, window_frame) #nav_frame gets passed as the parent container to the navbar frame.   See below



    #instantiate window frame functionality(?)



    root.mainloop()

if __name__ == "__main__":
    create_main_window()


"""
this is just a super rudimentary rough draft.  More functionality to come.

to do list for main.py:
1) add navbar.py
2) add frame for dashboard.py
3) add frame for Family.py
4) add frame for planner.py
5) add frame for contacts/emergency contacts
6) add frame for menu at the top



root = Tk() //creates the root object

root.geometry("400x400") // sets the window size in terms of pixels

//create frame 1
frame1 = Frame(root, bg="black", width=500, height=300) #sets the frame up in size and location (root window)
frame1.pack() //puts the frame1 in the root object

//create frame 2
frame2 = Frame(frame1, bg="white", width=100, heigh=100)
frame2.pack(pady=20, padx=20)

root.mainloop() // do the thing












"""