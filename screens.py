from constants import *
from classes.Platform import *
from classes.Button import *
from classes.Character import *
from classes.Level import *
from classes.Screen import *


def first_screen(character, screen):
    exit_button = Button(EXIT_BUTTON_FIRST_SCREEN_X, EXIT_BUTTON_FIRST_SCREEN_Y, EXIT_BUTTON_WIDTH, EXIT_BUTTON_HEIGHT,
                         EXIT_BUTTON_PIC, EXIT_BUTTON_HOVER, screen)
    start_button = Button(START_BUTTON_X, START_BUTTON_Y, START_BUTTON_WIDTH, START_BUTTON_HEIGHT,
                          START_BUTTON_PIC, START_BUTTON_HOVER, screen)
    next_face = Button(NEXT_BUTTON_X, FACE_BUTTON_Y, NEXT_BUTTON_WIDTH, NEXT_BUTTON_HEIGHT,
                       NEXT_ITEM_PIC, NEXT_ITEM_HOVER, screen)
    pre_face = Button(PRE_BUTTON_X, FACE_BUTTON_Y, PRE_BUTTON_WIDTH, PRE_BUTTON_HEIGHT,
                      PRE_ITEM_PIC, PRE_ITEM_HOVER, screen)

    next_body = Button(NEXT_BUTTON_X, BODY_BUTTON_Y, NEXT_BUTTON_WIDTH, NEXT_BUTTON_HEIGHT,
                       NEXT_ITEM_PIC, NEXT_ITEM_HOVER, screen)
    pre_body = Button(PRE_BUTTON_X, BODY_BUTTON_Y, PRE_BUTTON_WIDTH, PRE_BUTTON_HEIGHT,
                      PRE_ITEM_PIC, PRE_ITEM_HOVER, screen)

    next_legs = Button(NEXT_BUTTON_X, LEGS_BUTTON_Y, NEXT_BUTTON_WIDTH, NEXT_BUTTON_HEIGHT,
                       NEXT_ITEM_PIC, NEXT_ITEM_HOVER, screen)
    pre_legs = Button(PRE_BUTTON_X, LEGS_BUTTON_Y, PRE_BUTTON_WIDTH, PRE_BUTTON_HEIGHT,
                      PRE_ITEM_PIC, PRE_ITEM_HOVER, screen)
    button_dict = {"exit_button": exit_button, "start_button": start_button, "next_face": next_face,
                   "pre_face": pre_face, "next_body": next_body, "pre_body": pre_body,
                   "next_legs": next_legs, "pre_legs": pre_legs}
    items = []
    character.x = 185
    character.y = 150
    first_screen = Screen(FIRST_BACKGROUND, [character], button_dict, items, screen)
    return first_screen


def second_screen_setup(character, screen):
    f = open("info.txt")
    levels = f.readlines(0)
    levels = str(levels).replace("[", "").replace("]", "").replace("'", "").split(" ")
    bigest = 0
    for num in levels:
        num = int(num)
        if num > bigest:
            bigest = num
    exit_button = Button(EXIT_BUTTON_X, EXIT_BUTTON_Y, EXIT_BUTTON_WIDTH, EXIT_BUTTON_HEIGHT,
                         EXIT_BUTTON_PIC, EXIT_BUTTON_HOVER, screen)
    first_level = LevelButton(FIRST_COL, FIRST_ROW, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT, 1, LEVEL_BUTTON_PIC,
                              LEVEL_BUTTON_HOVER_PIC, LEVEL_BUTTON_OFF_PIC, '1' in levels, character, screen)
    second_level = LevelButton(FIRST_COL, SECOND_ROW, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT, 2, LEVEL_BUTTON_PIC,
                               LEVEL_BUTTON_HOVER_PIC, LEVEL_BUTTON_OFF_PIC, '2' in levels, character, screen)
    third_level = LevelButton(SECOND_COL, SECOND_ROW, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT, 3, LEVEL_BUTTON_PIC,
                              LEVEL_BUTTON_HOVER_PIC, LEVEL_BUTTON_OFF_PIC, '3' in levels, character, screen)
    fourth_level = LevelButton(THIRD_COL, SECOND_ROW, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT, 4, LEVEL_BUTTON_PIC,
                               LEVEL_BUTTON_HOVER_PIC, LEVEL_BUTTON_OFF_PIC, '4' in levels, character, screen)
    fifth_level = LevelButton(THIRD_COL, FIRST_ROW, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT, 5, LEVEL_BUTTON_PIC,
                              LEVEL_BUTTON_HOVER_PIC, LEVEL_BUTTON_OFF_PIC, '5' in levels, character, screen)
    button_dict = {"exit_button": exit_button, "first_level": first_level, "second_level": second_level,
                   "third_level": third_level, "fourth_level": fourth_level, "fifth_level": fifth_level}
    items = []
    second_screen = Screen(CHOOSE_LEVELS_BACKGROUND, [character], button_dict, items, screen)
    f.close()
    return second_screen


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
