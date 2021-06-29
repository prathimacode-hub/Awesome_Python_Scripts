import pygame
import sys
import sqlite3
import os
import ctypes

pygame.init()
pygame.mixer.init()
# colors
WHITE = (255, 255, 255)
REDISH = (248, 80, 10)
BLACK = (0, 0, 0)
BLUISH = (78, 144, 255)
# setup the screen
WIDTH, HEIGHT = 500, 660
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Charger")
clock = pygame.time.Clock()
FPS = 90
# sounds
BUTTON_CLICK_SOUND = pygame.mixer.Sound("Sounds/mixkit-arcade-game-jump-coin-216.wav")
BUTTON_CLICK_SOUND.set_volume(0.3)
MESSAGE_SOUND = pygame.mixer.Sound("Sounds/mixkit-quick-win-video-game-notification-269.wav")
APPLAUSE_SOUND = pygame.mixer.Sound("Sounds/mixkit-girls-audience-applause-510.wav")
APPLAUSE_SOUND.set_volume(0.3)
MESSAGE_SOUND.set_volume(0.1)
# fonts 
VEHICLE_FONT = pygame.font.SysFont("comicsansms", 45)
COIN_FONT = pygame.font.SysFont("comicsansms", 21)
# Load images of vehicles
IMG_WIDTH, IMG_HEIGHT = 150, 250
VEHICLES_LIST = []
for i in range(8):
    img = pygame.image.load(os.path.join("Assets/Vehicles", f"vehicle{i}.png"))
    img = pygame.transform.scale(img, (IMG_WIDTH, IMG_HEIGHT))
    img = pygame.transform.rotate(img, 90)
    VEHICLES_LIST.append(img)
# Load imgaes of buttons
BUTTTON_LIST = []
for i in range(4):
    btn = pygame.image.load(os.path.join("Assets/Buttons", f"button{i}.png"))
    btn = pygame.transform.scale(btn, (180, 84))
    BUTTTON_LIST.append(btn)
# Arrow buttons
NEXT_ARROW_BTN = pygame.image.load(os.path.join("Assets/Buttons/Arrows", "arrow0.png"))
NEXT_ARROW_BTN = pygame.transform.scale(NEXT_ARROW_BTN, (48, 48))

PREV_ARROW_BTN = pygame.transform.rotate(NEXT_ARROW_BTN, 180)

BACK_BUTTON = pygame.image.load(os.path.join("Assets/Buttons/Arrows", "arrow1.png"))
BACK_BUTTON = pygame.transform.scale(BACK_BUTTON, (38, 28))
BACK_BUTTON = pygame.transform.rotate(BACK_BUTTON, 180)
# Load images of cons
COINS = []
for i in range(10):
    coin = pygame.image.load(os.path.join("Assets/Coins", f"coin{i}.png"))
    coin = pygame.transform.scale(coin, (32, 32))
    COINS.append(coin)
# Database
def fetch_all_data(db, table):
    '''Used to fetch all the data from the given table
    in the database.
    Params : String(database name), String(table name)
    Return : list of tuples'''
    connection = sqlite3.connect(db)
    cur = connection.cursor()

    lst = []
    for row in cur.execute(f'SELECT * FROM {table}'):
        lst.append(row)
    connection.close()
    return lst
 
def get_data_of_car(lst, tuple_inedex):
    '''Give details of car from the list of tuples
    Parmas : list(list of tuple), int(tuple index)
    Retrun : tuple'''
    return lst[tuple_inedex]

