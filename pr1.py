import pygame
import numpy as np


pygame.init()


WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Transformation")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

def draw_point(x, y, color, label=""):
    """Рисует точку на экране."""
    if -CENTER_X <= x <= CENTER_X and -CENTER_Y <= y <= CENTER_Y:
        pygame.draw.circle(screen, color, (CENTER_X + int(x), CENTER_Y - int(y)), 5)
        if label:
            font = pygame.font.SysFont(None, 24)
            text = font.render(label, True, color)
            screen.blit(text, (CENTER_X + int(x) + 10, CENTER_Y - int(y) - 10))
    else:
        print(f"Point ({x}, {y}) is out of bounds.")


T = np.array([[1, 3],
              [4, 1]])


x, y = map(float, input("Введите координаты точки (x y): ").split())


original_point = np.array([x, y])
transformed_point = T @ original_point


print("Исходные координаты:", original_point)
print("Преобразованные координаты:", transformed_point)


scale = 5


scaled_original = original_point * scale
scaled_transformed = transformed_point * scale
print(f"Исходная: {scaled_original}")
print(f"Преобразованная: {scaled_transformed}")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    
    pygame.draw.line(screen, (0, 0, 0), (0, CENTER_Y), (WIDTH, CENTER_Y), 1)  # Ось X
    pygame.draw.line(screen, (0, 0, 0), (CENTER_X, 0), (CENTER_X, HEIGHT), 1)  # Ось Y

    
    draw_point(original_point[0] * scale, original_point[1] * scale, RED, "Оригинал")
    draw_point(transformed_point[0] * scale, transformed_point[1] * scale, BLUE, "Преобразованные")

    
    pygame.display.flip()


pygame.quit()
