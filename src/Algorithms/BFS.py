"""
BFS.py
"""
from collections import deque
import tkinter as tk 

def find(source, destination, prev, dists, queue, grid):
     while len(queue) > 0:
            rows, columns = grid.rows, grid.columns

            v = queue.popleft()
            r, c = v[0], v[1] 
            # Get unvisited neighboring tiles 
            tiles = []
            for row, col in [[r-1, c], [r, c-1], [r, c+1], [r+1, c]]: 
                if row >=0 and col >=0 and row < rows and col < columns:
                    if dists[row][col] < 0:
                        tiles.append([row, col])
                        dists[row][col] = dists[r][c] + 1
                        prev[row][col] = v
                        if [row, col] == destination:
                            # print(f"found destinaiton {destination} with {row, col}")
                            return dists[row][col]
                        queue.append([row, col])
                # Color visited tiles 
                grid.update_color(tiles, "deep sky blue")


def run_BFS(grid):
    print("Starting BFS")

    if grid.tilesClicked < 2: 
        title = "Error"
        message = "Must specify both source and destination tiles"
        print(f"{title}\n{message}")
        # tk.messagebox.showerror(title=title, message=message)
    else:
        dists = [ [ -1 for i in range(grid.columns) ] for j in range(grid.rows) ]
        prev = [ [ -1 for i in range(grid.columns) ] for j in range(grid.rows) ]
        q = deque()

        source = grid.sourceSink[0]
        destination = grid.sourceSink[1]
        dists[source[0]][source[1]] = 0
        q.append(source)

        distance = find(source, destination, prev, dists, q, grid)
        
        # print(f"Dists:\n{dists}")
        # print(f"Source: {source}\nDestination: {destination}")

        # print(distance)

        # backtrack for path 
        w = destination
        while w != source:
            # paint bfs path 
            grid.update_color([w], "green")
            w = prev[w[0]][w[1]]




    