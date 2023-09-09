
def get_child_boards_list(board):
    """
    This function gets ALL child boards (i.e. the graph)
    since it seems we will need to feed all possible solutions to
    the previously established bfs_shortest_paths algo
    :param board: A starting board (RxC) matrix
    :return: A list of ALL possible child and subchild boards
    """

    # determine board size
    row_count = 0
    max_col = 0
    for rows in board:
        row_count += 1
        col_count = 0
        for columns in board:
            col_count += 1
            if (col_count > max_col):
                max_col = col_count

    print (f'board size {row_count} x {max_col}')
    # find position of the zero (empty space)

    # determine if we can move up

    # determine if we can move down

    # determine if we can move left

    # determine if we can move right

    # return list_of_child_boards




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
