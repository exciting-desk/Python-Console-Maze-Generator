f_map = ""
s_coords = []

def split_coords(coords, size):
    """
    Split the coordinates into sublists that represent the rows of the maze.

    Args:
        coords (List[List[int]]): A list of coordinates in the maze.
        size (int): The size of the maze.
    """
    global s_coords
    temp_s = []
    counter = 0
    for i in coords:
        if counter == size:
            counter = 0
            s_coords.append(temp_s.copy())
            temp_s = []
        temp_s.append(i)
        counter += 1
    s_coords.append(temp_s.copy())


def draw_coord(size):
    """
    Add the coordinates for the rows at the top of the maze.

    Args:
        size (int): The size of the maze.
    """
    global f_map
    f_map += " "
    for i in range(0,size):
        if i<10:
            f_map += "   " + str(i)
        else:
            f_map += "  " + str(i)
    f_map += "\n"


def initial_draw(walls):
    """
    Draw the initial state of the maze.

    Args:
        walls (List[List[int]]): A list of coordinates where there are walls in the maze.
    """
    global f_map
    coord_c = 0

    for i in s_coords:
        if coord_c < 10:
            f_map += str(coord_c) + " "
        else:
            f_map += str(coord_c)
        for j in i:
            if j in walls:
                f_map += "|///"
            else:
                f_map += "|___"
        coord_c += 1
        f_map += "\n"

def draw(walls, size):
    """
    Draws the final map using print()

    Args:
        walls (List[List[int]]): A list of coordinates representing the walls in the maze.
        size (int): The size of the maze.
    """
    draw_coord(size)
    initial_draw(walls)
    print(f_map)