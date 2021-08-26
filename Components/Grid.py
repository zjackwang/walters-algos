"""
Grid.py 
Layout will be an N x M grid 
"""
import tkinter as tk

class Grid():

    # def __init__(self, N, M):
    #     self.N = N
    #     self.M = M
    #     self.width = 500
    #     self.height = 500
    #     self.root = tk.Tk()
    #     self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
    #     self.canvas.pack(fill=tk.BOTH)

    # def _fill_grid(self):
    #     self.canvas.create_rectangle()
    #     for row in range(self.N):
    #         for col in range(self.M):
    #             self.canvas.create_rectangle(
    #                 x = self.canvas.width/M, 
    #                 y = self.height/N)

    # def run(self):
    #     self.root.mainloop()

    def __init__(self, root, N, M):
        self.root = root 
        self.canvas = tk.Canvas(self.root, width=500, height=500, borderwidth=0, highlightthickness=0)
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

    def redraw(self, event=None):
        self.canvas.delete("rect")
        cellwidth = int(self.canvas.winfo_width()/self.columns)
        cellheight = int(self.canvas.winfo_height()/self.rows)
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column*cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                tile = self.canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="rect")
                self.tiles[row,column] = tile
                self.canvas.tag_bind(tile, "<1>", lambda event, row=row, column=column: self.clicked(row, column))

    def clicked(self, row, column):
        tile = self.tiles[row,column]
        tile_color = self.canvas.itemcget(tile, "fill")
        new_color = tile_color 
        if tile_color == "white":
            if self.tilesClicked < 2:
                new_color = "red"
                self.sourceSink[self.tilesClicked] = [row, column]
                self.tilesClicked += 1
        else:
            new_color = "white"
            self.tilesClicked -= 1
        self.canvas.itemconfigure(tile, fill=new_color)
        self.status.configure(text="you clicked on %s/%s" % (row, column))


if __name__ == "__main__":
    grid = Grid()
    grid.mainloop()