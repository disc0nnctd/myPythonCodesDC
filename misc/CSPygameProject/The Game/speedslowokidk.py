import pygame, random, sys
from random import choice, randrange
from os import path
img_dir = path.join(path.dirname('__file__'), 'sprites')

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
    "RCar1.png",
    "RCar2.png",
    "RCar3.png"
	)
LCars= (
	"LCar1.png",
	"LCar2.png",
        "LCar3.png"
	)
def RCar_sel():
	RiCar=choice(RCars)
	Rcar_img = pygame.image.load(path.join(img_dir, RiCar)).convert_alpha()
	return Rcar_img
def LCar_sel():
	LeCar=choice(LCars)
	Rcar_img = pygame.image.load(path.join(img_dir, LeCar)).convert_alpha()
	return Rcar_img

class Car(pygame.sprite.Sprite):
	def __init__(self, x, y, direction):
		pygame.sprite.Sprite.__init__(self)
		self.speed=1
		self.direct=direction
		if self.direct==1:
			im=RCar_sel()
		elif self.direct==-1:
			im=LCar_sel()
		self.image = pygame.transform.scale(im, (70, 40))
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
		car = Car(x, ys[0],1)
		cars.add(car)
		x += 130
	x = randrange(200)
	for _ in range(3):
		car = Car(x, ys[1],-1)
		cars.add(car)
		x += 160
	x = randrange(200)
	for _ in range(3):
		RCar_sel()
		car = Car(x, ys[2],1)
		cars.add(car)
		x += 110
	x = randrange(200)
	for _ in range(3):
		car = Car(x, ys[3],-1)
		cars.add(car)
		x += 190
	x = randrange(200)
	for _ in range(3):
		RCar_sel()
		car = Car(x, ys[4],1)
		cars.add(car)
		x += 125
	x=randrange(200)
	for _ in range(3):
		car = Car(x, ys[5],-1)
		cars.add(car)
		x += 155
	x=randrange(200)
	for _ in range(3):
		car=Car(x,ys[6],1)
		cars.add(car)
		x+=140
	return cars

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.speed=6
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
			self.speedx = -1*self.speed
		if keystate[pygame.K_RIGHT]:
			self.speedx = 1*self.speed
		if keystate[pygame.K_UP]:
			self.speedy = -1*self.speed
		if keystate[pygame.K_DOWN]:
			self.speedy = 1*self.speed
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
		self.image.fill(green)
		self.rect = self.image.get_rect()
		self.rect.centerx = random.randint(10,WIDTH-10)
		self.rect.y = 20
def message_to_screen(msg,color):
    textSurf,textRect = text_objects(msg,color)
    #screen_text = font.render(msg,True,color)
    #gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    textRect.center=(WIDTH/2),(HEIGHT/2)
    gameDisplay.blit(textSurf,textRect)
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load(path.join(img_dir, 'road.png')).convert()
background_rect = background.get_rect()

pygame.display.set_caption("Road")
player_img = pygame.image.load(path.join(img_dir, "sheep.png")).convert_alpha()

clock = pygame.time.Clock()

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
		message_to_screen("You Win!",red)
		print "You Win!"
	
	all_sprites.update()
	screen.fill(black)
	screen.blit(background, background_rect)
	all_sprites.draw(screen)

	pygame.display.flip()

pygame.quit()
quit()
