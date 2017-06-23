import pygame
import random
from random import choice, randrange
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

class MovingObstacle(pygame.sprite.Sprite):
	"Base class for all moving obstacles"
	def __init__(self, x, y, direction):
		super(MovingObstacle, self).__init__()
		self.speed = 2
		self.go_left = direction
		self.img = pygame.Surface((30, 30))
		self.img.fill(white)
		self.rect = self.img.get_rect()
		self.rect.x = x
		self.rect.y = y

	def draw(self):
		"Moves and then draws the obstacle"
		# Adjust the position of the obstacle.
		if self.go_left:
			self.rect.x -= self.speed
		else:
			self.rect.x += self.speed
		# Reset the object if it moves out of screen.
		if isinstance(self, Car):
			if self.rect.x > 480:
				self.rect.x = -40
			elif self.rect.x < -40:
				self.rect.x = 480
class Car(MovingObstacle):

	def __init__(self, x, y, direction=0):
		super(Car, self).__init__(x, y, direction)

def create_hostiles():
	"Create the obstacles that trigger death on collision"
	hostiles = pygame.sprite.Group()
	ys = [520, 480, 440, 400, 360]
	x = randrange(200)
	for _ in range(3):
		car = Car(x, ys[0], 1)
		hostiles.add(car)
		x += 144
	x = randrange(200)
	for _ in range(3):
		car = Car(x, ys[1])
		hostiles.add(car)
		x += 128
	x = randrange(200)
	for _ in range(3):
		car = Car(x, ys[2],1)
		hostiles.add(car)
		x += 128
	x = randrange(200)
	for _ in range(2):
		car = Car(x, ys[3])
		hostiles.add(car)
		x += 128
	x = randrange(200)
	for _ in range(2):
		car = Car(x, ys[4],1)
		hostiles.add(car)
		x += 176

	return hostiles

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
hostiles = create_hostiles()
final=Final()
all_sprites.add(final)
all_sprites.add(player)
clock = pygame.time.Clock()
running = True
while running:

	clock.tick(FPS)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False
	hits = pygame.sprite.spritecollide(player, hostiles, False)
	if hits:
		player.rect.centerx = WIDTH / 2
		player.rect.bottom = HEIGHT - 10
	
	fin=pygame.sprite.collide_rect(player,final)
	if fin:
		running=False
		print "You Win!"
	

	all_sprites.update()
	screen.fill(black)
	all_sprites.draw(screen)

	pygame.display.flip()

pygame.quit()