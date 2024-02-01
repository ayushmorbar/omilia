import pygame
import sys
from language_menu import language_call
from help_menu import help_call

pygame.init()

# Get the screen resolution
infoObject = pygame.display.Info()

# Set up the screen
screen_width = infoObject.current_w
screen_height = infoObject.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Omilia")

# Load images
bg_img = pygame.image.load("menuAssets/oi.png")
start_button_img = pygame.image.load("menuAssets/start1.png")
help_button_img = pygame.image.load("menuAssets/help1.png")
pygame.mixer.music.load("menuAssets/menubg.wav")
pygame.mixer.music.play(-1)

# Create Rect objects for the buttons
start_button_rect = pygame.Rect(
    screen_width // 2 - start_button_img.get_width() // 2, 
    screen_height // 2 - start_button_img.get_height() // 2, 
    start_button_img.get_width(), 
    start_button_img.get_height()
)
help_button_rect = pygame.Rect(
    screen_width // 2 - help_button_img.get_width() // 2, 
    screen_height // 2 + help_button_img.get_height(), 
    help_button_img.get_width(), 
    help_button_img.get_height()
)

# Main loop
while True:
    # Draw the background and buttons
    screen.blit(bg_img, (0, 0))
    screen.blit(start_button_img, start_button_rect)
    screen.blit(help_button_img, help_button_rect)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse clicked on a button
            if start_button_rect.collidepoint(event.pos):
                language_call()
            elif help_button_rect.collidepoint(event.pos):
                help_call()

    # Update the screen
    pygame.display.update()
