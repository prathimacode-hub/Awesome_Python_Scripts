import pyautogui
from PIL import Image, ImageGrab
import time


def autoMate(key):
    pyautogui.keyDown(key)
    return


def collision(data):
    # Check collision for birds
    for i in range(170, 210):
        for j in range(209, 374):
            if data[i, j] < 100:
                autoMate("down")
                return
    # Check collision for cactus
    for i in range(237, 275):
        for j in range(376, 440):
            if data[i, j] < 100:
                autoMate("up")
                return
    return


if __name__ == "__main__":
    print("The game is starting in 2 seconds...")
    time.sleep(2)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        collision(data)