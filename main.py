import matplotlib.pyplot as plt
import networkx as nx
import pylab
import my_networkx as my_nx

G = nx.DiGraph()

edge_list = [(0, 4, {'w': '2'}), (0, 1, {'w': '5'}), (0, 2, {'w': '3'}), (4, 1, {'w': '6'}),
             (4, 2, {'w': '10'}), (4, 3, {'w': '4'}), (2, 3, {'w': '2'}), (1, 3, {'w': '6'}),
             (1, 2, {'w': '2'}), (2, 1, {'w': '1'})]
G.add_edges_from(edge_list)

pos = nx.shell_layout(G)
fig, ax = plt.subplots()
nx.draw_networkx_nodes(G, pos, ax=ax)
nx.draw_networkx_labels(G, pos, ax=ax)
fig.savefig("1.png", bbox_inches='tight', pad_inches=0)

curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
straight_edges = list(set(G.edges()) - set(curved_edges))
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges)
arc_rad = 0.25
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges, connectionstyle=f'arc3, rad = {arc_rad}')
fig.savefig("2.png", bbox_inches='tight', pad_inches=0)
edge_weights = nx.get_edge_attributes(G, 'w')
curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
my_nx.my_draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=curved_edge_labels, rotate=False, rad=arc_rad)
nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=straight_edge_labels, rotate=False)
fig.savefig("3.png", bbox_inches='tight', pad_inches=0)
pylab.show()
