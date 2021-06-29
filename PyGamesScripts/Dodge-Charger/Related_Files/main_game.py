import sqlite3
import pygame
import os
import sys
import random
import time
from Related_Files.garage_menu import fetch_all_data
from Related_Files.garage_menu import COINS
from Related_Files.garage_menu import draw_coin

pygame.init()
pygame.mixer.init()
# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
# setup the screen
WIDTH, HEIGHT = 500, 660
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Charger")
clock = pygame.time.Clock()
FPS = 90
# sounds
HEART_COLLECT_SOUND = pygame.mixer.Sound("Sounds/mixkit-retro-arcade-casino-notification-211.wav")
HEART_COLLECT_SOUND.set_volume(0.3)
COIN_COLLECT_SOUND = pygame.mixer.Sound("Sounds/mario_coin_sound.mp3")
COIN_COLLECT_SOUND.set_volume(0.1)
HEALTH_LOSS_SOUND = pygame.mixer.Sound("Sounds/health_loss.wav")
HEALTH_LOSS_SOUND.set_volume(0.1)
GAME_OVER_SOUND = pygame.mixer.Sound("Sounds/mixkit-spooky-game-over-1948.wav")
GAME_OVER_SOUND.set_volume(0.4)
BUTTON_CLICK_SOUND = pygame.mixer.Sound("Sounds/mixkit-arcade-game-jump-coin-216.wav")
BUTTON_CLICK_SOUND.set_volume(0.3)
# Load background of the game
BACKGROUND = pygame.image.load(os.path.join("Assets/Background", "road.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
# Load all player car images
CAR_WIDTH, CAR_HEIGHT = 50, 110
CARS_IMG = []
for i in range(8):
    img = pygame.image.load(os.path.join("Assets/Vehicles", f"vehicle{i}.png"))
    img = pygame.transform.scale(img, (CAR_WIDTH, CAR_HEIGHT))
    CARS_IMG.append(img)
# Load all images of enemy cars
ENEMY_CARS = []
for i in range(6):
    img = pygame.image.load(os.path.join("Assets/Enemy_Cars", f"car{i}.png"))
    img = pygame.transform.scale(img, (CAR_WIDTH, 80))
    img = pygame.transform.rotate(img, 180)
    ENEMY_CARS.append(img)
# Load image of heart
HEART_IMG = pygame.image.load(os.path.join("Assets/Others", "heart.png"))
HEART_IMG = pygame.transform.scale(HEART_IMG, (32, 32))
# Load game over logo, crash car logo, home buttton
GAME_OVER_IMG = pygame.image.load(os.path.join("Assets/Others", "game_over_logo.png"))
GAME_OVER_IMG = pygame.transform.scale(GAME_OVER_IMG, (450, 90))
CRASH_CAR_IMG = pygame.image.load(os.path.join("Assets/Others", "crash_car.png"))
CRASH_CAR_IMG = pygame.transform.scale(CRASH_CAR_IMG, (250, 250))
HOME_BTN_IMG = pygame.image.load(os.path.join("Assets/Others", "home_logo.png"))
# database
def get_player_car_data(db, table):
    '''This function return data of that car which is equiped from all the cars
    Params : String(db), String(table)
    Return : tuple(row)'''
    row = None
    data = fetch_all_data(db, table)
    for r in data:
        if r[6] == 1:
            row = r
            break
    return row

class PlayerCar:
    def __init__(self, img, speed, health, pos_x, pos_y):
        self.img = img
        self.speed = speed
        self.health = health
        self.max_health = health
        self.rect = self.img.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.visible = True

    def update(self, user_input):
        '''This method move the player car with user_input
        Params : boolean(user_input)
        Return : None'''
        if user_input[pygame.K_LEFT] and self.rect.x > 102:
                self.rect.x -= self.speed
        elif user_input[pygame.K_RIGHT] and self.rect.x + self.rect.width < 399:
            self.rect.x += self.speed
        elif user_input[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif user_input[pygame.K_DOWN] and self.rect.y + self.rect.height + 20 < HEIGHT:
            self.rect.y += self.speed

    def health_bar(self):
        '''Draw health bar on the screen
        Params : None
        Reuturn : None'''
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.bottomleft[1] + 10, CAR_WIDTH, 10))
        pygame.draw.rect(screen, GREEN, (self.rect.x, self.rect.bottomleft[1] + 10, CAR_WIDTH - ((CAR_WIDTH/self.max_health) * (self.max_health - self.health) ), 10))
        pygame.draw.rect(screen, BLACK, (self.rect.x, self.rect.bottomleft[1] + 10, CAR_WIDTH, 10), 2)
    
    def reduce_health(self):
        '''Reduce health if the car hit by the enemy car
        Params : None
        Return : None'''
        if self.health > 0:
            self.health -= 1

    def increase_health(self):
        '''Increase health bar if the car collects the heart
        Parmas : None
        Return : None'''
        if self.health < self.max_health:
            self.health += 1

    def draw(self):
        '''This method will draw the player car on the screen
        Params : None
        Return : None'''
        self.health_bar()
        screen.blit(self.img, (self.rect.x, self.rect.y))

class EnemyCar:
    def __init__(self, img, speed, pos_x, pos_y):
        self.img = img
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def update(self, index):
        '''This function move the car vertically with the speed
        if the car is goes off the screen then spawn another
        Params : int(index)
        Return : None'''
        self.rect.y += self.speed
        if self.rect.y > HEIGHT + self.img.get_width():
            self.remove_car_from_list(index)

    def remove_car_from_list(self, index):
        '''Remove the car from the list with the help of given index
        Params : int(index)
        Return : None'''
        global enemy_car_list
        enemy_car_list.pop(index)

    def check_collision(self, rect, index):
        '''Check for the colloision with given rect and
        remove the car from the list with the help of index
        and if collide then return true
        Params : Rect, int(index)
        Return : boolean'''
        if self.rect.colliderect(rect):
            HEALTH_LOSS_SOUND.play()
            self.remove_car_from_list(index)
            return True
        return False

    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

class Coin:
    def __init__(self, x_pos, y_pos, speed):
        self.current_img_count = 0
        self.speed = speed
        self.img = COINS[self.current_img_count]
        self.rect = self.img.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self, index):
        '''This function move the coin vertically with the given speed
        if the coin is goes off the screen then spawn another
        Params : int(index)
        Return : None'''
        self.current_img_count += 0.3
        if self.current_img_count > len(COINS):
            self.current_img_count = 0
        self.img = COINS[int(self.current_img_count)]
        self.rect.y += self.speed
        if self.rect.y > HEIGHT + self.img.get_width():
            self.remove_coin_from_list(index)

    def remove_coin_from_list(self, index):
        global coin_list
        '''Remove the coin from the list with the help of given index
        Params : int(index)
        Return : None'''
        coin_list.pop(index)

    def check_collision(self, rect, index):
        global coins_collected
        '''Check for the colloision with given rect and
        remove the coin from the list with the help of index
        and increase coins_collected
        Params : Rect, int(index)'''
        if self.rect.colliderect(rect):
            COIN_COLLECT_SOUND.play()
            coins_collected += 1
            self.remove_coin_from_list(index)

    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

