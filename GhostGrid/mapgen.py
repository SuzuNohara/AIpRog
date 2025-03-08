import random
import os
import json
from util.node import Node
from config import Config

class MapGen:
    def __init__(self):
        self.layers = Config.WORLD_LAYERS
        self.npl = Config.NODES_PER_LAYER
        self.max_connections = Config.MAX_CONNECTIONS
        self.grid = self.generate_grid()

    def generate_grid(self):
        grid = []
        for layer in range(self.layers):
            for node in range(self.npl):
                grid.append(Node(layer, node, [], 30 + layer * 100, 30 + node * 30))
        return grid

    def generate_connections_for_grid(self):
        for node in self.grid:
            possible_connections = [n for n in self.grid if n != node and len(n.connections) < self.max_connections]
            num_connections = min(random.randint(1, self.max_connections), len(possible_connections))
            connections = random.sample(possible_connections, k=num_connections)
            for connection in connections:
                if len(node.connections) < self.max_connections and connection.node_id not in node.connections:
                    node.connections.append(connection.node_id)
                if len(connection.connections) < self.max_connections and node.node_id not in connection.connections:
                    connection.connections.append(node.node_id)
        return self.grid

    def save_to_file(self):
        if not os.path.exists('maps'):
            os.makedirs('maps')
        map_number = 1
        while os.path.exists(f'maps/map{map_number:03d}.map'):
            map_number += 1
        filename = f'maps/map{map_number:03d}.map'

        map_data = []
        for node in self.grid:
            node_data = {
                'node_id': node.node_id,
                'layer': node.layer,
                'loot': node.loot,
                'x': node.x,
                'y': node.y,
                'connections': node.connections
            }
            map_data.append(node_data)

        with open(filename, 'w') as file:
            json.dump(map_data, file, indent=4)

    def kruskal_verify(self):
        parent = {}
        rank = {}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        # Initialize union-find structure
        for node in self.grid:
            parent[node.node_id] = node.node_id
            rank[node.node_id] = 0

        # Perform union operations for all connections
        for node in self.grid:
            for connection in node.connections:
                union(node.node_id, connection)

        # Check if all nodes are connected
        root = find(self.grid[0].node_id)
        for node in self.grid:
            if find(node.node_id) != root:
                return False
        return True

# Example usage
if __name__ == "__main__":
    map_gen = MapGen()
    map_gen.generate_connections_for_grid()
    if map_gen.kruskal_verify():
        print("All nodes are connected!")
    else:
        print("Not all nodes are connected!")
    map_gen.save_to_file()