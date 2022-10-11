from Views.Character.eSprites import eSprites
from Views.Character.Sprites import CharacterSprite
import pygame, time

class CharacterView():
    char_height = 32
    char_width = 19
    #
    def __init__(self, screen_width:int, screen_height) -> None:
        self.pos_x = 250
        self.pos_y = 250
        self.direction = eSprites.DOWN
        self.speed = 0.1
        self.px_step = 3
        #
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        #
        self.sprites = CharacterSprite('Tex/sprite.png')

    def update(self):
        if(self.pos_x >= self.SCREEN_HEIGHT - CharacterView.char_height):
            self.pos_x = self.SCREEN_HEIGHT - CharacterView.char_height
        if(self.pos_y >= self.SCREEN_WIDTH - CharacterView.char_width):
            self.pos_y = self.SCREEN_WIDTH - CharacterView.char_width
        if(self.pos_x <= 0):
            self.pos_x = 0
        if(self.pos_y <= 0):
            self.pos_y = 0


    def move(self, key:int, screen:pygame.Surface):
        if(key == pygame.K_z):
            self.direction = eSprites.UP
            for image in self.sprites.get_move(eSprites.UP):
                screen.fill((50,50,50))
                self.pos_y -= self.px_step
                self.update()
                screen.blit(image, (self.pos_x, self.pos_y))
                pygame.time.delay(60)
                pygame.display.flip()

        if(key == pygame.K_q):
            self.direction = eSprites.LEFT
            for image in self.sprites.get_move(self.direction):
                screen.fill((50,50,50))
                self.pos_x -= self.px_step
                self.update()
                screen.blit(image, (self.pos_x, self.pos_y))
                pygame.time.delay(60)
                pygame.display.flip()
                
        if(key == pygame.K_s):
            self.direction = eSprites.DOWN
            for image in self.sprites.get_move(self.direction):
                screen.fill((50,50,50))
                self.pos_y += self.px_step
                self.update()
                screen.blit(image, (self.pos_x, self.pos_y))
                pygame.time.delay(60)
                pygame.display.flip()

        if(key == pygame.K_d):
            self.direction = eSprites.RIGHT
            for image in self.sprites.get_move(self.direction):
                screen.fill((50,50,50))
                self.pos_x += self.px_step
                self.update()
                screen.blit(image, (self.pos_x, self.pos_y))
                pygame.time.delay(60)
                pygame.display.flip()