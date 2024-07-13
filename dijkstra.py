import matplotlib.pyplot as plt
import networkx as nx
import pylab

g = nx.DiGraph()
toplam = 0
g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

g.add_edge(0, 4, weight=2)
g.add_edge(0, 1, weight=5)
g.add_edge(0, 2, weight=3)
g.add_edge(1, 2, weight=2)
g.add_edge(2, 1, weight=1)
g.add_edge(4, 3, weight=4)
g.add_edge(4, 2, weight=10)
g.add_edge(4, 1, weight=6)
g.add_edge(2, 3, weight=2)
g.add_edge(1, 3, weight=6)

for i in range(5):
    if g.has_edge(4, i):
        print("dijkstra path = ", nx.dijkstra_path(g, 4, i), "  uzaklık = ", nx.dijkstra_path_length(g, 4, i))
        toplam += nx.dijkstra_path_length(g, 4, i)
    else:
        print("dijkstra path = [4,", i, "]  uzaklık = yok")
print("4.node'un diğer node lara uzaklıklar toplamı = ", toplam)

g.remove_node(2)
edge_labels = dict([((u, v,), d['weight'])
                    for u, v, d in g.edges(data=True)])
pos = nx.shell_layout(g)
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
node_labels = {node: node for node in g.nodes()}
nx.draw_networkx_labels(g, pos, labels=node_labels)
nx.draw(g, pos, node_size=1500, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.05')

toplam2 = 0
print("")
print("2.node silindikten sonra dijkstra's path ve graph")
print("")
for i in range(5):
    if g.has_edge(4, i):
        print("dijkstra path = ", nx.dijkstra_path(g, 4, i), "  uzaklık = ", nx.dijkstra_path_length(g, 4, i))
        toplam2 += nx.dijkstra_path_length(g, 4, i)
    else:
        print("dijkstra path = [4,", i, "]  uzaklık = yok")
print("4.node'un diğer node lara uzaklıklar toplamı = ", toplam2)
pylab.show()