class Vehicles:
    def __init__(self, img, row_num, name, cost, speed, health, bought, equipped):
        self.img = img
        self.row_num = row_num
        self.name = name
        self.cost = cost
        self.speed = speed
        self.health = health
        self.bought = bought
        self.equpped = equipped

    def draw_vehicle(self):
        '''Draw car image on the screen with all its properties
        Params : None
        Return : None'''
        screen.blit(self.img, (120, 70))

        name = VEHICLE_FONT.render(self.name, 1, REDISH)
        screen.blit(name, (100, 240))

        cost = VEHICLE_FONT.render('Cost : '+str(self.cost)+' coins', 1, REDISH)
        screen.blit(cost, (100, 320))

        speed = VEHICLE_FONT.render('Speed : '+str(self.speed)+' km/h', 1, REDISH)
        screen.blit(speed, (100, 400))

        health = VEHICLE_FONT.render('Health : '+str(self.health)+' beats', 1, REDISH)
        screen.blit(health, (100, 480))

    def buy_bought_button(self, btn_index, m_x, m_y, left_click, total_coins):
        '''Draw buy button on the screen if the car is not bought and
        draw bought button if the car is bought.
        Params : int(button_ndex), int(mouse x position), int(mouse y positon) 
        boolean(left_click), int(total_coins)
        Return : None'''
        BUTTON = pygame.Rect(20, 560, 180, 84)
        if BUTTON.x + BUTTON.width > m_x > BUTTON.x and BUTTON.y + BUTTON.height > m_y > BUTTON.y:
            # Some hover effect for fun
            pygame.draw.rect(screen, BLACK, (BUTTON.x, BUTTON.y, 183, 87))
            # check if the button is a buy button !bought button and button is click
            if btn_index == 0 and left_click == True:
                BUTTON_CLICK_SOUND.play()
                self.buy(total_coins)

        pygame.draw.rect(screen, REDISH, BUTTON)
        screen.blit(BUTTTON_LIST[btn_index], (BUTTON.x, BUTTON.y))

    def equip_unequip_button(self, btn_index, m_x, m_y, left_click):
        '''Draw equip button on the screen if the car is bought and 
        unequip button if the car is equipped
        Params : None
        Return : None'''
        BUTTON = pygame.Rect(300, 560, 180, 84)
        if BUTTON.x + BUTTON.width > m_x > BUTTON.x and BUTTON.y + BUTTON.height > m_y > BUTTON.y:
            # Some hover effect for fun
            pygame.draw.rect(screen, BLACK, (BUTTON.x, BUTTON.y, 183, 87))
            # Check if the button is equip button or unequip and if it is click
            if btn_index == 2 and left_click == True:
                BUTTON_CLICK_SOUND.play()
                self.equip('Related_Files/MainDb.db', 'cartable', 'is_equiped', self.row_num)
            elif btn_index == 3 and left_click == True:
                BUTTON_CLICK_SOUND.play()
                self.unequip('Related_Files/MainDb.db', 'cartable', 'is_equiped', self.row_num)
        pygame.draw.rect(screen, BLUISH, BUTTON)
        screen.blit(BUTTTON_LIST[btn_index], (BUTTON.x, BUTTON.y))

    def update_database_for_buy(self, database, table1, table2, row_num, column1, column2, value1, value2):
        '''This function updates the data of the given database tables
        Params : String(database), Sring(table), Sring(table), int(row_num), String(column1)
        String(column2), int(value1), boolean(value2) 
        Return : None'''
        connection = sqlite3.connect(database)
        cur = connection.cursor()
        # update data of coin table
        cur.execute(f"""UPDATE {table1} SET {column1} = {value1}""")
        # update data of car table
        cur.execute(f"""UPDATE {table2} SET {column2} = {value2} WHERE row_id = {row_num}""")
        connection.commit()
        connection.close()

    def buy(self,total_coins):
        '''It is use to buy the car only if there is sufficient coin
        Params : int(total coins)
        Return : None
        '''
        if total_coins >= self.cost and self.bought !=1:
            APPLAUSE_SOUND.play()
            self.update_database_for_buy('Related_Files/MainDB.db', 'cointable', 'cartable', self.row_num, 'coin_collected', 'is_purchased', total_coins-self.cost, 1)
        else:
            MESSAGE_SOUND.play()
            ctypes.windll.user32.MessageBoxW(0, "Insufficient coins!!", "Message", 0)
    
    def equip(self, db, table, column, row_num):
        '''This function set is_equiped = 1 in given table
        Params : String(db), String(table), String(column), int(row_num)
        Return : None'''
        connection = sqlite3.connect(db)
        cur = connection.cursor()
        # Set is_equpeed = 1 in cartable where row_id == row_num
        cur.execute(f"""UPDATE {table} SET {column} = 1 WHERE row_id = {row_num}""")
        # Set is_equipeed = 0 in cartable where row_id != row_num
        cur.execute(f"""UPDATE {table} SET {column} = 0 WHERE row_id != {row_num}""")

        connection.commit()
        connection.close()

    def unequip(self, db, table, column, row_num):
        '''This function set is_equiped = 0 in given table
        Params : String(db), Sring(table), String(colulm), int(row_num)
        Return : None'''
        connection = sqlite3.connect(db)
        cur = connection.cursor()
        # set is_equiped = 0 in cartable
        cur.execute(f"""UPDATE {table} SET {column} = 0 WHERE row_id = {row_num}""")
        connection.commit()
        # If all car is unequip then equip suzuki by default
        data = fetch_all_data(db, table)
        if data[0][6] == 0 and data[1][6] == 0 and data[2][6] == 0 and data[3][6] == 0 and data[4][6] == 0 and data[5][6] == 0 and data[6][6] == 0 and data[7][6] == 0:
            cur.execute(f"""UPDATE {table} SET {column} = 1 WHERE row_id = 1""")
        
        connection.commit()
        connection.close()
       

