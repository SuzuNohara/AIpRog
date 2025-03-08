from pyvis.network import Network

net = Network(notebook=True)
net.add_node(1, label="Node 1", color="red")
net.add_node(2, label="Node 2", color="blue")
net.add_edge(1, 2)

net.show("node_graph.html")