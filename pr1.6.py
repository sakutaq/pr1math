import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Intersecting Segments Transformation")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Центр координат
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

def draw_point(x, y, color, label=""):
    """Рисует точку на экране."""
    pygame.draw.circle(screen, color, (CENTER_X + int(x), CENTER_Y - int(y)), 5)
    if label:
        font = pygame.font.SysFont(None, 20)
        text = font.render(label, True, color)
        screen.blit(text, (CENTER_X + int(x) + 10, CENTER_Y - int(y) - 10))

def draw_line(x1, y1, x2, y2, color):
    """Рисует линию между двумя точками."""
    pygame.draw.line(screen, color, (CENTER_X + int(x1), CENTER_Y - int(y1)), (CENTER_X + int(x2), CENTER_Y - int(y2)), 3)

# Матрица преобразования
T = np.array([[1, 2],
              [1, -3]])

# Матрица исходных отрезков
L = np.array([[-1/2, 3/2],
              [3, -2],
              [-1, -1],
              [3, 5/3]])

# Масштабируем матрицу отрезков на 100
L_scaled = L * 100

# Преобразование координат
L_transformed = (T @ L_scaled.T).T

# Искусственное смещение преобразованных отрезков
L_transformed[:, 0] += 200  # Сдвигаем по X
L_transformed[:, 1] -= 100  # Сдвигаем по Y

# Вывод результатов
print("Исходные координаты отрезков (масштабированные):\n", L_scaled)
print("Преобразованные координаты отрезков:\n", L_transformed)

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

    # Рисуем исходные отрезки
    for i in range(0, len(L_scaled), 2):
        x1, y1 = L_scaled[i]
        x2, y2 = L_scaled[i + 1]
        draw_line(x1, y1, x2, y2, RED)

    # Рисуем преобразованные отрезки
    for i in range(0, len(L_transformed), 2):
        x1, y1 = L_transformed[i]
        x2, y2 = L_transformed[i + 1]
        draw_line(x1, y1, x2, y2, BLUE)

    # Обновляем экран
    pygame.display.flip()

# Завершаем Pygame
pygame.quit()