def next_button():
    '''Draw next button on the screen. It is use for change
    between different cars.
    Params : None
    Return : tuple(Rect)'''
    screen.blit(NEXT_ARROW_BTN, (440, 330))
    return pygame.Rect(440, 330, NEXT_ARROW_BTN.get_width(), NEXT_ARROW_BTN.get_height())

def prev_button():
    '''Draw prev button on the screen. It is use for change
    between different cars.
    Params : None
    Return : tuple(Rect)'''
    screen.blit(PREV_ARROW_BTN, (10, 330))
    return pygame.Rect(10, 330, PREV_ARROW_BTN.get_width(), PREV_ARROW_BTN.get_height())

def back_button():
    '''Draw back button on the screen.
    Params : None
    Return : tuple(Rect)'''
    screen.blit(BACK_BUTTON, (430, 15))
    return pygame.Rect(430, 15, BACK_BUTTON.get_width(), BACK_BUTTON.get_height())

def draw_coin(total_coins):
    '''Draw coin image and total coin from database on the 
    top left of the screen
    Parma : int(total_coins)
    Return : None'''
    screen.blit(COINS[0], (10, 10))
    text = COIN_FONT.render(str(total_coins), 1, BLACK)
    screen.blit(text, (50, 10))

def room_one_loop():
    '''This loop display the first vechicle out of eight with
    all of its properties and behaviors
    Params : None
    Return : None'''
    run = True
    left_click = False
    while run:
        # instance of Vehicles class
        lst = fetch_all_data('Related_Files/MainDB.db', 'cartable')
        coin_lst = fetch_all_data('Related_Files/MainDB.db', 'cointable')
        total_coins = coin_lst[0][0]
        num, name, cost, speed, health, bought, equipped =  get_data_of_car(lst, 0)
        suzuki = Vehicles(VEHICLES_LIST[0], num, name, cost, speed, health, bought, equipped)
        clock.tick(FPS)
        left_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click = True
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill(WHITE)
        # Total coins
        draw_coin(total_coins)
        # Arrow Buttons
        BACK_ARROW_BTN_RECT = back_button()
        PREV_ARROW_BTN_RECT = prev_button()
        NEXT_ARROW_BTN_RECT = next_button()
        suzuki.draw_vehicle()
        # Check for, which button to draw buy/bought?
        if bought != 1:
            suzuki.buy_bought_button(0, m_x, m_y, left_click, total_coins)
        else:
            suzuki.buy_bought_button(1, m_x, m_y, left_click, total_coins)
        # Check for, which button to draw equip/unequip?
        if bought == 1 and equipped != 1:
            suzuki.equip_unequip_button(2, m_x, m_y, left_click)
        if bought == 1 and equipped == 1:
            suzuki.equip_unequip_button(3, m_x, m_y, left_click)
        # Check if prev arrow button is click
        if BACK_ARROW_BTN_RECT.x + BACK_ARROW_BTN_RECT.width > m_x > BACK_ARROW_BTN_RECT.x and BACK_ARROW_BTN_RECT.y + BACK_ARROW_BTN_RECT.height > m_y > BACK_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
        if PREV_ARROW_BTN_RECT.x + PREV_ARROW_BTN_RECT.width > m_x > PREV_ARROW_BTN_RECT.x and PREV_ARROW_BTN_RECT.y + PREV_ARROW_BTN_RECT.height > m_y > PREV_ARROW_BTN_RECT.y:
           if left_click:
               BUTTON_CLICK_SOUND.play()
               pass
        # Check if next arrow button is click
        if NEXT_ARROW_BTN_RECT.x + NEXT_ARROW_BTN_RECT.width > m_x > NEXT_ARROW_BTN_RECT.x and NEXT_ARROW_BTN_RECT.y + NEXT_ARROW_BTN_RECT.height > m_y > NEXT_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_two_loop()
        pygame.display.update()

