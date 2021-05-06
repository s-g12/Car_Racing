import pygame
import tkinter
import time
import random


pygame.init()
display_width = 800
display_height = 600
gray = (119,118,110)
black = (0,0,0)
gamedisplays = pygame.display.set_mode((display_width , display_height))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()

carimg = pygame.image.load('car.jpeg')
backgroundpic= pygame.image.load('grass.jpg')
yellow_strip = pygame.image.load('yellow.png')
strip = pygame.image.load('white.jpg')
car_width = 36



def obstacle(obs_startx,obs_starty,obs):
    if obs == 0:
        obs_pic = pygame.image.load("car2.jpg")
    elif obs ==1:
        obs_pic = pygame.image.load("car3.jpg")
    elif obs ==2:
        obs_pic = pygame.image.load("car4.jpg")
    elif obs ==3:
        obs_pic = pygame.image.load("car5.jpg")
    elif obs ==4:
        obs_pic = pygame.image.load("car6.jpg")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))
    





def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()



def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect = text_objects(text,largetext)
    textrect.center = ((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(1)
    game_loop()

def crash():
    message_display("Crashed")



def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    
    gamedisplays.blit(backgroundpic,(670,0))
    gamedisplays.blit(backgroundpic,(670,200))
    gamedisplays.blit(backgroundpic,(670,400))

    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))
    
    gamedisplays.blit(strip,(140,400))
    gamedisplays.blit(strip,(140,200))
    gamedisplays.blit(strip,(140,0))
                      
    gamedisplays.blit(strip,(645,400))
    gamedisplays.blit(strip,(645,200))
    gamedisplays.blit(strip,(645,0))
    
def car(x,y):
    gamedisplays.blit(carimg,(x,y))
    
def game_loop():
    x=(display_width*0.45)
    y=(display_height*0.8)


    

    x_change = 0

    obstacle_speed = 9
    obs=0
    y_change=0
    
    obs_startx = random.randrange(140,645)

    obs_starty=-750
    
    obs_width=36
    obs_height=85

    

    
    bumped = False

    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5

            if event.key == pygame.K_RIGHT:
                x_change = 5

        if  event.type == pygame.KEYUP  :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0  

      

        x += x_change               


        gamedisplays.fill(gray)
        background()
        obs_starty -= obstacle_speed/4
        
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
    
        
        car(x,y)
        
        if x> 645  or x< 140:
            crash()
    
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(140,645)
            obs = random.randrange(0,4)

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width  or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                crash()
                

        
            
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
