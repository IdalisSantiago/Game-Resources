# pygame setup/time/random
import pygame
import time
import random
 
from pygame.locals import *

pygame.init()
 
# Colors
white = (255, 255, 255)
yellow = (247, 223, 72)
black = (0, 0, 0)
red = (213, 50, 80)
green = (98, 181, 171)
blue = (50, 153, 213)
purple = (183, 150, 212)
 
# screen dimensions
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))

# Title
pygame.display.set_caption('Worm by Idalis')

#Start menu
mouse = pygame.mouse.get_pos() 
 
# keeps the display going
clock = pygame.time.Clock()
 
# Snake block sizes/food size/snake speed
worm_block = 10
fps = 15

 
# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
font_style2 = pygame.font.SysFont("bahnschrift", 80)
score_font = pygame.font.SysFont("comicsansms", 35)

#My drawings
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg,(dis_width,dis_height))


#The score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])
 
 
#The actual worm
def the_worm(worm_block, worm_List):
    for x in worm_List:
        body = pygame.image.load("body.png")
        body = pygame.transform.scale(body,(worm_block *3.5, worm_block *3.5)) 
        dis.blit(body, (x[0],x[1]))
        # pygame.draw.rect(dis, red, [x[0], x[1], worm_block, worm_block])
 
#Defineing Text
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 4.10, dis_height / 4])

def message2(msg, color):
    msg = font_style2.render(msg, True, color)
    dis.blit(msg, [dis_width / 3.70, dis_height / 7])
 
#Defining the game loop
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width /2
    y1 = dis_height /2
 
    x1_change = 0
    y1_change = 0
 
 #How to make the worm grow
    worm_List = []
    Length_of_worm = 1
 
 #Randomizing the food
    foodx = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0
 
 #Begining of the while loop
    while not game_over:

 #Actual Text
        while game_close == True:
            dis.blit(bg, (0,0))
            message("Press C to Play Again or Press Q to Quit", red)
            message2("Game Over", red)
            Your_score(Length_of_worm - 1)
            pygame.display.update()
            
 #Keys
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -worm_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = worm_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -worm_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = worm_block
                    x1_change = 0
 #grounds for losing
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
#background image
        dis.blit(bg,(0,0))
#food square
        candy = pygame.image.load("candy.png")
        candy = pygame.transform.scale(candy,(worm_block *4, worm_block *4))
        dis.blit(candy, (foodx,foody))
        # rect = pygame.draw.rect(dis, yellow, [foodx, foody, worm_block, worm_block])

#grounds for losing
        worm_Head = []
        worm_Head.append(x1)
        worm_Head.append(y1)
        worm_List.append(worm_Head)
        if len(worm_List) > Length_of_worm:
            del worm_List[0]
 
        for x in worm_List[:-1]:
            if x == worm_Head:
                game_close = True
 
        the_worm(worm_block, worm_List)
        Your_score(Length_of_worm - 1)
 
        pygame.display.update()
 
 #collecting food allows worm to grow by one block
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0
            Length_of_worm += 1
 
        clock.tick(fps)
 
    pygame.quit()
    quit()
 
gameLoop()