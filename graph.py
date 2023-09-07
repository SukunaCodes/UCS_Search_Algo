import networkx as nx
import matplotlib.pyplot as plt
import json


def show_weighted_graph(networkx_graph, node_size, font_size, fig_size):
    # Allocate the given figure size
    plt.figure(figsize=fig_size, dpi=80, num=None)
    plt.axis('off')
    # Compute the position of each vertex and display
    nodes_position = nx.spring_layout(networkx_graph)
    # Extract the weights corresponding to each edge in the graph
    edges_weights = nx.get_edge_attributes(networkx_graph, 'weight')
    # Draw the graph with the corresponding edge weights
    nx.draw_networkx(networkx_graph, nodes_position, node_size=node_size,
                     node_color=["orange"] * networkx_graph.number_of_nodes())
    # Draw the edge weights
    nx.draw_networkx_edges(networkx_graph, nodes_position, edgelist=list(networkx_graph.edges), width=2)
    # Add weights
    nx.draw_networkx_edge_labels(networkx_graph, nodes_position, edge_labels=edges_weights)
    # Add the labels of the nodes
    nx.draw_networkx_labels(networkx_graph, nodes_position, font_size=font_size,
                            font_family='sans-serif')
    plt.axis('off')
    plt.show()


def load_graph(filename):
    with open(filename) as locations:
        dict_locations = json.load(locations)
        return nx.Graph(dict_locations)
