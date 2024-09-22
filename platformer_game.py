import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enhanced Platformer Game")

# Load images
player_img = pygame.image.load("assets/player_img.png")
player_img = pygame.transform.scale(player_img, (50, 50))
enemy_img = pygame.image.load("assets/villain_img.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
collectible_img = pygame.image.load("assets/bullet.png")
collectible_img = pygame.transform.scale(collectible_img, (30, 30))
background_img = pygame.image.load("assets/backround.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player settings
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2, HEIGHT - player_height
player_speed = 5
gravity = 0.5
jump_power = -13
player_velocity_y = 0
on_ground = False

# Platform settings
platforms = [
    pygame.Rect(100, HEIGHT - 50, 200, 10),
    pygame.Rect(400, HEIGHT - 150, 200, 10),
    pygame.Rect(200, HEIGHT - 300, 200, 10),

    pygame.Rect(100, HEIGHT - 380, 200, 10),
    pygame.Rect(480, HEIGHT - 450, 200, 10),
    pygame.Rect(200, HEIGHT - 600, 200, 10),
]

# Enemy settings
enemies = [
    pygame.Rect(300, HEIGHT - 200, 35, 35),
    pygame.Rect(385, HEIGHT - 450, 35, 35),
    pygame.Rect(680, HEIGHT - 320, 35, 35)
]

# Collectibles settings
collectibles = [
    pygame.Rect(150, HEIGHT - 500, 30, 30),
    pygame.Rect(150, HEIGHT - 250, 30, 30),
    pygame.Rect(500, HEIGHT - 350, 30, 30)
]

score = 0
font = pygame.font.SysFont(None, 36)

def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(screen, GRAY, platform)

def draw_enemies():
    for enemy in enemies:
        screen.blit(enemy_img, (enemy.x, enemy.y))

def draw_collectibles():
    for collectible in collectibles:
        screen.blit(collectible_img, (collectible.x, collectible.y))

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_loop():
    global player_x, player_y, player_velocity_y, on_ground, score
    global collectibles, enemies

    running = True
    while running:
        screen.blit(background_img, (0, 0))  # Draw background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_SPACE] and on_ground:
            player_velocity_y = jump_power
            on_ground = False

        # Apply gravity
        player_velocity_y += gravity
        player_y += player_velocity_y

        # Check for collisions with platforms
        on_ground = False
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        for platform in platforms:
            if player_rect.colliderect(platform):
                if player_velocity_y > 0:
                    player_y = platform.top - player_height
                    player_velocity_y = 0
                    on_ground = True
                elif player_velocity_y < 0:
                    player_y = platform.bottom
                    player_velocity_y = 0

        # Check for collisions with enemies
        for enemy in enemies[:]:
            if player_rect.colliderect(enemy):
                print("Game Over!")
                pygame.quit()
                sys.exit()

        # Check for collisions with collectibles
        for collectible in collectibles[:]:
            if player_rect.colliderect(collectible):
                collectibles.remove(collectible)
                score += 1

        # Keep player within screen bounds
        if player_x < 0:
            player_x = 0
        if player_x > WIDTH - player_width:
            player_x = WIDTH - player_width
        if player_y > HEIGHT - player_height:
            player_y = HEIGHT - player_height
            on_ground = True

        draw_platforms()
        draw_enemies()
        draw_collectibles()
        draw_player(player_x, player_y)
        draw_score()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
