import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
G.add_edges_from(edges)

pos = nx.spring_layout(G)  # Customize layout
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightgreen", edge_color="gray")
plt.show()