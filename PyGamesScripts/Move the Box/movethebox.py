import pygame

# Initializing Pygame
pygame.init()
red=(0,255,255)
black=(0,0,0)
# Initializing surface

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Move the Box")
clock=pygame.time.Clock()

#we are adding the sprites now
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill(black)
        self.rect=self.image.get_rect()

        self.rect.center=(100,100)
        self.speedx=0
        self.speedy=0

    def update(self):
        self.speedx=0
        self.speedy=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx=-5
        if keystate[pygame.K_RIGHT]:
            self.speedx=5
        if keystate[pygame.K_UP]:
            self.speedy=-5
        if keystate[pygame.K_DOWN]:
            self.speedy=5
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy



all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)

running=True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    all_sprites.update()
    screen.fill(red)
    all_sprites.draw(screen)

    pygame.display.flip()
pygame.quit()
