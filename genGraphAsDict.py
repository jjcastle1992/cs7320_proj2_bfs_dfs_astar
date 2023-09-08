# TODO: Implement code to generate Python dict from list of tuples
#  generate dict

def build_graph_as_dict(node_list, directed_graph):
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

    #iterate through the given node list
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

    return graph