def room_two_loop():
    '''This loop display the second vechicle out of eight with
    all of its properties and behaviors
    Params : None
    Return : None'''
    run = True
    left_click = False
    while run:
        # instance of Vehicles class
        lst = fetch_all_data('Related_Files/MainDB.db', 'cartable')
        coin_lst = fetch_all_data('Related_Files/MainDB.db', 'cointable')
        total_coins = coin_lst[0][0]
        num, name, cost, speed, health, bought, equipped =  get_data_of_car(lst, 1)
        mini_truck = Vehicles(VEHICLES_LIST[1], num, name, cost, speed, health, bought, equipped)
        clock.tick(FPS)
        left_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click = True
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill(WHITE)
         # Total coins
        draw_coin(total_coins)
        # Arrow Buttons
        BACK_ARROW_BTN_RECT = back_button()
        PREV_ARROW_BTN_RECT = prev_button()
        NEXT_ARROW_BTN_RECT = next_button()
        mini_truck.draw_vehicle()
        # Check for, which button to draw buy/bought?
        if bought != 1:
            mini_truck.buy_bought_button(0, m_x, m_y, left_click, total_coins)
        else:
            mini_truck.buy_bought_button(1, m_x, m_y, left_click, total_coins)
        # Check for, which button to draw equip/unequip?
        if bought == 1 and equipped != 1:
            mini_truck.equip_unequip_button(2, m_x, m_y, left_click)
        if bought == 1 and equipped == 1:
            mini_truck.equip_unequip_button(3, m_x, m_y, left_click)
        # Check if prev arrow button is click
        if BACK_ARROW_BTN_RECT.x + BACK_ARROW_BTN_RECT.width > m_x > BACK_ARROW_BTN_RECT.x and BACK_ARROW_BTN_RECT.y + BACK_ARROW_BTN_RECT.height > m_y > BACK_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
        if PREV_ARROW_BTN_RECT.x + PREV_ARROW_BTN_RECT.width > m_x > PREV_ARROW_BTN_RECT.x and PREV_ARROW_BTN_RECT.y + PREV_ARROW_BTN_RECT.height > m_y > PREV_ARROW_BTN_RECT.y:
           if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_one_loop()
        # Check if next arrow button is click
        if NEXT_ARROW_BTN_RECT.x + NEXT_ARROW_BTN_RECT.width > m_x > NEXT_ARROW_BTN_RECT.x and NEXT_ARROW_BTN_RECT.y + NEXT_ARROW_BTN_RECT.height > m_y > NEXT_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_three_loop()
        
        pygame.display.update()
        
