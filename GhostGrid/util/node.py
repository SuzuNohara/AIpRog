class Node:
    node_id = 0
    layer = 0
    loot = 0
    x = 0
    y = 0
    connections = []

    def __init__(self, layer, node_id, connections, x, y):
        self.node_id = node_id
        self.layer = layer
        self.connections = connections
        self.loot = 0
        self.x = x
        self.y = y
