# Name: James Castle
# CS 7320
# Description: Toy all in one Python file to solve an n-Puzzle
# Date: Sep 11, 2023

import time
import copy
from queue import PriorityQueue


def legal_board_check(board):
    """
    This function checks to ensure the starting board is legal
    :param board: a 2d list of ints that should contain unique numbers
    and 1 zero
    :return: Boolean. True if all board conditions are met
       1. (N x N board dims)
       2. List values are  ints
       3. There is exactly 1 zero
    """
    square_matrix = False
    list_ints = True
    single_zero = False
    legal_board = False

    # determine board size and check number of zeroes on board
    total_board_rows = 0
    total_board_cols = 0
    zero_count = 0

    for rows in board:
        total_board_rows += 1
        col_count = 0
        for columns in rows:
            col_count += 1
            if (type(columns) != int):
                list_ints = False
            if (columns == 0):
                zero_count += 1
            if (col_count > total_board_cols):
                total_board_cols = col_count

    print(f'board size {total_board_rows} x {total_board_cols}')
    # Square Matrix Validation
    if (total_board_cols == total_board_rows):
        square_matrix = True
    else:
        print('ERROR: Board size is not a square matrix!')

    # Single Zero validation
    if (zero_count == 1):
        single_zero = True
    else:
        print('ERROR: There is more than one zero on the board')
        print(f'Number Zeroes: {zero_count}')

    # Validate all conditions for a legal board are met
    if ((square_matrix) and (list_ints) and (single_zero)):
        legal_board = True

    return legal_board


def get_child_boards_list(board):
    """
    This function gets ALL child boards for a given parent board
    :param board: 2d list of ints - A game board (RxC) matrix
    :return: A list of ALL possible child boards of the parent
    """

    list_of_child_boards = {}

    zero_position = [-1, -1]
    row_pos = -1  # to determine which

    total_board_rows = 0
    total_board_cols = 0

    # get our board dimensions AND the zero position
    for rows in board:
        row_pos += 1
        col_pos = -1
        total_board_rows += 1
        col_count = 0
        for columns in rows:
            col_pos += 1
            col_count += 1
            if (col_count > total_board_cols):
                total_board_cols = col_count
            if columns == 0:
                zero_position = [row_pos, col_pos]

    # determine if we can move up (Zero not in bottom Row)
    up_board = copy.deepcopy(board)

    if (zero_position[0] != (total_board_rows - 1)):
        swap_piece = up_board[zero_position[0] + 1][zero_position[1]]
        # swap zero
        up_board[zero_position[0] + 1][zero_position[1]] \
            = up_board[zero_position[0]][zero_position[1]]
        # swap swap_piece
        up_board[zero_position[0]][zero_position[1]] = swap_piece

        # add up_board to the list of children
        if str(board) in list_of_child_boards.keys():
            list_of_child_boards[str(board)].append(up_board)
        else:
            list_of_child_boards[str(board)] = [up_board]

    # determine if we can move down (Zero not in top row)
    down_board = copy.deepcopy(board)

    if (zero_position[0] != 0):
        swap_piece = down_board[zero_position[0] - 1][zero_position[1]]
        # swap zero
        down_board[zero_position[0] - 1][zero_position[1]] \
            = down_board[zero_position[0]][zero_position[1]]
        # swap swap_piece
        down_board[zero_position[0]][zero_position[1]] = swap_piece

        # add down_board to the list of children
        if str(board) in list_of_child_boards.keys():
            list_of_child_boards[str(board)].append(down_board)
        else:
            list_of_child_boards[str(board)] = [down_board]

    # determine if we can move left (Zero cannot be in last column)
    left_board = copy.deepcopy(board)

    if (zero_position[1] != (total_board_cols - 1)):
        swap_piece = left_board[zero_position[0]][zero_position[1] + 1]
        # swap zero
        left_board[zero_position[0]][zero_position[1] + 1] \
            = left_board[zero_position[0]][zero_position[1]]
        # swap swap_piece
        left_board[zero_position[0]][zero_position[1]] = swap_piece

        # add left_board to the list of children
        if str(board) in list_of_child_boards.keys():
            list_of_child_boards[str(board)].append(left_board)
        else:
            list_of_child_boards[str(board)] = [left_board]

    # determine if we can move right (Zero cannot be in first column)
    right_board = copy.deepcopy(board)

    if (zero_position[1] != 0):
        swap_piece = right_board[zero_position[0]][zero_position[1] - 1]
        # swap zero
        right_board[zero_position[0]][zero_position[1] - 1] \
            = right_board[zero_position[0]][zero_position[1]]
        # swap swap_piece
        right_board[zero_position[0]][zero_position[1]] = swap_piece
        # add right_board to the list of children
        if str(board) in list_of_child_boards.keys():
            list_of_child_boards[str(board)].append(right_board)
        else:
            list_of_child_boards[str(board)] = [right_board]

    return list_of_child_boards


