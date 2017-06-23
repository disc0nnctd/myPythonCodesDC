import pygame, random, sys
from random import choice, randrange
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

RCars = (
    "Rcar1.png",
    "Rcar2.png",
)
LCars= (
	'Lcar1.png',
	'Lcar2.png'
	)
def RCar_sel():
	RiCar=choice(RCars)
	Rcar_img = pygame.image.load(path.join(img_dir, RiCar)).convert_alpha()
	return Rcar_img
def LCar_sel():
	LeCar=choice(LCars)
	Rcar_img = pygame.image.load(path.join(img_dir, LeCar)).convert_alpha()
	return Rcar_img
# initialize pygame and create window
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road")
player_img = pygame.image.load(path.join(img_dir, "sheep.png")).convert_alpha()
#Rcar_img = pygame.image.load(path.join(img_dir, RiCar)).convert_alpha()
#Lcar_img = pygame.image.load(path.join(img_dir, "LCar1.png")).convert_alpha()
background = pygame.image.load(path.join(img_dir, 'road.png')).convert()
background_rect = background.get_rect()
clock = pygame.time.Clock()

class RCar(pygame.sprite.Sprite):
	def __init__(self, x, y, Rcar_img):
		pygame.sprite.Sprite.__init__(self)
		self.speed=1
		self.direct=1
		#self.image = pygame.Surface((30, 30))
		#self.image.fill(white)
		self.image = pygame.transform.scale(Rcar_img, (70, 40))
		self.rect = self.image.get_rect()
		self.rect.y= y
		self.rect.x= x
		self.speedx=self.speed*self.direct
	def update(self):
		self.rect.x += self.speedx

		if self.rect.x > WIDTH:
			self.rect.x = -40
		elif self.rect.x < -40:
			self.rect.x = WIDTH
class LCar(pygame.sprite.Sprite):
	def __init__(self, x, y, Lcar_img):
		pygame.sprite.Sprite.__init__(self)
		self.speed=1
		self.direct=-1
		#self.image = pygame.Surface((30, 30))
		#self.image.fill(white)
		self.image = pygame.transform.scale(Lcar_img, (70, 40))
		self.rect = self.image.get_rect()
		self.rect.y= y
		self.rect.x= x
		self.speedx=self.speed*self.direct
	def update(self):
		self.rect.x += self.speedx

		if self.rect.x > WIDTH:
			self.rect.x = -40
		elif self.rect.x < -40:
			self.rect.x = WIDTH

def create_cars():
	cars = pygame.sprite.Group()
	ys = range(150,500,55)
	x = randrange(200)
	for _ in range(3):
		car = RCar(x, ys[0],RCar_sel())
		cars.add(car)
		x += 130
	x = randrange(200)
	for _ in range(3):
		car = LCar(x, ys[1],LCar_sel())
		cars.add(car)
		x += 130
	x = randrange(200)
	for _ in range(3):
		RCar_sel()
		car = RCar(x, ys[2],RCar_sel())
		cars.add(car)
		x += 130
	x = randrange(200)
	for _ in range(3):
		car = LCar(x, ys[3],LCar_sel())
		cars.add(car)
		x += 130
	x = randrange(200)
	for _ in range(3):
		RCar_sel()
		car = RCar(x, ys[4],RCar_sel())
		cars.add(car)
		x += 130
	x=randrange(200)
	for _ in range(3):
		car = LCar(x, ys[5],LCar_sel())
		cars.add(car)
		x += 130
	for _ in range(3):
		car=RCar(x,ys[6],RCar_sel())
		cars.add(car)
		x+=140
	x=randrange(200)
	for _ in range(3):
		RCar_sel()
		car = RCar(x, ys[6],RCar_sel())
		cars.add(car)
		x += 150
	return cars
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = player_img
		#self.image = pygame.Surface((30, 40))
		#self.image.fill(green)
		self.image = pygame.transform.scale(player_img, (40, 45))
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
cars=create_cars()
final=Final()
all_sprites.add(final)
all_sprites.add(player)
all_sprites.add(cars)
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
	

	all_sprites.update()
	screen.fill(black)
	screen.blit(background, background_rect)
	all_sprites.draw(screen)

	pygame.display.flip()

pygame.quit()