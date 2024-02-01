import sys
import pygame

pygame.init()

# Get the screen resolution
infoObject = pygame.display.Info()

# Set up the screen
screen_width = infoObject.current_w
screen_height = infoObject.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Game Over")

def endscreen():
    # Load the help page image
    back_flag = False
    pygame.mixer.music.load("menuAssets/congrats.wav")
    pygame.mixer.music.set_volume(0.8)
    congrats = pygame.mixer.Sound("menuAssets/congratspeech.wav")
    congrats.play()
    pygame.mixer.music.play(-1)
    help_page_img = pygame.image.load("menuAssets/congrats.png")
    screen.blit(help_page_img, (0, 0))
    pygame.display.update()
    # Wait for the user to go back to the main menu
    while not back_flag:
        # Draw the back button
        # back_button_rect = pygame.Rect(500, 455, 300, 125)
        # back_button_rect = pygame.Rect(20, 20, 100, 50)
        # pygame.draw.rect(screen, (255, 255, 255), back_button_rect)
        # back_button_font = pygame.font.Font(None, 30)
        # back_button_text = back_button_font.render('Back', True, (0, 0, 0))
        # screen.blit(back_button_text, (30, 30))
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()