def bfs_shortest_paths(start_board, goal_board):
    """
    This function searches for the shortest path to a game state board
    if one exists.
    :param start_board: 2d list of ints containing starting game board
    :param goal_board: 2d list of ints containing goal state game board
    :return: 2d list of ints containing the shortest path if one
    exists. If there is no path to the goal state, None is returned.
    Also returns an int count of the number of nodes visited.
    """
    global bfs_nodes_visited  # to track number nodes visited
    bfs_nodes_visited = 0

    # Verify legality of start board
    legal_board = legal_board_check(start_board)

    # check for legal board before kicking off
    if (legal_board):
        queue = [[start_board]]

        # run BFS (Brute force)
        while queue:
            path = queue.pop(0)
            bfs_nodes_visited += 1
            vertex = path[len(path) - 1]

            # if verbose, print each current node visited
            if(verbose):
                print(f'**Current Board #{bfs_nodes_visited}**')
                matrix_printer([vertex])
            child_boards = get_child_boards_list(vertex)
            next_node_list = [x for x in child_boards[str(vertex)]
                              if str(x) not in set(str(path))]
            for next in next_node_list:

                # Check for victory conditions, and add to our path
                if next == goal_board:
                    return [path + [next]]
                else:
                    queue.append(path + [next])

    return None  # if no path is found


def bfs2_euclidean(start_board, goal_board):
    """
    This function searches for the shortest path to a game state board
    if one exists using Euclidean distance heuristics
    :param start_board: 2d list of ints containing starting game board
    :param goal_board: 2d list of ints containing goal state game board
    :return: 2d list of ints containing the shortest path if one
    exists. If there is no path to the goal state, None is returned.
    Also returns an int count of the number of nodes visited.
    """
    global bfs_nodes_visited  # to track number nodes visited
    bfs_nodes_visited = 0
    next_node_list_euclid = PriorityQueue()
    # Verify legality of start board
    legal_board = legal_board_check(start_board)

    # Check for legal board before kicking off
    if (legal_board):
        queue = [[start_board]]

        # Kick off BFS (Euclidean)
        while queue:
            path = queue.pop(0)
            bfs_nodes_visited += 1
            vertex = path[len(path) - 1]

            # if verbose, print each current node visited
            if(verbose):
                print(f'**Current Board #{bfs_nodes_visited}**')
                matrix_printer([vertex])
            child_boards = get_child_boards_list(vertex)
            next_node_list = [x for x in child_boards[str(vertex)]
                              if str(x) not in set(str(path))]

            # Create Euclidean Distance Priority Queue
            for node in next_node_list:
                euclidean_sum = euclidean_distance(node, goal_board)
                next_node_list_euclid.put((euclidean_sum, node))

            # Visit the Children in our Priority Queue
            while not (next_node_list_euclid.empty()):
                priority, next_node = next_node_list_euclid.get()

                # Check for victory conditions, and add to our path
                if next_node == goal_board:
                    return [path + [next_node]]
                else:
                    queue.append(path + [next_node])

    return None  # if no path is found


