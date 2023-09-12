# Name: James Castle
# CS 7320
# Description: Toy all in one Python file to solve an n-Puzzle
# Date: Sep 11, 2023

import copy

"""
Components:
1. bfs_shortest_path(start/current_board, goal)
2. get_child_board_list(board)
    Sequence:
        1. Set current_board = start_board
        2. (in final ver). *** WAIT for NOW***
            1. Check for legal start board - (n x n w/ int
            values [0: n-1] only.
            2. Check for legal goal board (n x n w/ int values [0:n-1]
            where each pair satisfies the equality n < n+1
        3. Append current_board to open_boards
        4. Generate first level of child nodes
            1. call get_child_boards(current_board)
            2. capture children in a variable 'child_boards'
        3. Add child_boards to open_boards list:
            1. Check that child_boards does not contain any boards
            in explored_boards list.
            2. If not in explored_boards, add child_boards to
            open_boards
        4. While open_list is not empty & shortest_path_found is None:
            1. call bfs_shortest_path(open_boards, current_board, goal)

        TERMINAL STATE:
            1. shortest_path found
            2. open_boards is empty (no legal child boards left)

"""
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

    print (f'board size {total_board_rows} x {total_board_cols}')
    # Sqauare Matrix Validation
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

    if ((square_matrix) and (list_ints) and (single_zero)):
        legal_board = True

    return legal_board



def get_child_boards_list(board):
    """
    This function gets ALL child boards for a given parent board
    :param board: 2d list of ints - A game board (RxC) matrix
    :return: A list of ALL possible child boards of the parent
    """

    list_of_child_boards = []

    zero_position = [-1, -1]
    row_pos = -1  # to determine which

    total_board_rows = 0
    total_board_cols = 0

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
    # print(f'This Level Start Board: {board}')
    up_board = copy.deepcopy(board)
    # print('\nBEGIN POSSIBLE MOVES: ')

    if (zero_position[0] != (total_board_rows - 1)):
        swap_piece = up_board[zero_position[0] + 1][zero_position[1]]
        # print(f'Swap Up: {swap_piece}')
        # swap zero
        up_board[zero_position[0] + 1][zero_position[1]] \
            = up_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        up_board[zero_position[0]][zero_position[1]] = swap_piece
        # print(f'Upboard{up_board}')

        # add up_board to the list of children
        list_of_child_boards.append(up_board)


    # determine if we can move down (Zero not in top row)
    down_board = copy.deepcopy(board)

    if (zero_position[0] != 0):
        swap_piece = down_board[zero_position[0] - 1][zero_position[1]]
        # print(f'Swap Down: {swap_piece}')
        # swap zero
        down_board[zero_position[0] - 1][zero_position[1]] \
            = down_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        down_board[zero_position[0]][zero_position[1]] = swap_piece
        # print(f'Downboard{down_board}')

        # add down_board to the list of children
        list_of_child_boards.append(down_board)

    # determine if we can move left (Zero cannot be in last column)
    left_board = copy.deepcopy(board)

    if (zero_position[1] != (total_board_cols - 1)):
        swap_piece = left_board[zero_position[0]][zero_position[1] + 1]
        # print(f'Swap Left: {swap_piece}')
        # swap zero
        left_board[zero_position[0]][zero_position[1] + 1] \
            = left_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        left_board[zero_position[0]][zero_position[1]] = swap_piece
        # print(f'Left_board{left_board}')

        # add left_board to the list of children
        list_of_child_boards.append(left_board)

    # determine if we can move right (Zero cannot be in first column)
    right_board = copy.deepcopy(board)

    if (zero_position[1] != 0):
        swap_piece = right_board[zero_position[0]][zero_position[1] - 1]
        # print(f'Swap Right: {swap_piece}')
        # swap zero
        right_board[zero_position[0]][zero_position[1] - 1] \
            = right_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        right_board[zero_position[0]][zero_position[1]] = swap_piece
        # print(f'Right_board{right_board}')

        # add right_board to the list of children
        list_of_child_boards.append(right_board)

    return list_of_child_boards


def bfs_shortest_paths(start_board, goal_board):
    """
    This function searches for the shortest path to a game state board
    if one exists.
    :param start: a 2d list of ints containing the starting game board
    :param goal: a 2d list of ints containing the goal state game board
    :return: a 2d list of ints containing the shortest path if one
    exists. If there is no path to the goal state, None is returned.
    Also returns an int count of the number of nodes visited.
    """
    bfs_nodes_visited = 0  # to track number nodes visited
    explored_boards = []  # note: should explore other ds for find speed
    open_boards = []
    shortest_path = None

    # Verify legality of start board
    legal_board = legal_board_check(start_board)

    if (legal_board):
        queue = [[start_board]]
        bfs_level = 0

        while queue:
            path = queue.pop(0)
            if (len(path) < 2):
                current_board = path[-1]
            else:
                current_board = path[1]
            bfs_nodes_visited += 1

            print(f'**Current Boards at Level: {bfs_level}**')
            for level_boards in open_boards:
                matrix_printer([level_boards])

            # generate the children of the vertex.
            if (bool(open_boards) == False):
                open_boards.append(current_board)
            explored_boards.append(current_board)

            num_unique_children = 0
            unique_children = []
            bfs_level += 1

            for nodes in open_boards:
                child_boards = get_child_boards_list(nodes)
                # check for duplicates, only add uniques to open board
                for child in child_boards:
                    if ((child not in open_boards) and
                            (child not in explored_boards)):
                        unique_children.append(child)
                        num_unique_children += 1

            for uniques in unique_children:
                open_boards.append(uniques)

            # check to see if any boards are the goal
            for board in open_boards:
                if board == goal_board:
                    return path + [board], bfs_nodes_visited
            # add path + open boards (children) to queue
            queue.append(path + unique_children)
            open_boards.pop(0)

    return shortest_path, bfs_nodes_visited  # No shortest path found


def matrix_printer(matrix, start_index=0, shortest_path=False):
    """
    BUG IN HERE RE SHORTEST PATH PRINT
    :param matrix:
    :param start_index:
    :param shortest_path:
    :return:
    """
    index = 0
    col_count = 0
    for boards in matrix:
        col_count = 0
        if (index >= start_index):
            for item in boards:
                col_count += 1
                print(item)
            if(shortest_path):
                print((col_count // 2) * ' ' + '| |')
                print((col_count // 2) * ' ' + ' V')
            else:
                print(10 * '-')
        index += 1

def main():

    # 3 Puzzle Driver
    start_state = [[0, 1], [3, 2]]
    goal_state = [[1, 2], [3, 0]]

    # 8 Puzzle Driver
    # start_state = [[4, 1, 3], [2, 0, 6], [7, 5, 8]]
    # start_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    # goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # my assumed goal

    shortest_path, bfs_nodes_visited = bfs_shortest_paths(start_state,
                                                          goal_state)
    print(f'Total Nodes Explored: {bfs_nodes_visited}')
    if (shortest_path != None):
        print(f'Shortest Path')
        matrix_printer(shortest_path, 0, True)
    else:
        print('Shortest path not found')


main()
