import copy


def get_child_boards_list(board):
    """
    This function gets ALL child boards (i.e. the graph)
    since it seems we will need to feed all possible solutions to
    the previously established bfs_shortest_paths algo
    :param board: A starting board (RxC) matrix
    :return: A list of ALL possible child and subchild boards
    """

    list_of_child_boards = []
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


    # determine if we can move up (zero position (i, j) where i < R-1
    print(f'Clean Board: {board}')
    up_board = copy.deepcopy(board)

    if (zero_position[0] < (total_board_rows - 1)):
        swap_piece = up_board[zero_position[0] + 1][zero_position[1]]
        print(swap_piece)
        # swap zero
        up_board[zero_position[0] + 1][zero_position[1]] \
            = up_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        up_board[zero_position[0]][zero_position[1]] = swap_piece
        print(f'Upboard{up_board}')

        # add up_board to the list of children
        list_of_child_boards.append(up_board)

    # determine if we can move down (zero position (i, j) where i < R+1
    print(f'Clean Board: {board}')
    down_board = copy.deepcopy(board)

    if (zero_position[0] < (total_board_rows + 1)):
        swap_piece = down_board[zero_position[0] - 1][zero_position[1]]
        print(swap_piece)
        # swap zero
        down_board[zero_position[0] - 1][zero_position[1]] \
            = down_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        down_board[zero_position[0]][zero_position[1]] = swap_piece
        print(f'Downboard{down_board}')

        # add up_board to the list of children
        list_of_child_boards.append(down_board)

    # determine if we can move left (zero position (i, j) where j < C-1
    print(f'Clean Board: {board}')
    left_board = copy.deepcopy(board)

    if (zero_position[1] < (total_board_cols - 1)):
        swap_piece = left_board[zero_position[0]][zero_position[1] + 1]
        print(swap_piece)
        # swap zero
        left_board[zero_position[0]][zero_position[1] + 1] \
            = left_board[zero_position[0]][zero_position[1]]

        # swap swap_piece
        left_board[zero_position[0]][zero_position[1]] = swap_piece
        print(f'Left_board{left_board}')

        # add up_board to the list of children
        list_of_child_boards.append(up_board)

    # determine if we can move right

    return list_of_child_boards




def bfs_shortest_paths(graph, start, goal):
    global bfs_nodes_visited  # to track number nodes visited

    queue = [[start]]
    bfs_nodes_visited = 0

    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        bfs_nodes_visited += 1
        next_node_list = [x for x in graph[vertex]
                          if x not in set(path)]
        for next in next_node_list:
            if next == goal:
                return [path + [next]]
            else:
                queue.append(path + [next])


def bfs2(start_board, goal_board):

    # Verify legal start board (square matrix)

    # get start board child boards
    get_child_boards_list(start_board)

    # check for the shortest path


def main():
    start_state = [[4, 1, 3], [2, 0, 6], [7, 5, 8]]
    all_child_boards = get_child_boards_list(start_state)

    # bfs_shortest_paths(all_child_boards)


main()