def bfs2_manhattan(start_board, goal_board):
    """
    This function searches for the shortest path to a game state board
    if one exists using Manhattan distance heuristics
    :param start_board: 2d list of ints containing starting game board
    :param goal_board: 2d list of ints containing goal state game board
    :return: 2d list of ints containing the shortest path if one
    exists. If there is no path to the goal state, None is returned.
    Also returns an int count of the number of nodes visited.
    """
    global bfs_nodes_visited  # to track number nodes visited
    bfs_nodes_visited = 0
    next_node_list_manhat = PriorityQueue()
    # Verify legality of start board
    legal_board = legal_board_check(start_board)

    # Check for legal board before kicking off
    if (legal_board):
        queue = [[start_board]]

        # Kick off BFS (Manhattan)
        while queue:
            path = queue.pop(0)
            bfs_nodes_visited += 1
            vertex = path[len(path) - 1]

            # if verbose, print each current node visited
            if(verbose):
                print(f'**Current Board #{bfs_nodes_visited}**')
                matrix_printer([vertex])
            child_boards = get_child_boards_list(vertex)
            next_node_list = [x for x in child_boards[str(vertex)]
                              if str(x) not in set(str(path))]

            # Create Manhattan Distance Priority Queue
            for node in next_node_list:
                manhattan_sum = manhattan_distance(node, goal_board)
                next_node_list_manhat.put((manhattan_sum, node))

            # Visit the Children in our Priority Queue
            while not (next_node_list_manhat.empty()):
                priority, next_node = next_node_list_manhat.get()

                # Check for victory conditions or append path with node
                if next_node == goal_board:
                    return [path + [next_node]]
                else:
                    queue.append(path + [next_node])

    return None  # if no path is found


def euclidean_distance(board, goal):
    """
    This function calculates the Euclidean Sum for a given board based
    on the variance in tile distance of the current board vs the goal
    board.
    :param board: 2d list of ints containing the board to give a
    Euclidean sum.
    :param goal: 2d list of ints containing goal state game board
    :return: float that is the sum of all Euclidean distances for the
    target board vs goal board
    """
    euclidean_sum = 0.0
    # customizing in-case goal board is not 1, 2, 3, 4...etc.

    # Calculate our Euclidean Sum
    for row_idx, row in enumerate(goal):
        for col_idx, element in enumerate(row):
            current_target = goal[row_idx][col_idx]
            board_coord, goal_coord = coordinate_finder(current_target,
                                                        board, goal)
            x1, y1 = board_coord
            x2, y2 = goal_coord
            euclidean_dist = (((x2 - x1) ** 2)+((y2 - y1) ** 2)) ** 0.5
            euclidean_sum += euclidean_dist

    return euclidean_sum


def manhattan_distance(board, goal):
    """
    This function calculates the Manhattan Sum for a given board based
    on the variance in tile distance of the current board vs the goal
    board.
    :param board: 2d list of ints containing the board to give a
    Manhattan sum.
    :param goal: 2d list of ints containing goal state game board
    :return: float that is the sum of all Manhattan distances for the
    target board vs goal board
    """
    manhattan_sum = 0.0
    # customizing in-case goal board is not 1, 2, 3, 4...etc.

    # Calculate our Manhattan Sum
    for row_idx, row in enumerate(goal):
        for col_idx, element in enumerate(row):
            current_target = goal[row_idx][col_idx]
            board_coord, goal_coord = coordinate_finder(current_target,
                                                        board, goal)
            x1, y1 = board_coord
            x2, y2 = goal_coord
            manhattan_dist = (abs(x1 - x2) + abs(y1 - y2))
            manhattan_sum += manhattan_dist

    return manhattan_sum


