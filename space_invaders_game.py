import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
player_img = pygame.image.load("assets/player_img.png")
alien_img = pygame.image.load("assets/villain_img.png")
bullet_img = pygame.image.load("assets/bullet.png")

# Scale images
player_img = pygame.transform.scale(player_img, (64, 64))
alien_img = pygame.transform.scale(alien_img, (64, 64))
bullet_img = pygame.transform.scale(bullet_img, (32, 32))

# Define player, alien, and bullet
player_x = WIDTH // 2
player_y = HEIGHT - 70
player_speed = 5

alien_speed = 1
alien_direction = 1
alien_list = []

num_aliens = 5
alien_width, alien_height = 64, 64

for i in range(num_aliens):
    alien_list.append([random.randint(0, WIDTH - alien_width), random.randint(-150, -alien_height)])

bullet_speed = 5
bullet_list = []

# Font and game over text
font = pygame.font.SysFont(None, 35)
game_over_text = font.render("Game Over", True, RED)

def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_alien(x, y):
    screen.blit(alien_img, (x, y))

def draw_bullet(x, y):
    screen.blit(bullet_img, (x, y))

def collision_check(obj1_x, obj1_y, obj2_x, obj2_y, obj1_width, obj1_height, obj2_width, obj2_height):
    return (obj1_x < obj2_x + obj2_width and obj1_x + obj1_width > obj2_x and
            obj1_y < obj2_y + obj2_height and obj1_y + obj1_height > obj2_y)

def game_loop():
    global player_x, player_y, player_speed
    global alien_speed, alien_direction
    global bullet_speed
    global alien_list, bullet_list

    running = True
    game_over = False
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - 64:
            player_x += player_speed
        if keys[pygame.K_SPACE] and not game_over:
            bullet_list.append([player_x + 16, player_y])

        # Move bullets
        for bullet in bullet_list[:]:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullet_list.remove(bullet)
            for alien in alien_list[:]:
                if collision_check(bullet[0], bullet[1], alien[0], alien[1], 32, 32, alien_width, alien_height):
                    alien_list.remove(alien)
                    bullet_list.remove(bullet)
                    break

        # Move aliens
        for alien in alien_list:
            alien[0] += alien_speed * alien_direction
            if alien[0] <= 0 or alien[0] >= WIDTH - alien_width:
                alien_direction *= -1
                for a in alien_list:
                    a[1] += 10

            if collision_check(player_x, player_y, alien[0], alien[1], 64, 64, alien_width, alien_height):
                screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
                game_over = True

        # Draw player, aliens, and bullets
        draw_player(player_x, player_y)
        for alien in alien_list:
            draw_alien(alien[0], alien[1])
        for bullet in bullet_list:
            draw_bullet(bullet[0], bullet[1])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
