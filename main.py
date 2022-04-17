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


def change_item(buttons):
    if buttons["next_face"].in_button(event.pos[0], event.pos[1]):
        amit.next_face()
    if buttons["pre_face"].in_button(event.pos[0], event.pos[1]):
        amit.pre_face()
    if buttons["next_body"].in_button(event.pos[0], event.pos[1]):
        amit.next_body()
    if buttons["pre_body"].in_button(event.pos[0], event.pos[1]):
        amit.pre_body()
    if buttons["next_legs"].in_button(event.pos[0], event.pos[1]):
        amit.next_legs()
    if buttons["pre_legs"].in_button(event.pos[0], event.pos[1]):
        amit.pre_legs()


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


def hover(some_screen):
    global screen_num
    if event.type == pygame.MOUSEMOTION:
        # For hover
        flag = False
        for button in some_screen.buttons:
            btn = some_screen.buttons[button]
            if btn.in_button(event.pos[0], event.pos[1]):
                flag = True
            btn.display(btn.in_button(event.pos[0], event.pos[1]))
        if not flag and screen_num == 1:
            f = open("info.txt")
            levels = f.readlines(0)
            f.close()
            levels = str(levels).replace("[", "").replace("]", "").replace("'", "").split(" ")
            bigest = 0
            for num in levels:
                num = int(num)
                if num > bigest:
                    bigest = num
            some_screen.characters[0].display_on_button(bigest)


amit = Character(185, 150, [], screen)
yakir = Princess(185, 150, [], screen)
first_screen = first_screen(yakir, screen)
choose_level_screen = second_screen_setup(amit, screen)
first_level = first_level(amit, yakir, screen)


screen_num = 0
running = True
while running:
    if screen_num == 0:  # first screen
        # Arrange the items on the screen
        first_screen.display(screen_num)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONUP and \
                    first_screen.buttons["exit_button"].in_button(event.pos[0], event.pos[1]):
                running = False
            # Real game loop
            hover(first_screen)
            if event.type == pygame.MOUSEBUTTONUP:
                if first_screen.buttons["start_button"].in_button(event.pos[0], event.pos[1]):
                    screen_num = 1
                change_item(first_screen.buttons)

            pygame.display.flip()
    if screen_num == 1:  # choose level screen
        choose_level_screen.display(screen_num)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # or event.type == pygame.MOUSEBUTTONUP and \
                #        exit_button.in_button(event.pos[0], event.pos[1]):
                running = False
            hover(choose_level_screen)
            if event.type == pygame.MOUSEBUTTONUP:
                if choose_level_screen.buttons["exit_button"].in_button(event.pos[0], event.pos[1]):
                    screen_num = 0
                if choose_level_screen.buttons["first_level"].in_button(event.pos[0], event.pos[1]):
                    screen_num = 2
                    amit.x, amit.y = CHARACTER_FIRST_LEVEL_X, CHARACTER_FIRST_LEVEL_Y
                    yakir.x, yakir.y = PRINCESS_FIRST_LEVEL_X, PRINCESS_FIRST_LEVEL_Y
            pygame.display.flip()
    if screen_num == 2:
        first_level.display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            hover(first_level)
            if event.type == pygame.MOUSEBUTTONUP:
                if first_level.buttons["exit_button"].in_button(event.pos[0], event.pos[1]):
                    screen_num = 1
        move(first_level.characters[0])
        first_level.characters[1].gravity()
        if first_level.characters[1].collide_with_character(first_level.characters[0]):
            f = open("info.txt", "a")
            f.write(" 2")
            f.close()
            choose_level_screen.buttons["second_level"].mood = True
            screen_num = 1
        pygame.display.flip()





