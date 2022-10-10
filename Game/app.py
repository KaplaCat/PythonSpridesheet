import pygame, time
from Views.Character.Sprites import CharacterSprite
from Views.Character.CharacterView import CharacterView
from Configuration import Configuration

############### Init game ###############
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Spritesheets')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((50,50,50))

############### Class game ###############
character = CharacterView(SCREEN_WIDTH, SCREEN_HEIGHT)
config = Configuration()

if __name__ == '__main__':
    while config.RUN:
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_z]):
            character.move(pygame.K_z, screen)
        elif(keys[pygame.K_q]):
            character.move(pygame.K_q, screen)
        elif(keys[pygame.K_s]):
            character.move(pygame.K_s, screen)
        elif(keys[pygame.K_d]):
            character.move(pygame.K_d, screen)
        else:
            character.idle(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.RUN = False
                
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()