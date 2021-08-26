# Snake Game

## Requirements brainstorming

1. NxM Grid of rectangles
2. Method to change color of rectangle -> User Interface Panel
   a. For shortest path calculations
   b. For visualization of snake and food
3. Shortest path algorithms
4. Controls
5. Randomization of food
6. Game Over conditions

## Design Sketch

1. UX
   Canvas -> Control Panel
   -> Grid
   -> Color Changing Rectangles
   Alerts
2. Controls
   Start BFS/DFS
   Clear Grid
   Randomize barriers
   Start Snake
   Pause
3. Algorithms/Data Structure
   Grid Matrix
   BFS
   DFS
   Snake Calculations

### Phase 1

1. UX
   a. We can mark a source tile and a sink tile on the grid
   b. We can run BFS with a control panel button to find the distance between source and sink
   c. By running BFS, we can see the grid display the algorithm working and then finally display the distance
2. Controls
   a. Clicking a tile will mark the source and clicking another will mark the sink (only two allowed)
   b. Clicking BFS button after two tiles are marked will trigger BFS
3. Algorithms/Data Structures
   a. There will be a matrix representing the state of each tile
   b. BFS and result - Must create function to alter the state of the matrix and redraw the canvas
