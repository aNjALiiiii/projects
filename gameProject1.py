import pygame
import time
import random

pygame.init()

pygame.mixer.music.load('roaring.wav')
pygame.mixer.music.play(-1)


display_width=800
display_height=600
car_Width=73
car_height=82
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

black=(0,0,0)
white=(100,0,255)

carImg = pygame.image.load('racecar.png')
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def crash():
    message_display('You Crashed')

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    start_game()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def start_game():
    gameExit = False
    x_change = 0
    y_change = 0
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                elif event.key == pygame.K_UP:
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    y_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key ==pygame.K_DOWN:
                    x_change = 0
                    y_change = 0
            print(event)

            x += x_change
            y += y_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x,y)
        if((x < 0) or (x > display_width-car_Width)):
            crash()
        elif((y < 0) or (x > display_height-car_height)):
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
        pygame.display.update()
        clock.tick(60)

start_game()
pygame.quit()
quit()
