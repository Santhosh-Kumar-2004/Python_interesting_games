import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Paddle settings
paddle_width, paddle_height = 100, 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 10
paddle_speed = 10

# Ball settings
ball_size = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x, ball_speed_y = 5, -5

# Brick settings
brick_width, brick_height = 60, 20
bricks = [(i * (brick_width + 10), j * (brick_height + 10)) for i in range(12) for j in range(6)]

def draw_paddle(x, y):
    pygame.draw.rect(screen, BLUE, [x, y, paddle_width, paddle_height])

def draw_ball(x, y):
    pygame.draw.ellipse(screen, RED, [x, y, ball_size, ball_size])

def draw_bricks():
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, [brick[0], brick[1], brick_width, brick_height])

def game_loop():
    global paddle_x, ball_x, ball_y, ball_speed_x, ball_speed_y

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
            paddle_x += paddle_speed

        # Move ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Ball collision with walls
        if ball_x <= 0 or ball_x >= WIDTH - ball_size:
            ball_speed_x = -ball_speed_x
        if ball_y <= 0:
            ball_speed_y = -ball_speed_y

        # Ball collision with paddle
        if (paddle_x < ball_x < paddle_x + paddle_width or
            paddle_x < ball_x + ball_size < paddle_x + paddle_width) and \
           (paddle_y < ball_y + ball_size < paddle_y + paddle_height):
            ball_speed_y = -ball_speed_y

        # Ball collision with bricks
        for brick in bricks[:]:
            if (brick[0] < ball_x < brick[0] + brick_width or
                brick[0] < ball_x + ball_size < brick[0] + brick_width) and \
               (brick[1] < ball_y < brick[1] + brick_height or
                brick[1] < ball_y + ball_size < brick[1] + brick_height):
                bricks.remove(brick)
                ball_speed_y = -ball_speed_y

        draw_paddle(paddle_x, paddle_y)
        draw_ball(ball_x, ball_y)
        draw_bricks()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
