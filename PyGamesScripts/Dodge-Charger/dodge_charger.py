from Related_Files.main_game import game_loop
from Related_Files.garage_menu import draw_coin, fetch_all_data, room_one_loop
import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# sounds
BUTTON_CLICK_SOUND = pygame.mixer.Sound("Sounds/mixkit-arcade-game-jump-coin-216.wav")
BUTTON_CLICK_SOUND.set_volume(0.3)
# fonts
NORMAL_FONT = pygame.font.SysFont("comicsansms", 15)
# setup the screen
WIDTH, HEIGHT = 500, 660
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Charger")
clock = pygame.time.Clock()
FPS = 90

# Load title image
TITLE_IMG = pygame.image.load(os.path.join("Assets/Others", "dc_logo.png"))
TITLE_IMG = pygame.transform.scale(TITLE_IMG, (450, 90))
# Load button images
PLAY_LOGO = pygame.image.load(os.path.join("Assets/Others", "play_logo.png"))
GARAGE_LOGO = pygame.image.load(os.path.join("Assets/Others", "garage_logo.png"))
QUIT_LOGO = pygame.image.load(os.path.join("Assets/Others", "quit_logo.png"))


def make_button(img ,m_x, m_y, x, y, left_click, action):
    '''Draw button on the screen and also check for click
    Params : int(m_x), int(m_y)
    Return : None'''
    BUTTON = img.get_rect()
    BUTTON.x = x
    BUTTON.y = y
    if BUTTON.x + BUTTON.width > m_x > BUTTON.x and BUTTON.y + BUTTON.height > m_y > BUTTON.y:
        # Some hover effect for fun
        pygame.draw.rect(screen, RED, (BUTTON.x, BUTTON.y, BUTTON.width, BUTTON.height))
        pygame.draw.rect(screen, BLACK, (BUTTON.x, BUTTON.y, BUTTON.width, BUTTON.height), 5)
        if left_click:
            BUTTON_CLICK_SOUND.play()
            action()
    screen.blit(img, (BUTTON.x, BUTTON.y))

def play():
    '''Call the game_loop
    Params : None
    Return : None'''
    game_loop()

def garage():
    '''Call the room_one_loop()
    Params : None
    Return : None'''
    room_one_loop()

def quit():
    '''quit the game
    Params : None
    Return : None'''
    sys.exit()

def main_loop():
    run = True
    left_click = False
    while run:
        clock.tick(FPS)
        left_click = False
        m_x, m_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click = True
        
        screen.fill(WHITE)
        coins_lst = fetch_all_data('Related_files/MainDB.db', 'cointable')
        total_coins = coins_lst[0][0]
        draw_coin(total_coins)
        screen.blit(TITLE_IMG, (30, 50))
        make_button(PLAY_LOGO, m_x, m_y, 155, 160, left_click, play)
        make_button(GARAGE_LOGO, m_x, m_y, 110, 290, left_click, garage)
        make_button(QUIT_LOGO, m_x, m_y, 160, 410, left_click, quit)

        my_name = NORMAL_FONT.render('Created by :- Mudit', 1, BLACK)
        screen.blit(my_name, (10, 590))
        note = NORMAL_FONT.render('Controls :- Arrow Keys', 1, BLACK)
        screen.blit(note, (10, 620))
        pygame.display.update()

if __name__ == "__main__":
    main_loop()