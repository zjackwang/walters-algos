"""
Window.py 
Provides general layout for game

Window
    - Grid
    - Controls
"""

import tkinter as tk
from Grid import Grid


class Window(tk.Tk):

    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        self.grid = Grid(self, 20, 20)

    # want to draw and redraw rectangles individually. 



if __name__ == "__main__":
    window = Window()
    window.mainloop()