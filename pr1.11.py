import pygame
import numpy as np
import math


class Unit:
    """Класс для управления единицами измерения."""
    def __init__(self, pixel_per_unit: float):
        self.pixel_per_unit = pixel_per_unit

    def get_length(self, dl: float) -> int:
        """Преобразование длины в пиксели."""
        return int(self.pixel_per_unit * dl)


class Origin:
    """Класс для хранения координат начала координат."""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class ReferenceFrame:
    """Класс для системы отсчета."""
    def __init__(self, origin: Origin, unit: Unit):
        self.origin = origin
        self.unit = unit

    def get_x(self, x: float) -> int:
        """Преобразование координаты X в пиксели."""
        return self.origin.x + self.unit.get_length(x)

    def get_y(self, y: float) -> int:
        """Преобразование координаты Y в пиксели."""
        return self.origin.y - self.unit.get_length(y)  # Y инвертируется для графики


# Настройки экрана
WIDTH, HEIGHT = 800, 800
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Масштабирование и вращение квадрата")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создание системы отсчета
unit = Unit(pixel_per_unit=50)  # Один юнит равен 50 пикселям
origin = Origin(WIDTH // 2, HEIGHT // 2)
rf = ReferenceFrame(origin, unit)

# Начальные координаты квадрата
square = np.array([
    [2, -2, -2, 2],  # x-координаты
    [2, 2, -2, -2]   # y-координаты
])

# Параметры преобразования
m = 0.9  # Коэффициент масштабирования
alpha = math.pi / 32  # Угол поворота

# Матрица масштабирования
scale_matrix = np.array([
    [m, 0],
    [0, m]
])

# Матрица поворота
rotation_matrix = np.array([
    [math.cos(alpha), -math.sin(alpha)],
    [math.sin(alpha), math.cos(alpha)]
])

# Комбинированная матрица преобразования
transformation_matrix = scale_matrix @ rotation_matrix

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Копия исходного квадрата
    transformed_square = square.copy()

    # Применение преобразований
    for _ in range(20):
        transformed_square = transformation_matrix @ transformed_square
        points = [(rf.get_x(x), rf.get_y(y)) for x, y in transformed_square.T]
        pygame.draw.polygon(screen, WHITE, points, 1)

    pygame.display.flip()

pygame.quit()