class Heart:
    def __init__(self, img, speed, x_pos, y_pos):
        self.img = img
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self):
        global init_time
        '''Move the heart vertically on the screen with the given speed
        Params : None
        Return : None'''
        self.rect.y  += self.speed
        if self.rect.y > HEIGHT + self.img.get_width():
            init_time = time.time()
            self.reset_x_y_pos()

    def reset_x_y_pos(self):
        '''Reset the x and y position of the heart image
        Params : None
        Return : None'''
        self.rect.x =  random.choice([110, 190, 265, 345])
        self.rect.y = random.choice([-95, -412, -200, -615, -788, -1087])

    def check_collision(self, rect):
        global init_time
        '''Check for the colloision with given rect and
        reset the x and y position of the heart image
        and if true return true
        Params : int(index)
        Return : boolean'''
        if self.rect.colliderect(rect):
            HEART_COLLECT_SOUND.play()
            init_time = time.time()
            self.reset_x_y_pos()
            return True
        return False
            
    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))
# Some Important variable for game
enemy_car_list = []
enemy_car_speed = None
coin_list = []
coins_collected = None
init_time = None
RESPAWN_TIME = 30
def game_loop():
    '''This is the main game loop
    Params : None
    Return : None'''
    global enemy_car_speed, coins_collected, init_time
    enemy_car_speed = 3
    coins_collected = 0
    init_time = time.time()
    enemy_car_list.clear()
    coin_list.clear()
    '''This is the main game loop.
    Params : None
    Return : None'''
    run = True
    bg_posy = 0
    num, name, cost, speed, health, bought, equiped = get_player_car_data('Related_Files/MainDB.db', 'cartable')
    # instance of the PlayerCar
    car = PlayerCar(CARS_IMG[num-1], speed, health, 110, 550)
    # instance of the Heart
    car_heart = Heart(HEART_IMG, 1, random.choice([110, 190, 265, 345]), random.choice([-95, -412, -200, -615, -788, -1087]))
    while(run):
        clock.tick(FPS)
        user_input = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Add background
        screen.blit(BACKGROUND, (0, -HEIGHT + bg_posy))
        screen.blit(BACKGROUND, (0, bg_posy))   
        if bg_posy == HEIGHT:
            bg_posy = 0
        bg_posy += 1

        # Cons on top left of the screen
        draw_coin(coins_collected)
        # Add Player car)
        car.draw()
        car.update(user_input)
        # Add enemy cars
        if len(enemy_car_list) < 3:
            img = random.choice(ENEMY_CARS)
            pos_x = random.choice([110, 190, 265, 345])
            pos_y = random.choice([-85,-228, -368, -457, -651, -870, -999, -1205, -1354,-1578, -1742, -1985, -2275])
            enemy_car_list.append(EnemyCar(img, enemy_car_speed, pos_x, pos_y)) 
        for i, e_car in enumerate(enemy_car_list):
            e_car.draw()
            e_car.update(i)
            is_collide = e_car.check_collision(car.rect, i)
            if is_collide:
                car.reduce_health()

        # Add coins
        if len(coin_list) < 2:
            x_pos = random.choice([110, 190, 265, 345])
            y_pos = random.choice([-95, -412, -200, -615, -788, -1087])
            coin_list.append(Coin(x_pos, y_pos, 1))
        for i, c in enumerate(coin_list):
            c.draw()
            c.update(i)
            c.check_collision(car.rect, i)

        # Adding heart power
        if time.time() - init_time > RESPAWN_TIME:
            car_heart.draw()
            car_heart.update()
            is_collide = car_heart.check_collision(car.rect)
            if is_collide:
                enemy_car_speed += 1
                car.increase_health()
        if car.health <= 0:
            run = False
            end_loop()
        pygame.display.update()

