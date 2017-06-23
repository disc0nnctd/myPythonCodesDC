import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

# initialize pygame and create window
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road")
clock = pygame.time.Clock()
listy=[200,300,400,500] #y-postions, where the cars should spawn
class Car(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30, 30))
		self.image.fill(white)
		self.rect = self.image.get_rect()
		self.speed=random.randint(1,4)
		self.rect.y = random.choice(listy)
		self.speedy = 0
		if self.rect.y%2==0:
			self.rect.x = 0
			self.speedx = self.speed*1
		else:
			self.rect.x = WIDTH-10
			self.speedx=self.speed*-1

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.left < -25 or self.rect.right > WIDTH + 20:
			self.kill()


class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30, 40))
		self.image.fill(green)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.bottom = HEIGHT - 10
		self.speedx = 0
		self.speedy = 0
	def update(self):
		self.speedx = 0
		self.speedy = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -8
		if keystate[pygame.K_RIGHT]:
			self.speedx = 8
		if keystate[pygame.K_UP]:
			self.speedy = -8
		if keystate[pygame.K_DOWN]:
			self.speedy = 8
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT
		if self.rect.top < 0:
			self.rect.top = 0

class Final(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 40))
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.rect.centerx = random.randint(10,WIDTH-10)
		self.rect.y = 20
all_sprites = pygame.sprite.Group()
player = Player()
cars = pygame.sprite.Group()
final=Final()
all_sprites.add(final)
all_sprites.add(player)
for i in range(5):
    m = Car()
    all_sprites.add(m)
    cars.add(m)
	
running = True
while running:

	clock.tick(FPS)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False
	hits = pygame.sprite.spritecollide(player, cars, False)
	if hits:
		player.rect.centerx = WIDTH / 2
		player.rect.bottom = HEIGHT - 10

	
	fin=pygame.sprite.collide_rect(player,final)
	if fin:
		running=False
		print "You Win!"
	

	m = Car()
	all_sprites.add(m)
	cars.add(m)

	all_sprites.update()
	screen.fill(black)
	all_sprites.draw(screen)

	pygame.display.flip()

pygame.quit()