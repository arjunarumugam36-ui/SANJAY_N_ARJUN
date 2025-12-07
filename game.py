import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dodge Game')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Player
player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 60
player_velocity = 5

# Enemies
enemy_size = 40
enemy_velocity = 3
enemies = []

# Score
score = 0
font = pygame.font.Font(None, 36)

def spawn_enemy():
    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_size)
    enemy_y = -enemy_size
    enemies.append([enemy_x, enemy_y])

def update_enemies():
    for enemy in enemies[:]:
        enemy[1] += enemy_velocity
        if enemy[1] > SCREEN_HEIGHT:
            enemies.remove(enemy)
            global score
            score += 10

def check_collision(player_rect, enemies_list):
    for enemy in enemies_list:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            return True
    return False

def draw_game():
    screen.fill(BLACK)
    
    # Draw player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))
    
    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))
    
    # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

# Game loop
spawn_timer = 0
running = True

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_velocity
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_velocity
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_velocity
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
        player_y += player_velocity
    
    # Spawn enemies
    spawn_timer += 1
    if spawn_timer > 40:
        spawn_enemy()
        spawn_timer = 0
    
    # Update enemies
    update_enemies()
    
    # Check collisions
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    if check_collision(player_rect, enemies):
        print(f'Game Over! Final Score: {score}')
        running = False
    
    # Draw
    draw_game()

pygame.quit()
sys.exit()
