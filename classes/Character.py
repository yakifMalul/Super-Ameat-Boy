import pygame
# from playsound import playsound
from constants import *


class Character:
    global AMIT_FACE_INDEX
    global AMIT_BODY_INDEX
    global AMIT_LEGS_INDEX

    def __init__(self, x, y, list_of_platforms, screen):
        self.x = x
        self.y = y
        self.list_of_platforms = list_of_platforms
        self.screen = screen
        self.grav = 0
        self.velY = 0
        self.mood = "ameat boy"

    def next_face(self):
        global AMIT_FACE_INDEX
        AMIT_FACE_INDEX = (AMIT_FACE_INDEX + 1) % NUM_OF_FACES

    def pre_face(self):
        global AMIT_FACE_INDEX
        if AMIT_FACE_INDEX == 0:
            AMIT_FACE_INDEX = NUM_OF_FACES - 1
        else:
            AMIT_FACE_INDEX -= 1

    def next_body(self):
        global AMIT_BODY_INDEX
        AMIT_BODY_INDEX = (AMIT_BODY_INDEX + 1) % NUM_OF_BODIES

    def pre_body(self):
        global AMIT_BODY_INDEX
        if AMIT_BODY_INDEX == 0:
            AMIT_BODY_INDEX = NUM_OF_BODIES - 1
        else:
            AMIT_BODY_INDEX -= 1

    def next_legs(self):
        global AMIT_LEGS_INDEX
        AMIT_LEGS_INDEX = (AMIT_LEGS_INDEX + 1) % NUM_OF_LEGS

    def pre_legs(self):
        global AMIT_LEGS_INDEX
        if AMIT_LEGS_INDEX == 0:
            AMIT_LEGS_INDEX = NUM_OF_LEGS - 1
        else:
            AMIT_LEGS_INDEX -= 1

    def display(self):
        if self.velY > 0:
            k = 0
            while "down" not in self.is_blocked() and k <= self.velY:
                k += 1
                self.y += 1
        elif self.velY < 0:
            k = 0
            while "up" not in self.is_blocked() and k >= self.velY:
                k -= 1
                self.y -= 1
        folder = self.mood
        # display face
        img = pygame.image.load(CHARACTER_FACES[AMIT_FACE_INDEX].replace("folder", folder))
        img1 = pygame.transform.scale(img, (ITEM_WIDTH, ITEM_HEIGHT))
        self.screen.blit(img1, (self.x, self.y))
        # display body
        img = pygame.image.load(CHARACTER_BODIES[AMIT_BODY_INDEX].replace("folder", folder))
        img2 = pygame.transform.scale(img, (ITEM_WIDTH, ITEM_HEIGHT))
        self.screen.blit(img2, (self.x, self.y + ITEM_HEIGHT))
        # display face
        img = pygame.image.load(CHARACTER_LEGS[AMIT_LEGS_INDEX].replace("folder", folder))
        img3 = pygame.transform.scale(img, (ITEM_WIDTH, ITEM_HEIGHT))
        self.screen.blit(img3, (self.x, self.y + 2 * ITEM_HEIGHT))
        # pygame.display.flip()

    def display_on_screen(self, screen_num):
        if screen_num == 0:
            folder = "ameat boy"
            # display face
            img = pygame.image.load(CHARACTER_FACES[AMIT_FACE_INDEX].replace("folder", folder))
            img1 = pygame.transform.scale(img, (FIRST_SCREEN_ITEM_WIDTH, FIRST_SCREEN_ITEM_HEIGHT))
            self.screen.blit(img1, (185, 150))
            # display body
            img = pygame.image.load(CHARACTER_BODIES[AMIT_BODY_INDEX].replace("folder", folder))
            img2 = pygame.transform.scale(img, (FIRST_SCREEN_ITEM_WIDTH, FIRST_SCREEN_ITEM_HEIGHT))
            self.screen.blit(img2, (185, 150 + FIRST_SCREEN_ITEM_HEIGHT))
            # display face
            img = pygame.image.load(CHARACTER_LEGS[AMIT_LEGS_INDEX].replace("folder", folder))
            img3 = pygame.transform.scale(img, (FIRST_SCREEN_ITEM_WIDTH, FIRST_SCREEN_ITEM_HEIGHT))
            self.screen.blit(img3, (185, 150 + 2 * FIRST_SCREEN_ITEM_HEIGHT))
        elif screen_num == 1:
            pass
        else:
            self.display()

    def display_on_button(self, button_num):
        if button_num == 1:
            self.x = FIRST_COL
            self.y = FIRST_ROW
        elif button_num == 2:
            self.x = FIRST_COL
            self.y = SECOND_ROW
        elif button_num == 3:
            self.x = SECOND_COL
            self.y = SECOND_ROW
        elif button_num == 4:
            self.x = THIRD_COL
            self.y = SECOND_ROW
        elif button_num == 5:
            self.x = THIRD_COL
            self.y = FIRST_ROW
        self.x = self.x + (LEVEL_BUTTON_WIDTH - CHARACTER_WIDTH) / 2
        self.y = self.y + (LEVEL_BUTTON_HEIGHT - CHARACTER_HEIGHT) / 2
        self.mood = "ameat boy"
        self.display()

    def right(self, sprint):
        for i in range(STEP):
            if "right" not in self.is_blocked():
                self.x += 1
                self.mood = "right"
            if "right" not in self.is_blocked() and sprint:
                self.x += 1.1
                self.mood = "running right"
        self.display()

    def left(self, sprint):
        for i in range(STEP):
            if "left" not in self.is_blocked():
                self.x -= 1
                self.mood = "left"
            if "left" not in self.is_blocked() and sprint:
                self.x -= 1.1
                self.mood = "running left"
        self.display()

    def jump(self):
        if "down" in self.is_blocked():
            self.velY -= JUMP
        self.display()
        # if "down" in self.is_blocked():
        #     for i in range(JUMP):
        #        if pressed_buttons[pygame.K_SPACE] and "up" not in self.is_blocked():
        #     if pressed_buttons[pygame.K_SPACE]:
        #         self.velY -= 15
        #            self.pos.add_y(-1)
        # else:
        #     pass

    def gravity(self):
        if "down" not in self.is_blocked():
            if self.velY < 15:
                self.velY += 2
        else:
            self.velY = 0

    def is_obstacle(self):
        if "obstacle" in self.is_blocked():
            return True

    def from_where_blocked(self, list_platforms_collide):
        list_of_collision = []
        for platform in list_platforms_collide:
            up = pygame.Rect(self.x + 1, self.y, CHARACTER_WIDTH - 2, 1)
            down = pygame.Rect(self.x + 1, self.y + CHARACTER_HEIGHT, CHARACTER_WIDTH - 5, 1)
            left = pygame.Rect(self.x, self.y + 1, 1, CHARACTER_HEIGHT - 2)
            right = pygame.Rect(self.x + ITEM_WIDTH, self.y + 1, 1, CHARACTER_HEIGHT - 2)
            plat = pygame.Rect(platform.x, platform.y, platform.width, platform.height)
            if platform.obstacle == True:
                list_of_collision.append("obstacle")
            if up.colliderect(plat):
                list_of_collision.append("up")
            if down.colliderect(plat):
                list_of_collision.append("down")
            if right.colliderect(plat):
                list_of_collision.append("right")
            if left.colliderect(plat):
                list_of_collision.append("left")
        return list_of_collision

    def is_blocked(self):
        list_platforms_collide = []
        character = pygame.Rect(self.x, self.y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
        for platform in self.list_of_platforms:
            plat = pygame.Rect(platform.x, platform.y , platform.width, platform.height)
            collide = character.colliderect(plat)
            if collide:
                list_platforms_collide.append(platform)
        return self.from_where_blocked(list_platforms_collide)


class Princess(Character):
    def __init__(self, x, y, list_of_platforms, screen):
        super().__init__(x, y, list_of_platforms, screen)

    def display(self):
            if self.velY > 0:
                k = 0
                while "down" not in self.is_blocked() and k <= self.velY:
                    k += 1
                    self.y += 1
            elif self.velY < 0:
                k = 0
                while "up" not in self.is_blocked() and k >= self.velY:
                    k -= 1
                    self.y -= 1
            # display princess
            img = pygame.image.load(PRINCESS_PIC)
            img1 = pygame.transform.scale(img, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
            self.screen.blit(img1, (self.x, self.y))

    def collide_with_character(self, character):
        princess = pygame.Rect(self.x, self.y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
        character = pygame.Rect(character.x, character.y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
        if princess.colliderect(character):
            return True
        else:
            return False
