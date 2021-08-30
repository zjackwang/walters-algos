"""
CPanel.py
Provides panel of control buttons used to perform 
actions such as run BFS
"""

import tkinter as tk

from Algorithms.BFS import run_BFS
from Algorithms.DFS import run_DFS

class CPanel:

    def __init__(self, root):
        self.root = root 
        self.canvas = tk.Canvas(self.root, width=500, height=200, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        
        self.bfs_button = tk.Button(self.root, text="BFS", command=lambda: run_BFS(self.root.grid))
        self.bfs_button.pack(side="top")

        self.dfs_button = tk.Button(self.root, text="DFS", command=lambda: run_DFS(self.root.grid))
        self.dfs_button.pack(side="top")

        self.reset_button = tk.Button(self.root, text="Reset", command=lambda: self.root.grid.reset())
        self.reset_button.pack(side="top")
        