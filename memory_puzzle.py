import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 500, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Puzzle")

# Card settings
card_size = 100
card_rows, card_cols = 6, 5
card_values = list(range(15)) * 2
random.shuffle(card_values)
cards = [[card_values.pop() for _ in range(card_cols)] for _ in range(card_rows)]
revealed = [[False] * card_cols for _ in range(card_rows)]
selected = []

def draw_cards():
    for row in range(card_rows):
        for col in range(card_cols):
            rect = pygame.Rect(col * card_size, row * card_size, card_size, card_size)
            pygame.draw.rect(screen, WHITE, rect)
            if revealed[row][col]:
                pygame.draw.rect(screen, BLACK, rect.inflate(-10, -10))
                font = pygame.font.SysFont(None, 55)
                text = font.render(str(cards[row][col]), True, WHITE)
                screen.blit(text, rect.move(30, 30))
            pygame.draw.rect(screen, BLACK, rect, 2)

def check_match():
    global selected
    if len(selected) == 2:
        (row1, col1), (row2, col2) = selected
        if cards[row1][col1] != cards[row2][col2]:
            pygame.time.wait(1000)
            revealed[row1][col1] = revealed[row2][col2] = False
        selected = []

def game_loop():
    global selected
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)
        draw_cards()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = y // card_size, x // card_size
                if not revealed[row][col] and len(selected) < 2:
                    revealed[row][col] = True
                    selected.append((row, col))
                    check_match()

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
