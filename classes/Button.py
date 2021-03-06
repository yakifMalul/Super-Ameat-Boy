import pygame
from constants import *


class Button:
    def __init__(self, x, y, width, height, pic, hover, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pic = pygame.transform.scale(pygame.image.load(pic), (width, height))
        self.hover = pygame.transform.scale(pygame.image.load(hover), (width + 6, height + 6))
        self.screen = screen

    def in_button(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False

    def display(self, is_hover):
        if is_hover:
            self.screen.blit(self.hover, (self.x - 3, self.y - 3))
        else:
            self.screen.blit(self.pic, (self.x, self.y))


class LevelButton(Button):
    def __init__(self, x, y, width, height, num, pic, hover, off, mood, character, screen):
        super().__init__(x, y, width, height, pic, hover, screen)
        self.num = num
        self.off = pygame.transform.scale(pygame.image.load(off), (width, height))
        self.mood = mood
        self.character = character

    def in_button(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            if self.mood:
                return True
        return False

    def display(self, is_hover):
        if self.mood:
            if is_hover:
                self.screen.blit(self.hover, (self.x - 3, self.y - 3))
                self.character.display_on_button(self.num)
            else:
                self.screen.blit(self.pic, (self.x, self.y))
        else:
            self.screen.blit(self.off, (self.x, self.y))
