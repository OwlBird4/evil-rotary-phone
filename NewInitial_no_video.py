import pygame,sys,random,time
import math
import time
#import moviepy
#from moviepy.editor import *
#import os
#import imageio
#imageio.plugins.ffmpeg.download()

         
class Image:
    def __init__(self, name,width=100, height=100,transparent=False ):
        if transparent == True:
            self.pic = pygame.image.load("images//"+name).convert_alpha()
        else:
            self.pic = pygame.image.load("images//"+name).convert()
        self.pic = pygame.transform.scale(self.pic, (width, height))   
        self.x = 0
        self.y = 0
        self.width=width
        self.height=height
             
    def display(self):      
        screen.blit(self.pic,[self.x,self.y ])
    def get_width(self):
        return self.width
    def get_height(self)  :
        return self.height
    def setXY(self,x,y):
        self.x = x
        self.y = y
    def getRect(self):
        r = pygame.Rect(self.x,self.y,self.width,self.height)
        return r
    def resize(self,newW,newH):
        self.pic=pygame.transform.scale(self.pic, (newW, newH))

        
def PressEnterToContinue():
    cont = True
    while cont == True:
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()    
            if keys_pressed[pygame.K_RETURN]:
                cont = False

def imagesCollide(ship,ship2):
    aRect = ship.getRect()
    bRect = ship2.getRect()
    
    if aRect.colliderect(bRect):
        return True
    
    else: 
        return False

def mouseClick(pic1):
    click=False
    pos = pygame.mouse.get_pos()
    aRect = pic1.getRect()
    if aRect.collidepoint(pos[0],pos[1]) and pygame.mouse.get_pressed()[0] :
        click=True

    return click


screenWidth = 1150
screenHeight =  600


screen = pygame.display.set_mode([screenWidth,screenHeight])
pygame.init()

pygame.key.set_repeat(100,30)
clock = pygame.time.Clock()
clock.tick(60)



# load images for your game . Use PNG and JPG

#load fonts

myFont24 = pygame.font.SysFont("Courier",24,True,False)
myFont48 = pygame.font.SysFont("Courier",60,True,False)

# Color Variables
#add as many as you like. search google RGB color values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

shipsremain = 8


#initialize some variables
reps=0
jumpmode=False
run_once=False
run_once_2=False
run_once_3=False
run_once_4=False
level = 0
score = 0
gameOver = False
showLaser = False
pygame.display.set_caption("haxxor")

#----------------------------------------------------------------------
 


#----------------------------------------------------------------------
# Main Program Loops 60x per second 
#----------------------------------------------------------------------


# load images
Windows_10_desktop = Image("Windows-10-desktop.png",screenWidth,screenHeight,True);
mario_standing = Image("mario_standing.png",75,75,True);
mario_standing_2 = Image("mario_standing.png",75,75,True);
mario_in_air = Image("mario_in_air.png",75,75,True);
galaga_icon_locked = Image("galaga_icon_locked.png",150,150,True);
galaga_icon_unlocked = Image("galaga_icon_unlocked.png",150,150,True);
ship_fighter = Image("ship_fighter.png",100,100,True);
alien_ship =Image("alien_small.png",50,50,True);
space_back = Image("Spaceimage.jpg",screenWidth,screenHeight,True);
alien_ship2 =Image("alien_small.png",50,50,True);
alien_ship3 =Image("alien_small.png",50,50,True);
laser_bullet =Image("laser_fire_beam.png",25,25,True);
alien_ship4 =Image("alien_small.png",50,50,True);
alien_ship5 =Image("alien_small.png",50,50,True);
alien_ship6 =Image("alien_small.png",50,50,True);
alien_ship7 =Image("alien_small.png",50,50,True);
alien_ship8 =Image("alien_small.png",50,50,True);
cat_mouse_locked =Image("cat_mouse_locked.png",150,150,True);
cat_mouse_unlocked =Image("cat_mouse_unlocked.png",150,150,True);
tower_defense_icon_locked = Image("tower_defense_icon_locked.png",100,100,True);
tower_defense_icon_unlocked = Image("tower_defense_icon_unlocked.png",100,100,True);

while gameOver == False :
    pygame.display.update()

    if jumpmode==True :
           mario_standing.x+= 10
           mario_standing.y-= 10
           mario_in_air.x = mario_standing.x
           mario_in_air.y = mario_standing.y
           mario_standing = mario_in_air
           reps+=1
           if reps == 10 :
               jumpmode=False
               reps=0

    mario_standing.y+= 5

    if mario_standing.y >= 600-mario_standing.height :
        mario_standing_2.x = mario_standing.x
        mario_standing_2.y = mario_standing.y
        mario_standing = mario_standing_2
        mario_standing.y = 600-mario_standing.height
    
    if level == 0 :
