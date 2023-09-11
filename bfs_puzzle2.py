import copy

"""
Components:
1. bfs_shortest_path(graph_as_known, start/current_board, goal)
2. get_child_board_list(board)
3. bfs2(start_board, goal_board) - calls BFS
    - house start board and goal board from main
    - this should house open and explored boards
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

def get_child_boards_list(board):
    """
    This function gets ALL child boards (i.e. the graph)
    since it seems we will need to feed all possible solutions to
    the previously established bfs_shortest_paths algo
    :param board: A starting board (RxC) matrix
    :return: A list of ALL possible child and subchild boards
    """

    list_of_child_boards = {}

    # determine board size
    total_board_rows = 0
    total_board_cols = 0
    for rows in board:
        total_board_rows += 1
        col_count = 0
        for columns in board:
            col_count += 1
            if (col_count > total_board_cols):
                total_board_cols = col_count

    print (f'board size {total_board_rows} x {total_board_cols}')
    zero_position = [-1, -1]
    row_pos = -1  # to determine which

    for rows in board:
        row_pos += 1
        col_pos = -1
        for columns in rows:
            col_pos += 1
            if columns == 0:
                zero_position = [row_pos, col_pos]

    print(f'Zero Position is: {zero_position}')

    # RxC matrix (where R = Num Rows and C = Num Columns

    # KNOWN POTENTIAL BUGS: NOT BOUNDING FOR EDGE CASES

    # determine if we can move up (zero position (i, j) where i < R-1
    print(f'This Level Start Board: {board}')
    up_board = copy.deepcopy(board)
    print('\nBEGIN POSSIBLE MOVES: ')

    if (zero_position[0] < (total_board_rows - 1)):
        swap_piece = up_board[zero_position[0] + 1][zero_position[1]]
        print(f'Swap Up: {swap_piece}')
        # swap zero
        up_board[zero_position[0] + 1][zero_position[1]] \
            = up_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        up_board[zero_position[0]][zero_position[1]] = swap_piece
        print(f'Upboard{up_board}')

        # add up_board to the list of children
        if str(board) in list_of_child_boards.keys():
            list_of_child_boards[str(board)].append(up_board)
        else:
            list_of_child_boards[str(board)] = [up_board]

    # determine if we can move down (zero position (i, j) where i > 0
    down_board = copy.deepcopy(board)

    if (zero_position[0] > 0):
        swap_piece = down_board[zero_position[0] - 1][zero_position[1]]
        print(f'Swap Down: {swap_piece}')
        # swap zero
        down_board[zero_position[0] - 1][zero_position[1]] \
            = down_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        down_board[zero_position[0]][zero_position[1]] = swap_piece
        print(f'Downboard{down_board}')

        # add down_board to the list of children
        if str(board) in list_of_child_boards.keys():
            list_of_child_boards[str(board)].append(down_board)
        else:
            list_of_child_boards[str(board)] = [down_board]

    # determine if we can move left (zero position (i, j) where j < C-1
    left_board = copy.deepcopy(board)

    if (zero_position[1] < (total_board_cols - 1)):
        swap_piece = left_board[zero_position[0]][zero_position[1] + 1]
        print(f'Swap Left: {swap_piece}')
        # swap zero
        left_board[zero_position[0]][zero_position[1] + 1] \
            = left_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        left_board[zero_position[0]][zero_position[1]] = swap_piece
        print(f'Left_board{left_board}')

        # add left_board to the list of children
        if str(board) in list_of_child_boards.keys():
            list_of_child_boards[str(board)].append(left_board)
        else:
            list_of_child_boards[str(board)] = [left_board]

    # determine if we can move right (zero position (i, j) where j > 0
    right_board = copy.deepcopy(board)

    if (zero_position[1] > 0):
        swap_piece = right_board[zero_position[0]][zero_position[1] - 1]
        print(f'Swap Right: {swap_piece}')
        # swap zero
        right_board[zero_position[0]][zero_position[1] - 1] \
            = right_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        right_board[zero_position[0]][zero_position[1]] = swap_piece
        print(f'Right_board{right_board}')

        # add right_board to the list of children
        if str(board) in list_of_child_boards.keys():
            list_of_child_boards[str(board)].append(right_board)
        else:
            list_of_child_boards[str(board)] = [right_board]

    return list_of_child_boards




def bfs_shortest_paths(graph, start, goal):
    global bfs_nodes_visited  # to track number nodes visited

    queue = [[start]]
    bfs_nodes_visited = 0

   # NEED TO FIGURE OUT HOW TO COMPARE KEYS IN DICT to pull out next
    # board

    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        bfs_nodes_visited += 1
        next_board_list = [x for x in graph[str(vertex)]
                           if x not in set(str(path))]
        for next in next_board_list:
            if next == goal:
                return [path + [next]]
            else:
                queue.append(path + [next])

    return None  # No shortest path was found

def bfs2(start_board, goal_board):
    pass

def main():
    start_state = [[4, 1, 3], [2, 0, 6], [7, 5, 8]]
    goal_state = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]  # my assumed goal
    f1 = [[4, 0, 3], [2, 1, 6], [7, 5, 8]]
    shortest_path = bfs2(start_state, goal_state)

    if (shortest_path != None):
        print(f'Shortest Path: {shortest_path}')
    else:
        print('Shortest path note found')


main()
