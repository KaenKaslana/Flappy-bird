import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (177, 252, 252)

birdImg = pygame.image.load('images.jpg')
birdImg = pygame. transform. scale(birdImg, (50, 50))
bg = pygame.image.load('download.jpg')

dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Dino Game')

clock = pygame.time.Clock()
 
dino_block = 25
dino_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("press start 2p", 25)

#display the lost message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# display the score
def score(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width*3/4, 0])

# display the speed level
def speed(msg, color):

  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [dis_width*3/4, 15])

# Game loop
def gameLoop():
    game_over = False
    game_close = False
    sc=0
    sp=1
    x1 = 0
    y1 = 175
    dino_speed = 15
    x1_change = 0
    y1_change = 0

    blockx = 590
    blocky = random.randrange(150,400)

    blockx2 = 590
    blocky2 = 600-blocky-150
    dis.fill(blue)

    while not game_over:
 
        while game_close == True:
            
            dis.fill(white)
            message("You Lost! Press C-Play Again or Q-Quit", red)
 
            pygame.display.update()
 
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
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -15
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 15
                elif event.key == pygame.K_SPACE:
                    x1_change = 0
                    y1_change = 0
        
        x1 += x1_change
        y1 += y1_change
        dis.blit(bg, (0,0))
        score(("Score:"+str(sc)), black)
        speed(("Speed level:"+str(sp)), black)
        dis.blit(birdImg, (x1,y1))
 
        pygame.draw.rect(dis, black, [blockx,600-blocky, 10, blocky])
        pygame.draw.rect(dis, black, [blockx2,0, 10, blocky2])
        pygame.display.update()
        blockx-=10
        blockx2-=10
        sc+=1
        if x1+50 == blockx and (y1+50)>=(600-blocky):
            game_close = True

        if x1+50 == blockx and y1<=blocky2:
            game_close = True
          
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        if blockx==-10:
            blockx = 590
            blockx2 = 590
            blocky = random.randrange(150,400)
            blocky2 = 600-blocky-150
            dino_speed+=2
            sp+=1
                        
        clock.tick(dino_speed)
      
    pygame.quit()
    quit()
 
gameLoop()