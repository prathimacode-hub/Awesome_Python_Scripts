#importing required libraries
import os

IMAGE_SIZE = 128 #size of image
SCREEN_SIZE = 512 #size of screen
NUM_TILES_SIDE = 4 #number of tiles sides
NUM_TILES_TOTAL = 16 #number of tiles in toltal
MARGIN = 8 #margin

ASSET_DIR = 'assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
assert len(ASSET_FILES) == 8
