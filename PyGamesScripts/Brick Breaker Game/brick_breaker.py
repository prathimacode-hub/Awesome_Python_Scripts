import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Breaker Game")


#Font
font = pygame.font.SysFont('Ludica', 40) 

# Colors
bg = (234, 218, 184)
block_red = (242, 55, 96)
block_green = (16, 174, 17)
block_blue = (52, 25, 196)
paddle_col = (42, 85, 96)
paddle_outline = (0, 43, 70)
text_col = (78, 81, 139)
# (42, 85, 96) (142, 135, 123)

# Game variables
cols = 6
rows = 6

clock = pygame.time.Clock()
fps = 60
live_ball = False
game_over = 0


#Dispaly Text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))


# Wall class
class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50

    def create_wall(self):
        self.blocks = []
        #define an empty list for an individual block
        block_individual = []
        for row in range(rows):
            block_row = []
            #iterate through each column in that row
            for col in range(cols):
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                #assign block strength based on row
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                #create a list at this point to store the rect and colour data
                block_individual = [rect, strength]
                block_row.append(block_individual)
            #append the row to the full list of blocks
            self.blocks.append(block_row)


    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                #assign a colour based on block strength
                if block[1] == 3:
                    block_col = block_blue
                elif block[1] == 2:
                    block_col = block_green
                elif block[1] == 1:
                    block_col = block_red

                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, bg, (block[0]), 2)



# Paddle class
class paddle():
    def __init__(self):
        self.reset()
        
    def move(self):
        #reset movement direction
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1

        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1


    def draw(self):
        pygame.draw.rect(screen, paddle_col, self.rect)
        pygame.draw.rect(screen, paddle_outline, self.rect, 3)


    def reset(self):
        #define paddle variables
        self.height = 20
        self.width = int(screen_width / cols)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0



#Ball class
class game_ball():
    def __init__(self, x, y):
        self.reset(x, y)

    def move(self):

        collision_thresh = 5

        #Start off with the assumption that the wall has been destroyed
        wall_destroyed = 1
        row_count = 0
        for row in wall.blocks:
            item_count = 0
            for item in row:
                #Check collision
                if self.rect.colliderect(item[0]):
                    #Above
                    if abs(self.rect.bottom - item[0].top < collision_thresh and self.speed_y > 0):
                        self.speed_y *= -1

                    #Below
                    if abs(self.rect.top - item[0].bottom < collision_thresh and self.speed_y < 0):
                        self.speed_y *= -1

                    #Left
                    if abs(self.rect.right - item[0].left < collision_thresh and self.speed_x > 0):
                        self.speed_x *= -1

                    #Right
                    if abs(self.rect.left - item[0].right < collision_thresh and self.speed_x < 0):
                        self.speed_x *= -1


                    #Reduce block strength
                    if wall.blocks[row_count][item_count][1] > 1:
                        wall.blocks[row_count][item_count][1] -= 1
                    else:
                        wall.blocks[row_count][item_count][0] = (0, 0, 0, 0)

                    #Check if blocks still exits
                if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                    wall_destroyed = 0

                item_count += 1
                
            row_count += 1

            #Check if the wall destroyed
        if wall_destroyed == 1:
            self.game_over = 1
                



        #Check for collision with wall
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1

        #Check for collision with top
        if self.rect.top < 0:
            self.speed_y *= -1
        
        #Check for collision with bottom
        if self.rect.bottom > screen_height:
            self.game_over = -1


        #Check for collision with paddle
        if self.rect.colliderect(player_paddle):
            #Collision from top
            if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += player_paddle.direction
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                    self.speed_x = -self.speed_max

            else:
                self.speed_x *= -1



        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over


    def draw(self):
        pygame.draw.circle(screen, paddle_col, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(screen, paddle_outline, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)


    def reset(self, x, y):
        self.ball_rad = 15
        self.x = x-self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0






# Instance of a wall
wall = wall()
wall.create_wall()

# Instance of paddle
player_paddle = paddle()

# Instance of ball
ball = game_ball(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)


run = True
while run:

    clock.tick(fps)
    screen.fill(bg)

    #Draw all objects
    # Draw wall
    wall.draw_wall()
    # Draw paddle
    player_paddle.draw()
    # Draw ball
    ball.draw()


    if live_ball:
        player_paddle.move()
        game_over = ball.move()
        if game_over != 0:
            live_ball = False


    #Player instructions
    if not live_ball:
        if game_over == 0:
            draw_text('CLICK ANYWHERE TO START', font, text_col, 300, screen_height // 2 + 100)
        elif game_over == 1:
            draw_text('YOU WON!', font, text_col, 400, screen_height // 2 + 50)
            draw_text('CLICK ANYWHERE TO START', font, text_col, 300, screen_height // 2 + 100)
        elif game_over == -1:
            draw_text('YOU LOST!', font, text_col, 400, screen_height // 2 + 50)
            draw_text('CLICK ANYWHERE TO START', font, text_col, 300, screen_height // 2 + 100)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            ball.reset(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)
            player_paddle.reset()
            wall.create_wall()


    pygame.display.update()

pygame.quit()
