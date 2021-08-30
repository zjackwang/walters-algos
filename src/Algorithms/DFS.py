"""
DFS.py
Implementation of Depth-First Search
"""
from collections import deque
import tkinter as tk 

def find(source, destination, prev, visited, stack, grid):
    rows, columns = grid.rows, grid.columns
    visited[source[0]][source[1]] = 1
    while len(stack) > 0:
        v = stack.pop()
        r, c = v[0], v[1] 
        
        # Get unvisited neighboring tiles 
        tiles = []
        for row, col in [[r-1, c], [r, c-1], [r, c+1], [r+1, c]]:
            if row >=0 and col >=0 and row < rows and col < columns:
                if not visited[row][col]:
                    visited[row][col] = 1 
                    tiles.append([row, col])
                    prev[row][col] = v
                    if [row, col] == destination:
                        # print(f"found destination {destination} with {row, col}")
                        return 1
                    stack.append([row, col])
        print(tiles)
        # Color visited tiles 
        grid.update_color(tiles, "deep sky blue")
    return 0
    

def run_DFS(grid):
    print("Starting DFS")

    if grid.tilesClicked < 2: 
        title = "Error"
        message = "Must specify both source and destination tiles"
        print(f"{title}\n{message}")
        # tk.messagebox.showerror(title=title, message=message)
    else:
        visited = [ [ 0 for i in range(grid.columns) ] for j in range(grid.rows) ]
        prev = [ [ -1 for i in range(grid.columns) ] for j in range(grid.rows) ]
        s = deque()

        source = grid.sourceSink[0]
        destination = grid.sourceSink[1]
        
        s.append(source)

        haspath = find(source, destination, prev, visited, s, grid)
        
        print(f"Source: {source}\nDestination: {destination}")
        print(haspath)
        if haspath: 
            # backtrack for path 
            w = destination
            while w != source:
                # paint bfs path 
                grid.update_color([w], "green")
                w = prev[w[0]][w[1]]
