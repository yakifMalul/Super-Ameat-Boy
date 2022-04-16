from constants import *
from classes.Platform import *
from classes.Button import *
from classes.Character import *
from classes.Level import *


def first_level(character, princess, screen):
    platform1 = Platform(0, SCREEN_HEIGHT - 300, SCREEN_WIDTH, 300, PLATFORM_PIC, screen)
    platform2 = Platform(250, SCREEN_HEIGHT - 500, 300, 50, PLATFORM_PIC, screen)
    platform3 = Platform(600, SCREEN_HEIGHT - 600, 300, 50, PLATFORM_PIC, screen)
    platform4 = Platform(SCREEN_WIDTH - 400, SCREEN_HEIGHT - 700, 500, 800, PLATFORM_PIC, screen)
    platform_list = [platform1, platform2, platform3, platform4]
    exit_button = Button(EXIT_BUTTON_X, EXIT_BUTTON_Y, EXIT_BUTTON_WIDTH, EXIT_BUTTON_HEIGHT,
                         EXIT_BUTTON_PIC, EXIT_BUTTON_HOVER, screen)
    guide = Button(100, 100, 400, 200, GUIDE_PIC, GUIDE_PIC, screen)
    button_dict = {"exit_button": exit_button, "guide": guide}
    character.x = 100
    character.y = 600
    character.list_of_platforms = platform_list
    princess.x = 1340
    princess.y = 100
    princess.list_of_platforms = platform_list
    level = Level(DAY_BACKGROUND, [character, princess], platform_list, button_dict, 15, 10, screen)
    return level