def room_three_loop():
    '''This loop display the third vechicle out of eight with
    all of its properties and behaviors
    Params : None
    Return : None'''
    run = True
    left_click = False
    while run:
        # instance of Vehicles class
        lst = fetch_all_data('Related_Files/MainDB.db', 'cartable')
        coin_lst = fetch_all_data('Related_Files/MainDB.db', 'cointable')
        total_coins = coin_lst[0][0]
        num, name, cost, speed, health, bought, equipped =  get_data_of_car(lst, 2)
        taxi = Vehicles(VEHICLES_LIST[2], num, name, cost, speed, health, bought, equipped)
        clock.tick(FPS)
        left_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click = True
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill(WHITE)
         # Total coins
        draw_coin(total_coins)
        # Arrow Button
        BACK_ARROW_BTN_RECT = back_button()
        PREV_ARROW_BTN_RECT = prev_button()
        NEXT_ARROW_BTN_RECT = next_button()
        taxi.draw_vehicle()
        # Check if prev arrow button is click
        if BACK_ARROW_BTN_RECT.x + BACK_ARROW_BTN_RECT.width > m_x > BACK_ARROW_BTN_RECT.x and BACK_ARROW_BTN_RECT.y + BACK_ARROW_BTN_RECT.height > m_y > BACK_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
        if PREV_ARROW_BTN_RECT.x + PREV_ARROW_BTN_RECT.width > m_x > PREV_ARROW_BTN_RECT.x and PREV_ARROW_BTN_RECT.y + PREV_ARROW_BTN_RECT.height > m_y > PREV_ARROW_BTN_RECT.y:
           if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_two_loop()
        # Check if next arrow button is click
        if NEXT_ARROW_BTN_RECT.x + NEXT_ARROW_BTN_RECT.width > m_x > NEXT_ARROW_BTN_RECT.x and NEXT_ARROW_BTN_RECT.y + NEXT_ARROW_BTN_RECT.height > m_y > NEXT_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_four_loop()
        # Check for, which button to draw buy/bought?
        if bought != 1:
            taxi.buy_bought_button(0, m_x, m_y, left_click, total_coins)
        else:
            taxi.buy_bought_button(1, m_x, m_y, left_click, total_coins)
        # Check for, which button to draw equip/unequip?
        if bought == 1 and equipped != 1:
            taxi.equip_unequip_button(2, m_x, m_y, left_click)
        if bought == 1 and equipped == 1:
            taxi.equip_unequip_button(3, m_x, m_y, left_click)

        pygame.display.update()

