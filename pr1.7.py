import pygame
import numpy as np


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Triangle Rotation")
clock = pygame.time.Clock()


L = np.array([[3, -1],
              [4, 1],
              [2, 1]]) * 100


T = np.array([[0, 1],
              [-1, 0]])

L_transformed = L @ T.T


offset = np.array([300, 500])  
L += offset
L_transformed += offset


def draw_triangle(screen, points, color, label_prefix):
    
    pygame.draw.polygon(screen, color, points, 2)
    for i, point in enumerate(points):
        pygame.draw.circle(screen, color, point.astype(int), 5)  
        
        font = pygame.font.SysFont(None, 20)
        label = font.render(f"{label_prefix}{i+1}", True, color)
        screen.blit(label, point.astype(int) + np.array([10, -10]))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

   
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 800), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (800, 400), 1)

    
    draw_triangle(screen, L, (255, 0, 0), "O")

    
    draw_triangle(screen, L_transformed, (0, 0, 255), "T")

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
