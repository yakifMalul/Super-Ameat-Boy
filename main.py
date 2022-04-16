import pygame
from constants import *
from classes.Button import *
from classes.Character import *
from classes.Platform import *
from classes.Level import *
from screens import *

pygame.init()
pygame.display.set_caption("Super Ameat Boy")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def change_item():
    if next_face.in_button(event.pos[0], event.pos[1]):
        amit.next_face()
    if pre_face.in_button(event.pos[0], event.pos[1]):
        amit.pre_face()
    if next_body.in_button(event.pos[0], event.pos[1]):
        amit.next_body()
    if pre_body.in_button(event.pos[0], event.pos[1]):
        amit.pre_body()
    if next_legs.in_button(event.pos[0], event.pos[1]):
        amit.next_legs()
    if pre_legs.in_button(event.pos[0], event.pos[1]):
        amit.pre_legs()


def first_screen():
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
    button_list = [exit_button, start_button, next_face, pre_face, next_body, pre_body, next_legs, pre_legs]


def move(character):
    character.gravity()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        # move right
        if character.x <= SCREEN_WIDTH:
            if pressed[pygame.K_LSHIFT]:
                character.right(True)
            else:
                character.right(False)
    if pressed[pygame.K_a]:
        # move left
        if character.x >= 0:
            if pressed[pygame.K_LSHIFT]:
                character.left(True)
            else:
                character.left(False)
    if pressed[pygame.K_SPACE] or pressed[pygame.K_w]:
        if character.y >= 0:
            character.jump()
    pygame.display.flip()


amit = Character(185, 150, [], screen)
yakir = Princess(185, 150, [], screen)
first = first_level(amit, yakir, screen)


screen_num = 2
running = True
while running:
    if screen_num == 0:  # first screen
        # Arrange the items on the screen
        arrange1(FIRST_BACKGROUND, [amit], button_list, [])
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # or event.type == pygame.MOUSEBUTTONUP and \
                #        exit_button.in_button(event.pos[0], event.pos[1]):
                running = False
            # Real game loop
            if event.type == pygame.MOUSEMOTION:
                # For hover
                for button in button_list:
                    button.display(button.in_button(event.pos[0], event.pos[1]))
            if event.type == pygame.MOUSEBUTTONUP:
                if start_button.in_button(event.pos[0], event.pos[1]):
                    screen_num = 1
                change_item()
    if screen_num == 1:
        arrange1(CHOOSE_LEVELS_BACKGROUND, [], [], [])
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # or event.type == pygame.MOUSEBUTTONUP and \
                #        exit_button.in_button(event.pos[0], event.pos[1]):
                running = False
    if screen_num == 2:
        first.display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # or event.type == pygame.MOUSEBUTTONUP and \
                #        exit_button.in_button(event.pos[0], event.pos[1]):
                running = False

        move(first.characters[0])
        first.characters[1].gravity()
        if first.characters[1].collide_with_character(first.characters[0]):
            screen_num = 0
        pygame.display.flip()





