import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Draw the graph
nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1000)
plt.show()