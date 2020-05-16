import sys
import pygame
import random

# # Set Color
Blue = (0,250,0)
Green = (0,0,250)
Black = (0,0,0)

# # Initial Setup
WIDTH, HEIGHT = (500, 500)
FPS = 60
pygame.init()           # initialise game
pygame.mixer.init()     # fro sound
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
all_sprite = pygame.sprite.Group()

# # Load Images: 
head = pygame.image.load("img/body.png").convert()
head = pygame.transform.scale(head, (25,25))
head.set_colorkey(head.get_at((0,0)))
rect = head.get_rect()



game_over = False
while not game_over:
    screen.fill(Black)
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:       # type ( event ) isequals playgame.QUIT
            print("Quit")
            game_over = True

    screen.blit(head,rect)
    # all_sprite.update()
    # all_sprite.draw(screen)           
    pygame.display.flip()

pygame.quit()

