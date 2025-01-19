import pygame
import numpy as np


pygame.init()


WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Segment Transformation")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

def draw_point(x, y, color, label=""):
    """Рисует точку на экране."""
    pygame.draw.circle(screen, color, (CENTER_X + int(x), CENTER_Y - int(y)), 5)
    if label:
        font = pygame.font.SysFont(None, 24)
        text = font.render(label, True, color)
        screen.blit(text, (CENTER_X + int(x) + 10, CENTER_Y - int(y) - 10))

def draw_line(x1, y1, x2, y2, color):
    """Рисует линию между двумя точками."""
    pygame.draw.line(screen, color, (CENTER_X + int(x1), CENTER_Y - int(y1)), (CENTER_X + int(x2), CENTER_Y - int(y2)), 3)


T = np.array([[1, 3],
              [4, 1]])


x1, y1 = map(float, input("Введите координаты первой точки (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты второй точки (x2 y2): ").split())

segment = np.array([[x1, x2],
                    [y1, y2]])

transformed_segment = T @ segment


print("Исходные координаты отрезка:\n", segment)
print("Преобразованные координаты отрезка:\n", transformed_segment)


scale = 5


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    
    pygame.draw.line(screen, (0, 0, 0), (0, CENTER_Y), (WIDTH, CENTER_Y), 1)  # Ось X
    pygame.draw.line(screen, (0, 0, 0), (CENTER_X, 0), (CENTER_X, HEIGHT), 1)  # Ось Y

    
    draw_line(segment[0, 0] * scale, segment[1, 0] * scale,
              segment[0, 1] * scale, segment[1, 1] * scale, RED)
    draw_point(segment[0, 0] * scale, segment[1, 0] * scale, RED, "оригинал P1")
    draw_point(segment[0, 1] * scale, segment[1, 1] * scale, RED, "оригинал P2")

    
    draw_line(transformed_segment[0, 0] * scale, transformed_segment[1, 0] * scale,
              transformed_segment[0, 1] * scale, transformed_segment[1, 1] * scale, BLUE)
    draw_point(transformed_segment[0, 0] * scale, transformed_segment[1, 0] * scale, BLUE, "преобразованные P1")
    draw_point(transformed_segment[0, 1] * scale, transformed_segment[1, 1] * scale, BLUE, "преобразованные P2")

    
    pygame.display.flip()


pygame.quit()
