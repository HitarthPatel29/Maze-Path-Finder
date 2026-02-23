"""
This contains helper functions for maintaining puzzle states
verify goal
add new possible paths
get starting point
print maze with the path

Hitarth Patel, Mohawk College, 2022
"""
import copy, random
from prim_maze_generator import generate_maze, print_maze

def is_goal(state, maze):
    """Return true if the state is the goal of the maze"""
    row, col = state
    return row == len(maze) - 1 and maze[row][col] == 'c'

def next_states( state, maze):
    """returns a list of possible state paths arround(up, down, left, right) current state """
    row, col = state
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    valid_states = []

    for drow, dcol in directions:
        new_row, new_col = row + drow, col + dcol
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            if maze[new_row][new_col] != 'w':  # Not a wall
                valid_states.append((new_row, new_col))

    return valid_states

def get_start_state(maze):
    """returns the starting state location in a maze """
    for col in range(len(maze[0])):
        if maze[0][col] == 'c':
            return (0, col)     #(row, col) format

    return None

def print_result_maze(maze, path):
    """iterates through path list and marks path on maze and then calls print_maze form prim_maze_generator """
    # Create a deep copy of the maze to avoid modifying the original
    solution_maze = copy.deepcopy(maze)
    for row, col in path:
        # Mark the solution path with '*'
        if solution_maze[row][col] != 'w':  # Avoid marking walls
            solution_maze[row][col] = '*'
    print_maze(solution_maze)