def room_four_loop():
    '''This loop display the fourth vechicle out of eight with
    all of its properties and behaviors
    Params : None
    Return : None'''
    run = True
    left_click = False
    while run:
        # instance of Vehicles class
        lst = fetch_all_data('Related_Files/MainDB.db', 'cartable')
        coin_lst = fetch_all_data('Related_Files/MainDB.db', 'cointable')
        total_coins = coin_lst[0][0]
        num, name, cost, speed, health, bought, equipped =  get_data_of_car(lst, 3)
        ambulance = Vehicles(VEHICLES_LIST[3], num, name, cost, speed, health, bought, equipped)
        clock.tick(FPS)
        left_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click = True
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill(WHITE)
         # Total coins
        draw_coin(total_coins)
        # Arrow Buttons
        BACK_ARROW_BTN_RECT = back_button()
        PREV_ARROW_BTN_RECT = prev_button()
        NEXT_ARROW_BTN_RECT = next_button()
        ambulance.draw_vehicle()
        # Check for, which button to draw buy/bought?
        if bought != 1:
            ambulance.buy_bought_button(0, m_x, m_y, left_click, total_coins)
        else:
            ambulance.buy_bought_button(1, m_x, m_y, left_click, total_coins)
        # Check for, which button to draw equip/unequip?
        if bought == 1 and equipped != 1:
            ambulance.equip_unequip_button(2, m_x, m_y, left_click)
        if bought == 1 and equipped == 1:
            ambulance.equip_unequip_button(3, m_x, m_y, left_click)
        # Check if prev arrow button is click
        if BACK_ARROW_BTN_RECT.x + BACK_ARROW_BTN_RECT.width > m_x > BACK_ARROW_BTN_RECT.x and BACK_ARROW_BTN_RECT.y + BACK_ARROW_BTN_RECT.height > m_y > BACK_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
        if PREV_ARROW_BTN_RECT.x + PREV_ARROW_BTN_RECT.width > m_x > PREV_ARROW_BTN_RECT.x and PREV_ARROW_BTN_RECT.y + PREV_ARROW_BTN_RECT.height > m_y > PREV_ARROW_BTN_RECT.y:
           if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_three_loop()
        # Check if next arrow button is click
        if NEXT_ARROW_BTN_RECT.x + NEXT_ARROW_BTN_RECT.width > m_x > NEXT_ARROW_BTN_RECT.x and NEXT_ARROW_BTN_RECT.y + NEXT_ARROW_BTN_RECT.height > m_y > NEXT_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_five_loop()
        
        pygame.display.update()

def room_five_loop():
    '''This loop display the fifth vechicle out of eight with
    all of its properties and behaviors
    Params : None
    Return : None'''
    run = True
    left_click = False
    while run:
        # instance of Vehicles class
        lst = fetch_all_data('Related_Files/MainDB.db', 'cartable')
        coin_lst = fetch_all_data('Related_Files/MainDB.db', 'cointable')
        total_coins = coin_lst[0][0]
        num, name, cost, speed, health, bought, equipped =  get_data_of_car(lst, 4)
        taxi = Vehicles(VEHICLES_LIST[4], num, name, cost, speed, health, bought, equipped)
        clock.tick(FPS)
        left_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click = True
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill(WHITE)
         # Total coins
        draw_coin(total_coins)
        # Arrow Buttons
        BACK_ARROW_BTN_RECT = back_button()
        PREV_ARROW_BTN_RECT = prev_button()
        NEXT_ARROW_BTN_RECT = next_button()
        taxi.draw_vehicle()
        # Check for, which button to draw buy/bought?
        if bought != 1:
            taxi.buy_bought_button(0, m_x, m_y, left_click, total_coins)
        else:
            taxi.buy_bought_button(1, m_x, m_y, left_click, total_coins)
        # Check for, which button to draw equip/unequip?
        if bought == 1 and equipped != 1:
            taxi.equip_unequip_button(2, m_x, m_y, left_click)
        if bought == 1 and equipped == 1:
            taxi.equip_unequip_button(3, m_x, m_y, left_click)
        # Check if prev arrow button is click
        if BACK_ARROW_BTN_RECT.x + BACK_ARROW_BTN_RECT.width > m_x > BACK_ARROW_BTN_RECT.x and BACK_ARROW_BTN_RECT.y + BACK_ARROW_BTN_RECT.height > m_y > BACK_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
        if PREV_ARROW_BTN_RECT.x + PREV_ARROW_BTN_RECT.width > m_x > PREV_ARROW_BTN_RECT.x and PREV_ARROW_BTN_RECT.y + PREV_ARROW_BTN_RECT.height > m_y > PREV_ARROW_BTN_RECT.y:
           if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_three_loop()
        # Check if next arrow button is click
        if NEXT_ARROW_BTN_RECT.x + NEXT_ARROW_BTN_RECT.width > m_x > NEXT_ARROW_BTN_RECT.x and NEXT_ARROW_BTN_RECT.y + NEXT_ARROW_BTN_RECT.height > m_y > NEXT_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_six_loop()
        
        pygame.display.update()

