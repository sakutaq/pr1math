import pygame

# Инициализация Pygame
pygame.init()

# Размер окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Преобразование отрезков")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Исходные координаты отрезков
line1_start = (50, 100)
line1_end = (250, 200)
line2_start = (50, 200)
line2_end = (250, 300)

# Преобразование точек с матрицей T
def transform_point(x, y):
    # Матрица T = [[1, 2], [3, 1]]
    new_x = 1 * x + 2 * y
    new_y = 3 * x + 1 * y
    return new_x, new_y

# Преобразованные координаты отрезков
line1_start_transformed = transform_point(*line1_start)
line1_end_transformed = transform_point(*line1_end)
line2_start_transformed = transform_point(*line2_start)
line2_end_transformed = transform_point(*line2_end)

# Наклоны
m1 = (line1_end[1] - line1_start[1]) / (line1_end[0] - line1_start[0])
m2 = (line2_end[1] - line2_start[1]) / (line2_end[0] - line2_start[0])

m1_prime = (line1_end_transformed[1] - line1_start_transformed[1]) / (line1_end_transformed[0] - line1_start_transformed[0])
m2_prime = (line2_end_transformed[1] - line2_start_transformed[1]) / (line2_end_transformed[0] - line2_start_transformed[0])

# Функция для рисования отрезков
def draw_line(start, end, color):
    pygame.draw.line(screen, color, start, end, 2)

# Основной игровой цикл
running = True
while running:
    screen.fill(WHITE)  # Очистка экрана
    
    # Отображение исходных отрезков (красным)
    draw_line(line1_start, line1_end, RED)
    draw_line(line2_start, line2_end, RED)
    
    # Отображение преобразованных отрезков (синим)
    draw_line(line1_start_transformed, line1_end_transformed, BLUE)
    draw_line(line2_start_transformed, line2_end_transformed, BLUE)
    
    # Отображение наклонов
    font = pygame.font.SysFont("Arial", 24)
    text1 = font.render(f"m1 = {m1:.2f}", True, RED)
    text2 = font.render(f"m2 = {m2:.2f}", True, RED)
    text3 = font.render(f"m1' = {m1_prime:.2f}", True, BLUE)
    text4 = font.render(f"m2' = {m2_prime:.2f}", True, BLUE)
    
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))
    screen.blit(text3, (10, 70))
    screen.blit(text4, (10, 100))
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()
