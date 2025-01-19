import pygame


pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Primitives")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    
    pygame.draw.circle(screen, RED, (300, 200), 50, 5)  

    
    pygame.draw.line(screen, GREEN, (50, 50), (550, 50), 5)  
    pygame.draw.line(screen, BLUE, (50, 50), (300, 350), 3)  

    
    font = pygame.font.SysFont("Arial", 36)
    text_surface = font.render("примитивы", True, BLACK)
    screen.blit(text_surface, (200, 300))

    
    pygame.draw.polygon(screen, YELLOW, [(100, 150), (200, 100), (300, 150), (200, 200)], 0)

    
    pygame.display.flip()


pygame.quit()
