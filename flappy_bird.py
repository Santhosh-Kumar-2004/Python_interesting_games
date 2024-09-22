import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 650
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
GRAVITY = 1
FLAP_STRENGTH = -10
PIPE_WIDTH = 70
PIPE_HEIGHT = 550
PIPE_GAP = 200
PIPE_SPEED = 5
BIRD_WIDTH = 30
BIRD_HEIGHT = 30

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Load assets
bird_image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_image.fill((255, 0, 0))  # Yellow bird

pipe_image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
pipe_image.fill((0, 255, 0))  # Green pipes

# Bird properties
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0

# Pipe properties
pipe_x = SCREEN_WIDTH
pipe_height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
pipe_y = SCREEN_HEIGHT - pipe_height

def draw_bird():
    screen.blit(bird_image, (bird_x, bird_y))

def draw_pipe():
    screen.blit(pipe_image, (pipe_x, pipe_y - PIPE_HEIGHT))  # Top pipe
    screen.blit(pipe_image, (pipe_x, pipe_y + PIPE_GAP))  # Bottom pipe

def update_pipe():
    global pipe_x, pipe_y, pipe_height
    pipe_x -= PIPE_SPEED
    if pipe_x < -PIPE_WIDTH:
        pipe_x = SCREEN_WIDTH
        pipe_height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        pipe_y = SCREEN_HEIGHT - pipe_height

def check_collision():
    if bird_y < 0 or bird_y + BIRD_HEIGHT > SCREEN_HEIGHT:
        return True
    if pipe_x < bird_x + BIRD_WIDTH and pipe_x + PIPE_WIDTH > bird_x:
        if bird_y < pipe_y or bird_y + BIRD_HEIGHT > pipe_y + PIPE_GAP:
            return True
    return False

def game_loop():
    global bird_y, bird_velocity
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = FLAP_STRENGTH

        # Update bird
        bird_velocity += GRAVITY
        bird_y += bird_velocity

        # Update pipe
        update_pipe()

        # Check collision
        if check_collision():
            print("Game Over!")
            running = False

        # Draw everything
        screen.fill(WHITE)
        draw_bird()
        draw_pipe()
        pygame.display.flip()

        # Frame rate
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