def coordinate_finder(target_val, current_board, goal_board):
    """
    Finds coordinates of a target value (int) in 2 boards:
        1. Current Board
        2. Goal Board
    :param target_val: int to search for in the current and goal boards
    :param current_board: 2d list of ints containing the current board
    :param goal_board: 2d list of ints containing the goal board
    :return: tuple containing 2 ints
    """
    current_board_coords = (-1, -1)
    goal_board_coords = (-1, -1)

    # find current board coordinates for the target value
    for row_idx, row in enumerate(current_board):
        for col_idx, element in enumerate(row):
            if element == target_val:
                current_board_coords = (row_idx, col_idx)

    # find goal board coordinates for the target value
    for row_idx, row in enumerate(goal_board):
        for col_idx, element in enumerate(row):
            if element == target_val:
                goal_board_coords = (row_idx, col_idx)

    return current_board_coords, goal_board_coords


def matrix_printer(matrix, start_index=0, shortest_path=False):
    """
    :param matrix: 2d list of ints to print
    :param start_index: int index that defaults to zero for our print
    loop
    :param shortest_path: Bool indicating if the print should be
    formatted for shortest path results
    :return: void function so no return
    """
    index = 0

    # Check to see if we're printing shortest path board (for format)
    if(shortest_path):
        for boards in matrix:
            for sub_board in boards:
                col_count = 0
                if (index >= start_index):
                    for item in sub_board:
                        col_count += 1
                        print(item)
                    print((col_count // 2) * ' ' + '| |')
                    print((col_count // 2) * ' ' + ' V')
                index += 1
    else:
        for boards in matrix:
            col_count = 0
            if (index >= start_index):
                for item in boards:
                    col_count += 1
                    print(item)
                print(10 * '-')
            index += 1


def main():
    global verbose
    verbose = False  # If True, Print all Current Boards
                    # Else, only print shortest path, times, and nodes

    # 3 Puzzle Driver
    # start_state = [[3, 1], [0, 2]]
    # goal_state = [[1, 2], [3, 0]]

    # 8 Puzzle Driver
    # start_state = [[4, 1, 3], [2, 0, 6], [7, 5, 8]]
    # start_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    # goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # 15 Puzzle Driver
    start_state = [[2, 3, 7, 4],
                   [1, 6, 8, 12],
                   [5, 9, 11, 15],
                   [13, 10, 0, 14]]

    goal_state = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 0]]

    # test euclidean dist funct
    # euclidean_distance(start_state, goal_state)

    # Measure performance in seconds
    tic = time.perf_counter()
    shortest_path = bfs_shortest_paths(start_state, goal_state)
    toc = time.perf_counter()
    print('------------BRUTE FORCE BFS------------')
    print(f'Total Nodes Explored: {bfs_nodes_visited}')
    print(f'Time to completion: {toc - tic:0.04f} seconds')
    if (shortest_path != None):
        print(f'Shortest Path')
        matrix_printer(shortest_path, 0, True)
    else:
        print('Shortest path not found')

    # Test BFS with Euclidean Distance Heuristic
    tic = time.perf_counter()
    shortest_path_euclidean = bfs2_euclidean(start_state, goal_state)
    toc = time.perf_counter()
    print('------------Euclidean BFS------------')
    print(f'Total Nodes Explored: {bfs_nodes_visited}')
    print(f'Time to completion: {toc - tic:0.04f} seconds')
    if (shortest_path_euclidean != None):
        print(f'Shortest Path')
        matrix_printer(shortest_path_euclidean, 0, True)
    else:
        print('Shortest path not found')


    # Test BFS with Manhattan Distance Heuristic
    tic = time.perf_counter()
    shortest_path_manhattan = bfs2_manhattan(start_state,
                                             goal_state)
    toc = time.perf_counter()
    print('------------Manhattan BFS------------')
    print(f'Total Nodes Explored: {bfs_nodes_visited}')
    print(f'Time to completion: {toc - tic:0.04f} seconds')
    if (shortest_path_manhattan != None):
        print(f'Shortest Path')
        matrix_printer(shortest_path_manhattan, 0, True)
    else:
        print('Shortest path not found')


main()
