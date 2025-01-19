import pygame
import numpy as np

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Triangle Reflection with Adjustment")
clock = pygame.time.Clock()

# Исходная матрица треугольника (умножена на 100)
L = np.array([[8, 1],
              [7, 3],
              [6, 2]]) * 100

# Матрица отражения относительно линии y = x
T = np.array([[0, 1],
              [1, 0]])

# Преобразование треугольника (отражение)
L_transformed = L @ T.T

# Смещение для визуализации
offset_original = np.array([2, 10])  # Смещение для исходного треугольника
offset_transformed = np.array([2, 5])  # Смещение для отражённого треугольника

L += offset_original
L_transformed += offset_transformed

# Функция для рисования треугольника
def draw_triangle(screen, points, color, label_prefix):
    # Рисуем стороны треугольника
    pygame.draw.polygon(screen, color, points, 2)
    for i, point in enumerate(points):
        pygame.draw.circle(screen, color, point.astype(int), 5)  # Вершины
        # Подпись вершин
        font = pygame.font.SysFont(None, 20)
        label = font.render(f"{label_prefix}{i+1}", True, color)
        screen.blit(label, point.astype(int) + np.array([10, -10]))

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Оси координат
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 800), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (800, 400), 1)

    # Линия y = x
    pygame.draw.line(screen, (0, 255, 0), (0, 800), (800, 0), 1)

    # Рисуем исходный треугольник (красный)
    draw_triangle(screen, L, (255, 0, 0), "O")

    # Рисуем преобразованный треугольник (синий)
    draw_triangle(screen, L_transformed, (0, 0, 255), "T")

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
