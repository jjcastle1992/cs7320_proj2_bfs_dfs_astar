

def build_graph_as_dict (node_list, directed_graph=False):
    """
    Intakes a node list of tuples (e.g. (A, B) and creates a dictionary
    that models our graph relationship.
    :param node_list: a list of tuples
    :param directed_graph: a boolean where True is a directed graph and
    False is an uindirected graph
    :return: This function returns the graph as a dictionary of
    key-value pairs for parent-child node relationships.
    """
    graph = {}

    # iterate through the given node list
    for node_pair in node_list:
        node1, node2 = node_pair

        # check to see if the parent node exists as a key
        # if yes, simply add the child node to the parent node
        # if no, add parent node with child node relationship to graph
        if node1 in graph.keys():
            graph[node1].append(node2)
        else:
            graph[node1] = [node2]

        # if the node_list id undirected, create inverse parent - child
        # node relationships
        if not directed_graph:
            if node2 in graph.keys():
                graph[node2].append(node1)
            else:
                graph[node2] = [node1]
    print(f'Size of Graph: {len(graph.keys())}')
    return graph


def bfs_shortest_paths(graph, start, goal):
    global bfs_nodes_visited  # to track number nodes visited

    queue = [[start]]
    bfs_nodes_visited = 0

    while queue:
        path = queue.pop(0)
        vertex = path[len(path) - 1]
        bfs_nodes_visited += 1
        next_node_list = [x for x in graph[vertex]
                          if x not in set(path)]
        for next in next_node_list:
            if next == goal:
                return [path + [next]]
            else:
                queue.append(path + [next])


# main - try with larger graph and measure memory/search - complex graph
def main():
    # small graph - using integers for node labels
    node_list_1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
                   (6, 7), (7, 8), (8, 9), (9, 10)]

    # larger graph
    node_list_2 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
                   (6, 7), (7, 8), (8, 9), (9, 10), (100, 101),
                   (101, 102), (102, 103), (103, 104), (104, 105),
                   (105, 106), (106, 107), (107, 108), (108, 109),
                   (109, 110), (110, 111), (111, 112), (112, 113),
                   (113, 114), (114, 115), (115, 116), (116, 117),
                   (117, 118), (118, 119), (119, 120), (4, 100),
                   (120, 10), (200, 201), (201, 202), (202, 203),
                   (203, 204), (204, 205), (205, 206), (206, 207),
                   (207, 208), (208, 209), (209, 210), (210, 211),
                   (211, 212), (212, 213), (213, 214), (214, 215),
                   (215, 216), (216, 217), (217, 218), (218, 219),
                   (219, 220), (1, 200), (220, 10), (300, 301),
                   (301, 302), (302, 303), (303, 304), (304, 305),
                   (305, 306), (306, 307), (307, 308), (308, 309),
                   (309, 310), (310, 311), (311, 312), (312, 313),
                   (313, 314), (314, 315), (315, 316), (316, 317),
                   (317, 318), (318, 319), (319, 320), (3, 300),
                   (320, 10), (106, 200), (220, 112), (10, 666),
                   (10, 667), (10, 668), (668, 669), (666, 668)]

    # create your graph data structure from the node_list
    graph = build_graph_as_dict(node_list_2, directed_graph=False)

    # Here we are using nodes labeled with integers (0,1,2,...)
    print ("\nBreadth First Search-----------")
    start_node = 1
    goal_node = 10

    # get a list of all the paths to goal using BFS
    bfs_path_list = list(bfs_shortest_paths(graph, start_node, goal_node))

    # display # paths  and the paths
    print (f"BFS shortest path. Number paths={len(bfs_path_list)}/"
           f"\nBFS shortest path: {bfs_path_list}"
           f"\nTotal nodes visited: {bfs_nodes_visited}")


# run the main function
main()