def room_six_loop():
    '''This loop display the sexth vechicle out of eight with
    all of its properties and behaviors
    Params : None
    Return : None'''
    run = True
    left_click = False
    while run:
        # instance of Vehicles class
        lst = fetch_all_data('Related_Files/MainDB.db', 'cartable')
        coin_lst = fetch_all_data('Related_Files/MainDB.db', 'cointable')
        total_coins = coin_lst[0][0]
        num, name, cost, speed, health, bought, equipped =  get_data_of_car(lst, 5)
        taxi = Vehicles(VEHICLES_LIST[5], num, name, cost, speed, health, bought, equipped)
        clock.tick(FPS)
        left_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click = True
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill(WHITE)
         # Total coins
        draw_coin(total_coins)
        # Arrow Buttons
        BACK_ARROW_BTN_RECT = back_button()
        PREV_ARROW_BTN_RECT = prev_button()
        NEXT_ARROW_BTN_RECT = next_button()
        taxi.draw_vehicle()
        # Check for, which button to draw buy/bought?
        if bought != 1:
            taxi.buy_bought_button(0, m_x, m_y, left_click, total_coins)
        else:
            taxi.buy_bought_button(1, m_x, m_y, left_click, total_coins)
        # Check for, which button to draw equip/unequip?
        if bought == 1 and equipped != 1:
            taxi.equip_unequip_button(2, m_x, m_y, left_click)
        if bought == 1 and equipped == 1:
            taxi.equip_unequip_button(3, m_x, m_y, left_click)
        # Check if prev arrow button is click
        if BACK_ARROW_BTN_RECT.x + BACK_ARROW_BTN_RECT.width > m_x > BACK_ARROW_BTN_RECT.x and BACK_ARROW_BTN_RECT.y + BACK_ARROW_BTN_RECT.height > m_y > BACK_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
        if PREV_ARROW_BTN_RECT.x + PREV_ARROW_BTN_RECT.width > m_x > PREV_ARROW_BTN_RECT.x and PREV_ARROW_BTN_RECT.y + PREV_ARROW_BTN_RECT.height > m_y > PREV_ARROW_BTN_RECT.y:
           if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_five_loop()
        # Check if next arrow button is click
        if NEXT_ARROW_BTN_RECT.x + NEXT_ARROW_BTN_RECT.width > m_x > NEXT_ARROW_BTN_RECT.x and NEXT_ARROW_BTN_RECT.y + NEXT_ARROW_BTN_RECT.height > m_y > NEXT_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_seven_loop()
        
        pygame.display.update()

def room_seven_loop():
    '''This loop display the seventh vechicle out of eight with
    all of its properties and behaviors
    Params : None
    Return : None'''
    run = True
    left_click = False
    while run:
        # instance of Vehicles class
        lst = fetch_all_data('Related_Files/MainDB.db', 'cartable')
        coin_lst = fetch_all_data('Related_Files/MainDB.db', 'cointable')
        total_coins = coin_lst[0][0]
        num, name, cost, speed, health, bought, equipped =  get_data_of_car(lst, 6)
        taxi = Vehicles(VEHICLES_LIST[6], num, name, cost, speed, health, bought, equipped)
        clock.tick(FPS)
        left_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click = True
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill(WHITE)
         # Total coins
        draw_coin(total_coins)
        # Arrow Buttons
        BACK_ARROW_BTN_RECT = back_button()
        PREV_ARROW_BTN_RECT = prev_button()
        NEXT_ARROW_BTN_RECT = next_button()
        taxi.draw_vehicle()
        # Check for, which button to draw buy/bought?
        if bought != 1:
            taxi.buy_bought_button(0, m_x, m_y, left_click, total_coins)
        else:
            taxi.buy_bought_button(1, m_x, m_y, left_click, total_coins)
        # Check for, which button to draw equip/unequip?
        if bought == 1 and equipped != 1:
            taxi.equip_unequip_button(2, m_x, m_y, left_click)
        if bought == 1 and equipped == 1:
            taxi.equip_unequip_button(3, m_x, m_y, left_click)
        # Check if prev arrow button is click
        if BACK_ARROW_BTN_RECT.x + BACK_ARROW_BTN_RECT.width > m_x > BACK_ARROW_BTN_RECT.x and BACK_ARROW_BTN_RECT.y + BACK_ARROW_BTN_RECT.height > m_y > BACK_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
        if PREV_ARROW_BTN_RECT.x + PREV_ARROW_BTN_RECT.width > m_x > PREV_ARROW_BTN_RECT.x and PREV_ARROW_BTN_RECT.y + PREV_ARROW_BTN_RECT.height > m_y > PREV_ARROW_BTN_RECT.y:
           if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_six_loop()
        # Check if next arrow button is click
        if NEXT_ARROW_BTN_RECT.x + NEXT_ARROW_BTN_RECT.width > m_x > NEXT_ARROW_BTN_RECT.x and NEXT_ARROW_BTN_RECT.y + NEXT_ARROW_BTN_RECT.height > m_y > NEXT_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_eight_loop()
        
        pygame.display.update()

