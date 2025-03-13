import pygame
import time
from datetime import datetime
import itertools

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Размеры окна
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock + Music Player + Moving Ball")

# --- ЧАСТЬ 1: ЧАСЫ ---
# Загрузка изображений
clock_image = pygame.image.load("mickey_clock.png")  # Фон часов
right_hand = pygame.image.load("right_hand.png")  # Минутная стрелка
left_hand = pygame.image.load("left_hand.png")  # Секундная стрелка

# Центр экрана
clock_center = (WIDTH // 2, HEIGHT // 2 - 100)

# --- ЧАСТЬ 2: МУЗЫКАЛЬНЫЙ ПЛЕЕР ---
playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_song = 0

def play_music():
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()

play_music()

# --- ЧАСТЬ 3: ДВИЖЕНИЕ МЯЧА ---
ball_radius = 25
ball_x = WIDTH // 2
ball_y = HEIGHT - 100
speed = 20  # Скорость мяча

running = True
while running:
    screen.fill((255, 255, 255))  # Очистка экрана

    # --- ЧАСЫ ---
    screen.blit(clock_image, (WIDTH//4, HEIGHT//4 - 50))  # Фон часов

    # Получаем текущее время
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    # Поворот стрелок
    min_angle = -minutes * 6
    sec_angle = -seconds * 6

    rotated_min_hand = pygame.transform.rotate(right_hand, min_angle)
    rotated_sec_hand = pygame.transform.rotate(left_hand, sec_angle)

    # Отрисовка стрелок
    screen.blit(rotated_min_hand, clock_center)
    screen.blit(rotated_sec_hand, clock_center)

    # --- МЯЧ ---
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)

    pygame.display.flip()  # Обновление экрана

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # --- Управление музыкой ---
            if event.key == pygame.K_p:  # Play
                pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.pause()
            elif event.key == pygame.K_n:  # Next
                current_song = (current_song + 1) % len(playlist)
                play_music()
            elif event.key == pygame.K_b:  # Previous
                current_song = (current_song - 1) % len(playlist)
                play_music()

    # --- Движение мяча ---
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and ball_x - speed > 0:
        ball_x -= speed
    if keys[pygame.K_RIGHT] and ball_x + speed < WIDTH:
        ball_x += speed
    if keys[pygame.K_UP] and ball_y - speed > 0:
        ball_y -= speed
    if keys[pygame.K_DOWN] and ball_y + speed < HEIGHT:
        ball_y += speed

    time.sleep(0.1)  # Немного замедляем цикл

pygame.quit()
