import pygame
import sys
from node import Node

nodes = [Node(**data) for data in nodes_data]

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Node Diagram")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

running = True
while running:
    screen.fill(WHITE)

    # Draw connections
    for node in nodes:
        for conn in node.connections:
            if conn < len(nodes):  # Avoid out-of-range errors
                pygame.draw.line(screen, BLACK, (node.x, node.y), (nodes[conn].x, nodes[conn].y), 2)

    # Draw nodes
    for node in nodes:
        pygame.draw.circle(screen, BLUE, (node.x, node.y), 10)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
