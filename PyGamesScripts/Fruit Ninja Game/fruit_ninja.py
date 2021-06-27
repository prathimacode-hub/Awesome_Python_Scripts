import pygame, sys
import os
import random

player_lives = 3                                                #keep track of lives
score = 0                                                       #keeps track of score
fruits = ['melon','pear','orange','pomegranate','bomb']         #entities in the game

# initialize pygame and create window
w=800
h=600
FPS = 12        #The game display will refresh every 1/12th second
pygame.init()
pygame.display.set_caption('Fruit-Ninja Game')
gameDisplay = pygame.display.set_mode((w,h))   #sets game display size
clock = pygame.time.Clock()

# Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

background = pygame.image.load('Media/background.png')          #game background
font = pygame.font.Font(os.path.join(os.getcwd(),'fontdesign.ttf'),42)    #font of game display
score_text = font.render('Score : '+str(score),True,(255,255,255))   #score display

# Generalized structure of the fruit Dictionary
def generate_random_fruits(fruit):
    fruit_path="Media/"+fruit +".png"
    # 'x' determines where the fruit should be positioned on x-coordinate
    # 'speed_x' determines how fast the fruit should move in x direction.Controls the diagonal movement of fruits
    # 'speed_y' controls the speed of fruits in y-direction (UPWARD)
    # 'throw':False determines if the generated coordinate of the fruits is outside the gameDisplay or not.If outside,then it will be discarded.
    data[fruit]={
        'img': pygame.image.load(fruit_path),'x':random.randint(100,500),'y':800,
        'speed_x': random.randint(-10,10),'speed_y': random.randint(-80,-60),
        'throw': False,'t': 0,'hit': False
    }

    #Return the next random floating point number in the range [0.0, 1.0) to keep the fruits inside the gameDisplay
    if (random.random() >= 0.75):
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False

# Dictionary to hold the data the random fruit generation
data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("Media/red_lives.png"), (x, y))

# Generic method to draw fonts on the screen
font_name = pygame.font.match_font('fontdesign.ttf')
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop=(x,y)
    gameDisplay.blit(text_surface, text_rect)

# draw players lives
def draw_lives(display, x, y, lives, image) :
    for i in range(lives) :
        img = pygame.image.load(image)
        img_rect = img.get_rect()       #gets the (x,y) coordinates of the cross icons (lives on the the top rightmost side)
        img_rect.x = int(x + 35 * i)    #position of lives icon (sets the next cross icon 35pixels awt from the previous one)
        img_rect.y = y                  #takes care of how many pixels the cross icon should be positioned from top of the screen
        display.blit(img, img_rect)

# show game over display & front display
def show_gameover_screen():
    gameDisplay.blit(background, (0,0))
    draw_text(gameDisplay, "FRUIT NINJA!", 90, w/2,h/4)
    if not game_over :
        draw_text(gameDisplay,"Score : " + str(score), 50, w/2,h/2)
        draw_text(gameDisplay, "Game Over!!", 50,w/2,h*5/8)

    draw_text(gameDisplay, "Press any key to play!", 64,w/2,h*3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYUP:
                waiting = False

# Game Loop
first_round = True
game_over = True        #terminates the game while loop if more than 3-Bombs are cut
game_running = True     #used to manage the game loop
while game_running :
    if game_over :
        if first_round :
            show_gameover_screen()
            first_round = False
        game_over = False
        player_lives = 3
        draw_lives(gameDisplay, 690, 5, player_lives, 'Media/red_lives.png')
        score = 0

    for event in pygame.event.get():
        # checking for closing window
        if event.type == pygame.QUIT:
            game_running = False

    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(score_text, (0, 0))
    draw_lives(gameDisplay, 690, 5, player_lives,'Media/red_lives.png')

    for key, value in data.items():
        if value['throw']:
            value['x'] += value['speed_x']          #moving the fruits in x-coordinates
            value['y'] += value['speed_y']          #moving the fruits in y-coordinate
            value['speed_y'] += (1 * value['t'])    #increasing y-corrdinate
            value['t'] += 1                         #increasing speed_y for next loop

            if value['y'] <= 800:
                gameDisplay.blit(value['img'], (value['x'], value['y']))    #dynamic display of fruit inside display screen
            else:
                generate_random_fruits(key)

            current_position=pygame.mouse.get_pos()   #gets the current coordinate(x,y) in pixels of the mouse

            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x']+60 \
                    and current_position[1] > value['y'] and current_position[1] < value['y']+60:
                if key == 'bomb':
                    player_lives -= 1
                    if player_lives == 0:

                        hide_cross_lives(690, 15)
                    elif player_lives == 1 :
                        hide_cross_lives(725, 15)
                    elif player_lives == 2 :
                        hide_cross_lives(760, 15)
                    #if the user clicks bombs for three time,GAME OVER message should be displayed and the window should be reset
                    if (player_lives < 0):
                        show_gameover_screen()
                        game_over = True

                    half_fruit_path = "Media/explosion.png"
                else:
                    half_fruit_path = "Media/" + "half_" + key + ".png"

                value['img'] = pygame.image.load(half_fruit_path)
                value['speed_x'] += 10
                if key != 'bomb' :
                    score += 1
                score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
                value['hit'] = True
        else:
            generate_random_fruits(key)

    pygame.display.update()
    clock.tick(FPS)      #helps the loop to run at the right speed


pygame.quit()
