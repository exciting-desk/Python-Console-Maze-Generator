# Python-Console-Maze-Generator
Python coded maze generator using depth-first search algorithm and displaying the maze on the console.

This script is a program for generating a maze using a either a randomized depth-first search algorithm or Kruskal's algorithm. 


## DEPTH-FIRST SEARCH :

The DFS program has several functions that move the player around the grid, check the available directions the player can move in, set walls around the player's current position, and generate the final maze. The program makes use of global variables to track the player's position, the coordinates of the grid, the walls of the maze, and the paths visited.

The program uses the 'move()' function to move the player around the grid, 
the 'find_n()' function to find the available directions the player can move in and the 'normal_b()' function that moves the player to the next position.

The 'set_walls()' function is used to set walls around the player's current position, depending on the specified direction the player is going to move to next. 

The 'generate_maze()' function is the main function that generates the maze by repeatedly calling the above functions in a loop until all positions on the grid have been visited.


## KRUSKAL :

Kruskal's maze generation algorithm is a randomized algorithm used to generate mazes. The algorithm starts by initializing a grid of cells with walls between them, and then repeatedly selects a random wall from the grid, and removes it if the cells on either side are not connected to each other.

The 'main_algo()' function is the main function that generates the maze by repeatedly calling other functions in a loop until all cells on the grid have been joined. The 'join_cells()' function is used to join two cells together and removes the walls, the 'find_neighbours()' function to find the available cells that can be joined.

The 'draw_maze()' function is used to visualize the final maze by plotting the cells and the walls between them.
