import tkinter as tk

class ToolTip():
    """Creates a simple tooltip that appears when hovering over a widget."""
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None

        # Bind hover events
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        """Create and show the tooltip window."""
        x = self.widget.winfo_rootx() + 20  # Adjust tooltip position
        y = self.widget.winfo_rooty() + 20
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)  # Remove window decorations
        self.tooltip.geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, bg="yellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event):
        """Destroy the tooltip when mouse leaves."""
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
