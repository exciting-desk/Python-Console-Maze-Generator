import drawing
from random import shuffle
from time import sleep
from os import system

sets = []
coords = []
walls = []
cells = []
size = 0

def set_coords(n_size):
    """
    This function sets the coordinates of the cells in the grid.

    Args :
        n_size (int) : the size of the grid, it creates a grid of n_size*n_size

    """
    global size
    global coords
    size = n_size
    for i in range(0,size):
        for j in range(0,size):
            coords.append([i,j])
    drawing.split_coords(coords, size)


def intialize():
    """
    This function initializes the walls and sets of the grid.

    """
    global coords
    global walls

    s_coords = drawing.s_coords.copy()
    for i in s_coords:
        for j in i :
            if s_coords.index(i)%2 == 0:
                walls.append(j)
            else:
                if i.index(j)%2 == 0:
                    walls.append(j)
    
    for i in coords:
        if i not in walls:
            sets.append([i])
            cells.append(i)


def find_set_ind(cell):
    """
    This function finds the index of the set in which a given cell is present.

    Args:
        cell (list) : the cell for which the index of the set is to be found.

    Returns:
        (int) : the index of the set in which the cell is present

    """
    global sets

    for i in sets:
        if cell in i :
            return sets.index(i)


def find_n(cell):
    """
    This function finds the next cell which can be joined to the current cell.

    Args:
        cell (list) : the current cell

    Returns: 
        (list) : the next cell which can be joined to the current cell.

    """
    global cells

    tmp_reach = cell.copy()
    reach_cells = []

    tmp_reach[0]+=2
    if tmp_reach in cells:
        reach_cells.append(tmp_reach)
    tmp_reach = cell.copy()

    tmp_reach[0]-=2
    if tmp_reach in cells:
        reach_cells.append(tmp_reach)
    tmp_reach = cell.copy()

    tmp_reach[1]+=2
    if tmp_reach in cells:
        reach_cells.append(tmp_reach)
    tmp_reach = cell.copy()

    tmp_reach[1]-=2
    if tmp_reach in cells:
        reach_cells.append(tmp_reach)
    tmp_reach = cell.copy()

    if reach_cells:
        shuffle(reach_cells)
        return reach_cells[0]
    return reach_cells


def join(cell1, cell2):
    """
    This function joins two sets containing cell1 and cell2 respectively.

    Args:
        cell1 (list) : the first cell to be joined
        cell2 (list) : the second cell to be joined

    """
    global sets
    global walls
    set1 = sets[find_set_ind(cell1)]
    set2 = sets[find_set_ind(cell2)]

    set1+=set2
    sets.remove(set2)

    if cell1[1] == cell2[1]:
        if cell1[0]<cell2[0]:
            rem_wall = cell1.copy()
            rem_wall[0]+=1
            walls.remove(rem_wall)
        else:
            rem_wall = cell2.copy()
            rem_wall[0]+=1
            walls.remove(rem_wall)

    elif cell1[0] == cell2[0]:
        if cell1[1]<cell2[1]:
            rem_wall = cell1.copy()
            rem_wall[1]+=1
            walls.remove(rem_wall)
        else:
            rem_wall = cell2.copy()
            rem_wall[1]+=1
            walls.remove(rem_wall)


def main_algo(visualize, user_size):
    """
    Main algorithm for generating the maze. It is responsible for shuffling the cells, 
    checking for neighboring cells, and joining the sets containing those cells.

    Args:
        visualize (bool) : a boolean value indicating whether the maze should be visualized as it is generated
        user_size (int) : an integer value representing the size of the maze to be generated

    """
    shuffle(cells)
    while len(sets)>1:
        for i in cells:
            n_cell = find_n(i)
            if n_cell and (find_set_ind(n_cell) != find_set_ind(i)):
                join(i, n_cell)
            if visualize:
                drawing.draw(walls, user_size)
                sleep(0.5)
                system('cls')
            

    
def draw_maze(user_size, visualize):
    """
    Function that creates the maze by calling other functions in the correct order. 
    It sets the coordinates, initializes the sets, calls the main algorithm and draws the maze.

    Args:
        user_size (int) : an integer value representing the size of the maze to be generated
        visualize (bool) : a boolean value indicating whether the maze should be drawn as it is generated

    """
    set_coords(user_size)
    intialize()
    main_algo(visualize, user_size)
    drawing.draw(walls, user_size)



