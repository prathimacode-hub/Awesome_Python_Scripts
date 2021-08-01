import pygame
import random

pygame.init()
#setting the output window
white = (255, 255, 255)
myDisplay = pygame.display.set_mode((550, 550))
pygame.display.set_caption("Snow falls")
#making the circles
SnowFall= []
for i in range(150):
    x = random.randrange(0, 550)
    y = random.randrange(0, 550)
    SnowFall.append([x, y])


clock = pygame.time.Clock()
fram = False
background_position = [0, 0]
#setting the bg image
background_image = pygame.image.load("C:\\Users\\shahn\\PycharmProjects\\image_converter\\img.jpg")
while not fram:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fram = True

    myDisplay.blit(background_image, background_position)
    #moving the circles
    for n in SnowFall:
        n[1] += 1
        pygame.draw.circle(myDisplay, white, n, 4)

        if n[1] > 550:
            n[1] = random.randrange(-50, -5)
            n[0] = random.randrange(826)

    pygame.display.flip()
    #setting time for transition
    clock.tick(60)