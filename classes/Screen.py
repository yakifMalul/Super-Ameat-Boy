import pygame
from constants import *


class Screen:
    def __init__(self, background_image, characters, buttons, items, screen):
        self.background_image = pygame.transform.scale(pygame.image.load(background_image),
                                                       (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.characters = characters
        self.buttons = buttons
        self.items = items
        self.screen = screen

    def display(self):
        self.screen.blit(self.background_image, (0, 0))
        for character in self.characters:
            character.display_on_first_screen()
        for button in self.buttons:
            button.display(False)
        # for item in self.items:
        #     item.
