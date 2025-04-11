import pygame, sys, random
from snake_db import get_user
from save_score import save_score

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Установка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Настройка времени
clock = pygame.time.Clock()
FPS = 10

# Шрифт
font = pygame.font.SysFont("Verdana", 20)

# Игрок
username = input("Введите ваше имя: ")
user_id, (score, level) = get_user(username)

# Змейка и еда
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
        random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

# Игра
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    elif keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    elif keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    elif keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)

    # Движение змейки
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    # Проверка еды
    if head == food:
        score += 10
        if score % 50 == 0:
            level += 1
            FPS += 2
        food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
    else:
        snake.pop()

    # Проверка столкновений
    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake[1:]
    ):
        running = False

    # Отображение еды
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # Отображение змейки
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, CELL_SIZE, CELL_SIZE))

    # Отображение счёта и уровня
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(FPS)

# Сохранение результата после выхода
save_score(user_id, score, level)
pygame.quit()
sys.exit()
