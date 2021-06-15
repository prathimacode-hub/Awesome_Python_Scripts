#IMPORTING
import pygame
import random
import sys, os
pygame.font.init()
#pygame.mixer.init()

pygame.init()

#VARIABLES
WIDTH,HEIGHT=500,600
WIN=pygame.display.set_mode((WIDTH,HEIGHT))

#COLORS
BG=(242,194,203)
SLB=(217,132,155)
BNR=(191,122,160)
TXT=(254,245,238)
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
YELLOW=(255,255,0)

#HIT_SOUND=pygame.mixer.Sound(os.path.join('assets','hit_sound.mp3'))

#TITLE AND ICON
pygame.display.set_caption("Oddly Satisfying Animation")
ICON = pygame.image.load(os.path.join("Images", "splash.png"))
pygame.display.set_icon(ICON)


#CLASS DEFINITIONS
class Element(object):
    def __init__(self,x,y,b,l,col):
        self.x = x
        self.y = y
        self.b=b
        self.col=col
        self.l=l
        self.rectangle= pygame.Rect(self.x,self.y,self.b,self.l)
        self.velx = 0
        self.vely=0
        self.g=0
        self.bouncers=[]

    def draw(self,window):
        pygame.draw.rect(window,self.col,self.rectangle)
       
class Slab(Element):
    def __init__(self,x,y,b,l,col):
        super().__init__(x,y,b,l,col)       
    def draw(self,window):
        super().draw(window)

    def rect_ret(self):
        rectangle1=self.rectangle
        return rectangle1

    def slabMotion(self):
        self.g=0.25
        self.velx = 0
        self.vely+=self.g
        self.rectangle.y += self.vely
        
        
    def collisionBoundary(self):
        if self.rectangle.top<=10 and self.vely<0:
            self.vely *= -1
        if self.rectangle.bottom >= HEIGHT-10:
            self.vely=0
        

    def motionControl(self,keys_pressed):
        if keys_pressed[pygame.K_SPACE]:
            self.vely = 0
            self.vely -= 6


class Bouncer(Element):
    def __init__(self,x,y,b,l,col):
        super().__init__(x,y,b,l,col)
        self.velx = 3
        self.vely = 4
    def draw(self,window):
        super().draw(window)

    def rect_ret(self):
        rectangle1=self.rectangle
        return rectangle1

    def bouncerMotion(self):
        self.rectangle.x +=self.velx
        self.rectangle.y += self.vely

    def collisionBoundary(self):
        if (self.rectangle.left<=10 and self.velx<0) or (self.rectangle.right>=WIDTH-10 and self.velx>0):
            self.velx *= -1
        if (self.rectangle.top<=10 and self.vely<0) or (self.rectangle.bottom >= HEIGHT-10 and self.vely>0):
            self.vely *= -1       

    def collisionSlab(self,rectangle1):
        self.collision_tolerance=10
        self.rectangle1=rectangle1
        if self.rectangle.colliderect(self.rectangle1):
            if abs(self.rectangle1.bottom - self.rectangle.top) < self.collision_tolerance and self.vely<0:
                self.vely *= -1

            if abs(self.rectangle1.top - self.rectangle.bottom) < self.collision_tolerance and self.vely>0:
                self.vely *= -1

            if abs(self.rectangle1.left - self.rectangle.right) < self.collision_tolerance and self.velx>0:
                self.velx *= -1

            if abs(self.rectangle1.right - self.rectangle.left) < self.collision_tolerance and self.velx<0:
                self.velx *= -1

    def collisionBouncer(self,rectangle_list):
        self.collision_tolerance=10
        for rectangles in rectangle_list:
            self.rectangle1=rectangles
            self.collisionSlab(self.rectangle1)

#LIST OF RANDOM X AND Y COORDINATES LIST GENERATION FOR BOUNCERS
def posGenerator(n):
    posx_list=[]
    posy_list=[]
    #for x
    for i in range(n):
        value=random.randint(15,WIDTH-15)
        posx_list.append(value)

    #for y
    for i in range(n):
        value=random.randint(15,HEIGHT-15)
        posy_list.append(value)

    return posx_list,posy_list
        
    
        
#MAIN
def main():
    run=True
    FPS=60    
    n=6
    posx_list,posy_list=posGenerator(n)

    #OBJECTS
    element1=Slab(WIDTH//2-100,HEIGHT//2-25,200,50,SLB)
    element2=Bouncer(posx_list[0],posy_list[0],50,50,BNR)
    element3=Bouncer(posx_list[1],posy_list[1],50,50,BNR)
    element4=Bouncer(posx_list[2],posy_list[2],50,50,BNR)
    element5=Bouncer(posx_list[3],posy_list[3],50,50,BNR)
    element6=Bouncer(posx_list[4],posy_list[4],50,50,BNR)
    element7=Bouncer(posx_list[5],posy_list[5],50,50,BNR)
    rectangle1=element1.rect_ret()
    rectangle2=element2.rect_ret()
    rectangle3=element3.rect_ret()
    rectangle4=element4.rect_ret()
    rectangle5=element5.rect_ret()
    rectangle6=element6.rect_ret()
    rectangle7=element7.rect_ret()
    rectangle_list=[rectangle2,rectangle3,rectangle4,rectangle5,rectangle6,rectangle7]

    #DRAWING ELEMENTS ON SCREEN
    def draw_window():
        WIN.fill(BG)
        element1.draw(WIN)
        element2.draw(WIN)
        element3.draw(WIN)
        element4.draw(WIN)
        element5.draw(WIN)
        element6.draw(WIN)
        element7.draw(WIN)
        pygame.display.update()
        
        

    clock=pygame.time.Clock()
    
    #INFINITE LOOP
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
                run=False
           
        keys_pressed=pygame.key.get_pressed()
        
        #element1
        element1.slabMotion()
        element1.collisionBoundary()
        element1.motionControl(keys_pressed)
        

        #element2
        element2.bouncerMotion()
        element2.collisionBoundary()
        element2.collisionSlab(rectangle1)
        element2.collisionBouncer(rectangle_list)
        

        #element3
        element3.bouncerMotion()
        element3.collisionBoundary()
        element3.collisionSlab(rectangle1)
        element3.collisionBouncer(rectangle_list)

        #element4
        element4.bouncerMotion()
        element4.collisionBoundary()
        element4.collisionSlab(rectangle1)
        element4.collisionBouncer(rectangle_list)

        #element5
        element5.bouncerMotion()
        element5.collisionBoundary()
        element5.collisionSlab(rectangle1)
        element5.collisionBouncer(rectangle_list)

        #element6
        element6.bouncerMotion()
        element6.collisionBoundary()
        element6.collisionSlab(rectangle1)
        element6.collisionBouncer(rectangle_list)

        #element7
        element7.bouncerMotion()
        element7.collisionBoundary()
        element7.collisionSlab(rectangle1)
        element7.collisionBouncer(rectangle_list)

        draw_window()

#INSTRUCTION MENU       
def main_menu():
    title_font=pygame.font.SysFont("comicsans",30)
    run = True
    while run:
        WIN.fill(BG)
        title_label1= title_font.render("Press the Spacebar to move the slab...", 1, (TXT))
        title_label2 = title_font.render("Click anywhere on the screen...", 1, (TXT))
        
        WIN.blit(title_label1, (WIDTH/2 - title_label1.get_width()/2, 350))
        WIN.blit(title_label2, (WIDTH/2 - title_label2.get_width()/2, 400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()        
       
#CALLING           
main_menu()

