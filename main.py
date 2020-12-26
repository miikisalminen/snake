import pygame
import random as r
from time import sleep

pygame.init() #Start Pygame

WHITE = (255,255,255)
GRAY = (50,50,50)
GREEN = (0,255,0)

points = 0
direction = "down"

appleX = (r.randint(0,80)*10)
appleY = (r.randint(0,80)*10)

currentX = 450
currentY = 450
tail = [(450,450,10,10)]

screen = pygame.display.set_mode((810,810)) #Start the screen
pygame.display.set_caption('snake')

def newApple():
	global appleX
	global appleY
	global tail

	while True:
		appleX = (r.randint(0,81)*10)
		appleY = (r.randint(0,81)*10)
		if (appleX,appleY,10,10) in tail:
			continue
		else:
			pygame.draw.rect(screen,GREEN,(appleX,appleY,10,10))
			break


def gameOver():
	global tail
	global points
	tail = [(450,450,10,10)]


	print("GAME OVER! Points: {0}".format(points))
	points = 0
	for row in range(81):
		for col in range(81):
			pygame.draw.rect(screen,GRAY,((row*10),(col*10),10,10))
	newApple()


def move(direction):
	global currentY
	global currentX

	if direction == "up":
		currentY =  currentY - 10
		pygame.draw.rect(screen,WHITE,(currentX,currentY,10,10))

	if direction == "down":
		currentY = currentY + 10
		pygame.draw.rect(screen,WHITE,(currentX,currentY,10,10))

	if direction == "left":
		currentX =  currentX + 10
		pygame.draw.rect(screen,WHITE,(currentX,currentY,10,10))

	if direction == "right":
		currentX =  currentX - 10
		pygame.draw.rect(screen,WHITE,(currentX,currentY,10,10))

	if currentX > 800:
		currentX = 0
	if currentX < 0:
		currentX = 800
	if currentY > 800:
		currentY = 0
	if currentY < 0:
		currentY = 800

	if (currentX,currentY,10,10) in tail:
		gameOver()

	pygame.draw.rect(screen,GRAY,(tail[0]))
	tail.append((currentX,currentY,10,10))
	tail.pop(0)
	pygame.display.update()


pygame.draw.rect(screen,GREEN,(appleX,appleY,10,10))



for row in range(81):
	for col in range(81):
		pygame.draw.rect(screen,GRAY,((row*10),(col*10),10,10))

pygame.draw.rect(screen,WHITE,(currentX,currentY,10,10))
pygame.draw.rect(screen,GREEN,(appleX,appleY,10,10))
pygame.display.update()

running = True
while running:

	sleep(0.05)
	move(direction)
	pygame.display.update()

	if (currentX,currentY) == (appleX,appleY):
		tail.append((currentX,currentY,10,10))
		points = points + 1
		newApple()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #The user closed the window!
			running = False #Stop running
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_a:
				direction = "right"

			if event.key == pygame.K_w:
				direction = "up"

			if event.key == pygame.K_d:
				direction = "left"

			if event.key == pygame.K_s:
				direction = "down"


pygame.quit() #Close the window