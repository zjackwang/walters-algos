"""
Grid.py 
Layout will be an N x M grid 
"""
from time import sleep
import tkinter as tk

class Grid():
    """
    Initialize the Grid with N rows and M columns and using root as parent 
    """
    def __init__(self, root, N, M):
        self.root = root 
        self.canvas = tk.Canvas(self.root, width=1000, height=850,borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="bottom", fill="both", expand="true")
        self.rows = N
        self.columns = M
        self.tiles = {}
        self.canvas.bind("<Configure>", self.redraw)
        self.status = tk.Label(self.root, anchor="w")
        self.status.pack(side="bottom", fill="x")

        # source/sink 
        self.tilesClicked = 0
        self.sourceSink = [[-1,-1]] * 2

    """
    Updates all tiles when the window is resized
    """
    def redraw(self, event=None):
        self.canvas.delete("rect")
        # print(self.root.winfo_width())
        print(f"{self.canvas.winfo_width()}\n{self.canvas.winfo_height()}")
        cellwidth = int(self.canvas.winfo_width()/self.columns)
        cellheight = int(self.canvas.winfo_height()/self.rows)
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column*cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                tile = self.canvas.create_rectangle(x1,y1,x2,y2, fill="sky blue", tags="rect")
                self.tiles[row,column] = tile
                self.canvas.tag_bind(tile, "<1>", lambda event, row=row, column=column: self.clicked(row, column))

    """
    Changes color of specific set of tiles to a new color 
    """
    def update_color(self, tiles, new_color):
        for tile in tiles:
            print(tile)
            self.canvas.itemconfigure(self.tiles[tile[0], tile[1]], fill=new_color)
            self.delay()


    """
    Handles click event on tiles for bfs
    """
    def clicked(self, row, column):
        tile = self.tiles[row,column]
        tile_color = self.canvas.itemcget(tile, "fill")
        new_color = tile_color 
        if tile_color == "sky blue":
            if self.tilesClicked < 2:
                new_color = "steel blue"
                self.sourceSink[self.tilesClicked] = [row, column]
                self.tilesClicked += 1
        else:
            new_color = "sky blue"
            self.tilesClicked -= 1
        self.canvas.itemconfigure(tile, fill=new_color)
        self.status.configure(text="you clicked on %s/%s" % (row, column))

    """
    Waits after execution for visual update
    """
    def delay(self, sec=0.1):
        self.root.update()
        sleep(sec)

    """
    Resets the tiles from bfs/others
    """
    def reset(self):
        self.redraw()
        self.tilesClicked = 0
        self.sourceSink = [[-1,-1]] * 2
        