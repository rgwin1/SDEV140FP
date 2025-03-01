def center_window(window_width, window_height, window_frame):
    """
    Adjusts a Tkinter window's position so it is centered on the screen.

    Args:
        window_frame (Tk or Toplevel): The existing window to be repositioned.
        window_width (Tk or toplevel): The assigned width of the window
        window_height(Tk or toplevel): the assigned height of the window


    Description:
        This function calculates the center coordinates based on the 
        screen dimensions and updates the window's geometry to place 
        it in the middle of the screen.
    """

    window_frame.update_idletasks()
    # window_width = window_frame.winfo_width()
    # window_height = window_frame.winfo_height()
    screen_width = window_frame.winfo_screenwidth()
    screen_height = window_frame.winfo_screenheight()

    #find centerpoint
    center_x = int((screen_width - window_width)/2)
    center_y = int((screen_height - window_height)/2)

    window_frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    
def center_main(window_frame):
    """_summary_

    Args:
        window_frame (_type_): _description_
    """

    window_frame.update_idletasks()
    window_width = int(window_frame.winfo_screenwidth() * 0.40)
    window_height = int(window_frame.winfo_screenheight() * 0.75)
    screen_width = window_frame.winfo_screenwidth()
    screen_height = window_frame.winfo_screenheight()

    center_x = int((screen_width - window_width)/2)
    center_y = int((screen_height - window_height)/2)

    window_frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    