import pygame
from constants import *


class Level:
    def __init__(self, background_image, characters, platforms, buttons, time_star1, time_star2, screen):
        self.background_image = pygame.transform.scale(pygame.image.load(background_image),
                                                       (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.characters = characters
        self.platforms = platforms
        self.buttons = buttons
        self.time_star1 = time_star1
        self.time_start2 = time_star2
        self.screen = screen

    def display(self):
        self.screen.blit(self.background_image, (0, 0))
        for character in self.characters:
            character.display()
        for button in self.buttons:
            self.buttons[button].display(False)
        for platform in self.platforms:
            platform.display()
