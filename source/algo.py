from random import *
import drawing
import time
import os

coords = []
last_open = []
opens = []
stuck = False

def set_coords(size):
    for i in range(size):
        for j in range(size):
            coords.append([i, j])

    drawing.split_coords(coords, size)

player = [0, 0]
walls = []
visited = []
act_path = []


def move(dire):
    """
    Move the node in the specified direction.

    Args:
        dire (str): The direction to move in. Can be 'l' (left), 'r' (right), 'u' (up), or 'd' (down).

    Raises:
        AssertionError: If the node's new position is not within the grid, is a wall, or is a visited position.
    """
    if dire == 'l':
        player[1] -= 1
        assert player in coords, "OutOfMap"
        assert player not in walls, "OutOfPath"
        assert player not in visited, "InLastPath"

    elif dire == 'r':
        player[1] += 1
        assert player in coords, "OutOfMap"
        assert player not in walls, "OutOfPath"
        assert player not in visited, "InLastPath"

    elif dire == 'u':
        player[0] -= 1
        assert player in coords, "OutOfMap"
        assert player not in walls, "OutOfPath"
        assert player not in visited, "InLastPath"

    elif dire == 'd':
        player[0] += 1
        assert player in coords, "OutOfMap"
        assert player not in walls, "OutOfPath"
        assert player not in visited, "InLastPath"


def find_n():
    """
    Find the available directions (or neighbors) that the node can move in.

    Returns:
        List[str]: A list of available directions. Can be 'l' (left), 'r' (right), 'u' (up), or 'd' (down).
    """
    global player
    dire = ['l', 'r', 'u', 'd']
    available_dir = []
    old_p = player.copy()
    for i in dire:
        try:
            move(i)
        except AssertionError:
            player = old_p.copy()
        else:
            available_dir.append(i)
            player = old_p.copy()
    return available_dir


def normal_b(neigh):
    """
    Normal Behavior.

    Moves the player to the next Node when there are no obstacles on the way


    ARGS :
        neigh <list> : Available directions the direction can move towards
    """
    global visited
    ch_dir = neigh[randint(0, len(neigh) - 1)]
    set_walls(ch_dir)
    move(ch_dir)
    

def set_walls(dire):
    """
    Set walls around the player's current position depending on the specified direction it's gonna move next to.

    Args:
        dire (str): The direction to set walls in. Can be 'l' (left), 'r' (right), 'u' (up), or 'd' (down).
    """
    global walls
    global player

    vert = ['u', 'd']
    horz = ['l', 'r']

    old_p = player.copy()

    if dire == 'l' or dire == 'r':
        for i in vert:
            try:
                move(i)
            except AssertionError:
                player = old_p.copy()
            else:
                if player not in walls:
                    walls.append(player)
                player = old_p.copy()

    elif dire == 'u' or dire == 'd':
        for i in horz:
            try:
                move(i)
            except AssertionError:
                player = old_p.copy()
            else:
                if player not in walls:
                    walls.append(player)
                player = old_p.copy()

def generate_maze():
    """
    Generate a maze.

    The maze is generated using a randomized depth-first search algorithm. 
    The `stuck` variable is set to `True` when there are no more positions to move to.
    """
    global stuck
    global player
    global visited
    while not stuck:
        if player not in visited:
            visited.append(player.copy())

        av_dir = find_n()

        if av_dir:
            normal_b(av_dir)

        else:
            c = 0
            for i in reversed(visited):
                player = i.copy()
                av_dir = find_n()
                        
                if av_dir:
                    c+=1
                    break
                    
            if c == 0:
                stuck = True

def draw_maze(size):
    """
    draw a maze with the specified number of size and columns.

    Args:
        size (int): The size of the maze.
    """
    set_coords(size)
    generate_maze()
    drawing.draw(walls, size)