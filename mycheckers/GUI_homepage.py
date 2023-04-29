import pygame
import pygame.font
from algorithm import *
# Define colors
WHITE = (234, 234, 234)
BLACK = (0, 0, 0)
BLUE = (44, 62, 80)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Checkers Home Page")

# Set the font for the text
font = pygame.font.Font(None, 50)

# Create the text objects
title_text = font.render("Checkers", True, WHITE)
play_text = font.render("Play", True, WHITE)
quit_text = font.render("Watch AI vs AI", True, WHITE)

# Get the dimensions of the text objects
title_text_rect = title_text.get_rect()
play_text_rect = play_text.get_rect()
quit_text_rect = quit_text.get_rect()

# Set the position of the text objects
title_text_rect.centerx = SCREEN_WIDTH // 2
title_text_rect.top = 50
play_text_rect.centerx = SCREEN_WIDTH // 2
play_text_rect.top = 150
quit_text_rect.centerx = SCREEN_WIDTH // 2
quit_text_rect.top = 200

# Create the background
background = pygame.Surface(screen.get_size())
background.fill(BLUE)

# Blit the text objects onto the background
background.blit(title_text, title_text_rect)
background.blit(play_text, play_text_rect)
background.blit(quit_text, quit_text_rect)

# Set the active button to None
active_button = None

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on a button
            if active_button == "play":
                human_AI()
            elif active_button == "ai":
                # Quit the game
                AI_vs_AI()

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse is over a button
    if play_text_rect.collidepoint(mouse_pos):
        active_button = "play"
        play_text = font.render("Play", True, BLUE)
    elif quit_text_rect.collidepoint(mouse_pos):
        active_button = "ai"
        quit_text = font.render("Watch AI vs AI", True, BLUE)
    else:
        active_button = None
        play_text = font.render("Play", True, WHITE)
        quit_text = font.render("Watch AI vs AI", True, WHITE)

    # Draw the background and buttons onto the screen
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, WHITE, play_text_rect, 2)
    pygame.draw.rect(screen, WHITE, quit_text_rect, 2)
    screen.blit(play_text, play_text_rect)
    screen.blit(quit_text, quit_text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