#        if run_once_4 == False :
            # Video Code
#            os.environ["SDL_VIDEO_CENTERED"] = "1"
#            clip = VideoFileClip('test.mp4')
#            clip.preview()
#            screenWidth = 1150
#            screenHeight =  600
#            screen = pygame.display.set_mode([screenWidth,screenHeight])
#            pygame.init()
#            run_once_4 = True

        # Intro Screen Code
        galaga_icon_locked.x=900
        galaga_icon_locked.y=468
        cat_mouse_locked.x=600
        cat_mouse_locked.y=468
        tower_defense_icon_locked.x=300
        tower_defense_icon_locked.y=510
        Windows_10_desktop.display()
        galaga_icon_locked.display()
        cat_mouse_locked.display()
        tower_defense_icon_locked.display()
        text = myFont48.render("Welcome Haxxor!",True,RED)
        screen.blit(text,[300,100])   
        mario_standing.display()
        pygame.display.update()
        
        if run_once==False :
            enter = False
            run_once = True

#---------------Galaga Entry Code
        if enter == True and imagesCollide(mario_standing,galaga_icon_locked) and level == 0 :
            x = galaga_icon_locked.x
            y = galaga_icon_locked.y
            galaga_icon_locked.x = x
            galaga_icon_locked.y = y
            Windows_10_desktop.display()
            galaga_icon_locked = Image("galaga_icon_unlocked.png",150,150,True);
            galaga_icon_locked.x = x
            galaga_icon_locked.y = y
            galaga_icon_locked.display();
            galaga_icon_locked.display()
            cat_mouse_locked.display()
            tower_defense_icon_locked.display();
            mario_standing.display()
            galaga_icon_locked.x = x
            galaga_icon_locked.y = y
            text = myFont48.render("Welcome Haxxor!",True,RED)
            screen.blit(text,[300,100])
            pygame.display.update()
            pygame.time.delay(1000)
            level = 1

        if enter == True and imagesCollide(mario_standing,cat_mouse_locked) and level == 0 :
            x = cat_mouse_locked.x
            y = cat_mouse_locked.y
            cat_mouse_locked.x = x
            cat_mouse_locked.y = y
            Windows_10_desktop.display()
            cat_mouse_locked = Image("cat_mouse_unlocked.png",150,150,True);
            cat_mouse_locked.x = x
            cat_mouse_locked.y = y
            cat_mouse_locked.display();
            galaga_icon_locked.display()
            cat_mouse_locked.display()
            tower_defense_icon_locked.display();
            mario_standing.display()
            cat_mouse_locked.x = x
            cat_mouse_locked.y = y
            text = myFont48.render("Welcome Haxxor!",True,RED)
            screen.blit(text,[300,100])
            pygame.display.update()
            pygame.time.delay(1000)
            level = 2

        if enter == True and imagesCollide(mario_standing,tower_defense_icon_locked) and level == 0 :
            x = tower_defense_icon_locked.x
            y = tower_defense_icon_locked.y
            tower_defense_icon_locked.x = x
            tower_defense_icon_locked.y = y
            Windows_10_desktop.display()
            tower_defense_icon_locked = Image("tower_defense_icon_unlocked.png",150,150,True);
            tower_defense_icon_locked.x = x
            tower_defense_icon_locked.y = y
            tower_defense_icon_locked.display();
            galaga_icon_locked.display()
            cat_mouse_locked.display()
            tower_defense_icon_locked.display();
            mario_standing.display()
            tower_defense_icon_locked.x = x
            tower_defense_icon_locked.y = y
            text = myFont48.render("Welcome Haxxor!",True,RED)
            screen.blit(text,[300,100])
            pygame.display.update()
            pygame.time.delay(1000)
            level = 3


        enter = False