def room_eight_loop():
    '''This loop display the eight vechicle out of eight with
    all of its properties and behaviors
    Params : None
    Return : None'''
    run = True
    left_click = False
    while run:
        # instance of Vehicles class
        lst = fetch_all_data('Related_Files/MainDB.db', 'cartable')
        coin_lst = fetch_all_data('Related_Files/MainDB.db', 'cointable')
        total_coins = coin_lst[0][0]
        num, name, cost, speed, health, bought, equipped =  get_data_of_car(lst, 7)
        taxi = Vehicles(VEHICLES_LIST[7], num, name, cost, speed, health, bought, equipped)
        clock.tick(FPS)
        left_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click = True
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill(WHITE)
         # Total coins
        draw_coin(total_coins)
        # Arrow Buttons
        BACK_ARROW_BTN_RECT = back_button()
        PREV_ARROW_BTN_RECT = prev_button()
        NEXT_ARROW_BTN_RECT = next_button()
        taxi.draw_vehicle()
        # Check for, which button to draw buy/bought?
        if bought != 1:
            taxi.buy_bought_button(0, m_x, m_y, left_click, total_coins)
        else:
            taxi.buy_bought_button(1, m_x, m_y, left_click, total_coins)
        # Check for, which button to draw equip/unequip?
        if bought == 1 and equipped != 1:
            taxi.equip_unequip_button(2, m_x, m_y, left_click)
        if bought == 1 and equipped == 1:
            taxi.equip_unequip_button(3, m_x, m_y, left_click)
        # Check if prev arrow button is click
        if BACK_ARROW_BTN_RECT.x + BACK_ARROW_BTN_RECT.width > m_x > BACK_ARROW_BTN_RECT.x and BACK_ARROW_BTN_RECT.y + BACK_ARROW_BTN_RECT.height > m_y > BACK_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
        if PREV_ARROW_BTN_RECT.x + PREV_ARROW_BTN_RECT.width > m_x > PREV_ARROW_BTN_RECT.x and PREV_ARROW_BTN_RECT.y + PREV_ARROW_BTN_RECT.height > m_y > PREV_ARROW_BTN_RECT.y:
           if left_click:
                BUTTON_CLICK_SOUND.play()
                run = False
                room_seven_loop()
        # Check if next arrow button is click
        if NEXT_ARROW_BTN_RECT.x + NEXT_ARROW_BTN_RECT.width > m_x > NEXT_ARROW_BTN_RECT.x and NEXT_ARROW_BTN_RECT.y + NEXT_ARROW_BTN_RECT.height > m_y > NEXT_ARROW_BTN_RECT.y:
            if left_click:
                BUTTON_CLICK_SOUND.play()
                pass
        
        pygame.display.update()
if __name__ == "__main__":
    print("You can't run the game from here")