import pygame


class Platform:

    def __init__(self, x, y, width, height, picture, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.picture = picture
        self.screen = screen
        self.obstacle = False

    def display(self):
        img = pygame.image.load(self.picture)
        img = pygame.transform.scale(img, (self.width, self.height))
        self.screen.blit(img, (self.x, self.y))