def update_db(db, table, column, value):
    '''Update the coin table with new collected coins
    Params : String(db), String(table), String(column), int(value)
    Return : None'''
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    cur.execute(f"""UPDATE {table} SET {column} = {value}""")
    connection.commit()
    connection.close()    

def end_loop():
    '''This is the end game loop which show the result
    Params : None
    Return : None'''
    run = True
    left_click = False
    GAME_OVER_SOUND.play()
    # update coin in db
    coins_lst = fetch_all_data("Related_Files/MainDB.db", "cointable")
    total_coins = coins_lst[0][0]
    total_coins += coins_collected
    update_db('Related_Files/MainDB.db', 'cointable', 'coin_collected', total_coins)
    while run:
        clock.tick(FPS)
        m_x, m_y = pygame.mouse.get_pos()
        left_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click = True

        screen.fill(WHITE)
        screen.blit(GAME_OVER_IMG, (30, 50))
        screen.blit(CRASH_CAR_IMG, (120, 150))
        BUTTON = pygame.Rect(120, 450, 250, 90)
        if BUTTON.x + BUTTON.width > m_x > BUTTON.x and BUTTON.y + BUTTON.height > m_y > BUTTON.y:
            pygame.draw.rect(screen, RED, (BUTTON.x, BUTTON.y, 253, 93))
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
        pygame.draw.rect(screen, BLACK, BUTTON)
        screen.blit(HOME_BTN_IMG, (BUTTON.x + 15, BUTTON.y + 5))
        pygame.display.update()

if __name__ == "__main__":
    print("You can't run the game from here")