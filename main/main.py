import tkinter as tk
from tkinter import ttk


def create_nav_frame(container):
    
    #define fame
    frame = tk.Frame(container, bg='blue', height=75)

    #grid layout for navbar :: what's happening here?
    container.columnconfigure(0, weight=1)


    return frame


def create_main_window():
    root = tk.Tk()
    root.title('Family Tracker')
  
    
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)



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

    nav_frame = create_nav_frame(root)
    nav_frame.grid(column=0, row=0, sticky='ew', columnspan=2)

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


"""