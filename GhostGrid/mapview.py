import os
import json
import networkx as nx
import matplotlib.pyplot as plt

def load_map(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def create_graph_from_map(map_data):
    G = nx.Graph()
    for node in map_data:
        node_id = node['node_id']
        for connection in node['connections']:
            G.add_edge(node_id, connection)
    return G

def main():
    map_files = [f for f in os.listdir('./maps') if f.endswith('.map')]
    if not map_files:
        print("No map files found in './maps'")
        return

    # Load the first map file for demonstration
    map_data = load_map(os.path.join('./maps', map_files[0]))
    G = create_graph_from_map(map_data)

    pos = nx.spring_layout(G)  # Customize layout
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="magenta", edge_color="black")
    plt.show()

if __name__ == "__main__":
    main()