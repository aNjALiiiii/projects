import pygame
import time
import random

pygame.init()
score = 0
pygame.mixer.music.load('roaring.wav')
pygame.mixer.music.play(-1)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
#car image
carImg = pygame.image.load('racecar.png')
#background image
bg = pygame.image.load('1.png').convert()
intro_bg = pygame.image.load('bg.png')
intro_bg = pygame.transform.scale(intro_bg,(display_width,display_height))
bg = pygame.transform.scale(bg,(display_width,display_height))

gameIcon = pygame.image.load('racecar.png')
pygame.display.set_icon(gameIcon)
black = (0, 0, 0)
white = (255, 255, 255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
gray = (45,44,47)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)
clock = pygame.time.Clock()

racecar_width = 73


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    #game_loop()


def crash():
    message_display('You Crashed')
    #message_display("Your score: %s"%(score))
    game_intro()

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        gameDisplay.blit(intro_bg, (0, 0))
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    gameExit = False
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    dodged = 0
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        x_change = 0
                        y_change = 0
            print(event)

        x += x_change
        y += y_change

        gameDisplay.blit(bg,(0,0))

        button("Main menu",600,0, 200, 40, green, bright_green, game_intro)
        things(thing_startx, thing_starty, thing_width, thing_height, gray)
        thing_starty += thing_speed
        #score = dodged
        things_dodged(dodged)
        car(x, y)

        if ((x < 0) or (x > display_width - racecar_width)):
            # gameExit = True
            crash()
        if (thing_starty > display_height):
            thing_starty = -600
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
            print(dodged)

        if (y < thing_starty + thing_height):
            # print("Crossed vertically")
            if (
                        x > thing_startx and x < thing_startx + thing_width or x + racecar_width > thing_startx and x + racecar_width < thing_startx + thing_width):
                # print("Crossed horizontally")
                crash()

        pygame.display.update()

        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
