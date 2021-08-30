"""
Window.py 
Provides general layout for game

Window
    - Grid
    - Controls
"""

import tkinter as tk    
from .Grid import Grid
from .CPanel import CPanel


class Window(tk.Tk):

    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        self.cpanel = CPanel(self)
        self.grid = Grid(self, 10, 10)

if __name__ == "__main__":
    window = Window()
    window.mainloop()