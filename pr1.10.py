import pygame
import math

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("\u0423\u043b\u0438\u0442\u043a\u0430 \u041f\u0430\u0441\u043a\u0430\u043b\u044f")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Параметры улитки
a = 100  # масштаб увеличен
b = 150  # смещение увеличено

# Центр окна
cx, cy = WIDTH // 2, HEIGHT // 2

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отображение на экране
    screen.fill(WHITE)

    theta = 0
    max_theta = 20 * math.pi  # Общий угол для спирали (20 оборотов)
    step = 0.01  # Шаг угла

    points = []

    while theta <= max_theta:
        r = b + 2 * a * math.cos(theta)
        x = cx + r * math.cos(theta)
        y = cy + r * math.sin(theta)
        points.append((x, y))
        theta += step

    # Отрисовка спирали
    if len(points) > 1:
        pygame.draw.lines(screen, BLACK, False, points, 2)

    pygame.display.flip()

pygame.quit()
