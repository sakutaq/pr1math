import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Segment Transformation")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Центр координат
CENTER_X, CENTER_Y = WIDTH // 5 + 50 , HEIGHT // 1 + 50  # Сдвигаем вправо и вверх

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

# Матрица преобразования
T = np.array([[1, 2],
              [3, 1]])

# Исходная матрица координат конца отрезка
L = np.array([[0, 100],
              [200, 300]])

# Преобразование координат
transformed_L = T @ L

# Вычисление середины исходного отрезка
original_mid = np.mean(L, axis=1)

# Вычисление середины преобразованного отрезка
transformed_mid = np.mean(transformed_L, axis=1)

# Вывод результатов
print("Исходный отрезок:\n", L)
print("Преобразованный отрезок:\n", transformed_L)
print("Середина исходного отрезка:", original_mid)
print("Середина преобразованного отрезка:", transformed_mid)

# Коэффициент масштабирования
scale = 1

# Главный цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка экрана
    screen.fill(WHITE)

    # Рисуем оси координат
    pygame.draw.line(screen, BLACK, (0, CENTER_Y), (WIDTH, CENTER_Y), 1)  # Ось X
    pygame.draw.line(screen, BLACK, (CENTER_X, 0), (CENTER_X, HEIGHT), 1)  # Ось Y

    # Рисуем исходный отрезок
    draw_line(L[0, 0] * scale, L[1, 0] * scale, L[0, 1] * scale, L[1, 1] * scale, RED)
    draw_point(L[0, 0] * scale, L[1, 0] * scale, RED, "начало")
    draw_point(L[0, 1] * scale, L[1, 1] * scale, RED, "конец")

    # Рисуем преобразованный отрезок
    draw_line(transformed_L[0, 0] * scale, transformed_L[1, 0] * scale, transformed_L[0, 1] * scale, transformed_L[1, 1] * scale, BLUE)
    draw_point(transformed_L[0, 0] * scale, transformed_L[1, 0] * scale, BLUE, "преобр.начало")
    draw_point(transformed_L[0, 1] * scale, transformed_L[1, 1] * scale, BLUE, "преобр.конец")

    # Рисуем середины
    draw_point(original_mid[0] * scale, original_mid[1] * scale, GREEN, "середина (ориг)")
    draw_point(transformed_mid[0] * scale, transformed_mid[1] * scale, GREEN, "середина (преобр)")

    # Соединяем середины дополнительным отрезком
    draw_line(original_mid[0] * scale, original_mid[1] * scale,
              transformed_mid[0] * scale, transformed_mid[1] * scale, BLACK)

    # Обновляем экран
    pygame.display.flip()

# Завершаем Pygame
pygame.quit()
