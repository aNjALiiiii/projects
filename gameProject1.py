import pygame
pygame.init()

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


def start_game():
    gameExit = False
    x_change = 0
    y_change = 0
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
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
        car(x,y)
        if((x < 0) or (x > display_width-car_Width)):
            gameExit = True
        elif((y < 0) or (x > display_height-car_height)):
            gameExit = True
        pygame.display.update()
        clock.tick(60)

start_game()
pygame.quit()
quit()