#-----------------#LEVEL 1 CODE
    
    if level == 1:

        space_back.display()
        if run_once_2 == False :
            alien_ship.x = 900
            alien_ship.y = 468
            alien_ship2.x = 800
            alien_ship2.y = 468
            alien_ship3.x = 700
            alien_ship3.y = 468
            alien_ship4.x = 600
            alien_ship4.y = 468
            alien_ship5.x = 900
            alien_ship5.y = 518
            alien_ship6.x = 800
            alien_ship6.y = 518
            alien_ship7.x = 700
            alien_ship7.y = 518
            alien_ship8.x = 600
            alien_ship8.y = 518
            run_once_2 = True
        ship_fighter.display()
        alien_ship.display()
        alien_ship2.display()
        alien_ship3.display()
        alien_ship4.display()
        alien_ship5.display()
        alien_ship6.display()
        alien_ship7.display()
        alien_ship8.display()

        text = myFont24.render("Ships That Remain:"+str(shipsremain),True,WHITE)
        screen.blit(text,[600,0])

        if showLaser == True:
            laser_bullet.display()
            laser_bullet.y+=5

        if imagesCollide(laser_bullet,alien_ship) :
            alien_ship.x = 3100
            alien_ship.y = 3100
            shipsremain -= 1

        if imagesCollide(laser_bullet,alien_ship2) :
            alien_ship2.x = 3100
            alien_ship2.y = 3100
            shipsremain -= 1

        if imagesCollide(laser_bullet,alien_ship3) :
            alien_ship3.x = 3100
            alien_ship3.y = 3100
            shipsremain -= 1

        if imagesCollide(laser_bullet,alien_ship4) :
            alien_ship4.x = 3100
            alien_ship4.y = 3100
            shipsremain -= 1

        if imagesCollide(laser_bullet,alien_ship5) :
            alien_ship5.x = 3100
            alien_ship5.y = 3100
            shipsremain -= 1

        if imagesCollide(laser_bullet,alien_ship6) :
            alien_ship6.x = 3100
            alien_ship6.y = 3100
            shipsremain -= 1

        if imagesCollide(laser_bullet,alien_ship7) :
            alien_ship7.x = 3100
            alien_ship7.y = 3100
            shipsremain -= 1

        if imagesCollide(laser_bullet,alien_ship8) :
            alien_ship8.x = 3100
            alien_ship8.y = 3100
            shipsremain -= 1
            

            

        
        

#-----------------#LEVEL 2 CODE
    
    if level == 2:
        screen.fill(RED)
        mario_standing.display()


#-----------------#LEVEL 3 CODE
        
    if level == 3:
        screen.fill(GREEN)
        mario_standing.display()
  
        
   
# ------------ KEYBOARD INPUT -------------------------------------------------
# must be indented=
    for event in pygame.event.get():
        keys_pressed = pygame.key.get_pressed()    

# all button pressing here
        if keys_pressed[pygame.K_RIGHT]:
            mario_standing.x+= 3
            
        if keys_pressed[pygame.K_LEFT]:
            mario_standing.x-= 3

        if keys_pressed[pygame.K_UP]:
            mario_standing.y-= 3
            
        if keys_pressed[pygame.K_DOWN]:
            mario_standing.y+= 3

        if keys_pressed[pygame.K_RETURN]:
            enter = True

        if keys_pressed[pygame.K_SPACE]:
            jumpmode=True

        if keys_pressed[pygame.K_d]:
            ship_fighter.x+= 4

        if keys_pressed[pygame.K_a]:
            ship_fighter.x-=4

        if keys_pressed[pygame.K_RIGHT]:
            alien_ship.x+=5

        if keys_pressed[pygame.K_LEFT]:
            alien_ship.x-=5

        if keys_pressed[pygame.K_RIGHT]:
            alien_ship2.x+=5

        if keys_pressed[pygame.K_LEFT]:
            alien_ship2.x-=5

        if keys_pressed[pygame.K_RIGHT]:
            alien_ship3.x+=5

        if keys_pressed[pygame.K_LEFT]:
            alien_ship3.x-=5

        if keys_pressed[pygame.K_RIGHT]:
            alien_ship4.x+=5

        if keys_pressed[pygame.K_LEFT]:
            alien_ship4.x-=5

        if keys_pressed[pygame.K_RIGHT]:
            alien_ship5.x+=5

        if keys_pressed[pygame.K_LEFT]:
            alien_ship5.x-=5

        if keys_pressed[pygame.K_RIGHT]:
            alien_ship6.x+=5

        if keys_pressed[pygame.K_LEFT]:
            alien_ship6.x-=5

        if keys_pressed[pygame.K_RIGHT]:
            alien_ship7.x+=5
            alien_ship8.x+=5

        if keys_pressed[pygame.K_LEFT]:
            alien_ship7.x-=5
            alien_ship8.x-=5


        if keys_pressed[pygame.K_SPACE]:
            showLaser = True
            laser_bullet.x = ship_fighter.x
            laser_bullet.y = ship_fighter.y

    
            
            
        
            

  

        if keys_pressed[pygame.K_x]:
            pygame.quit()
            sys.exit()      


pygame.quit() #do not move 
sys.exit() #do not move 
