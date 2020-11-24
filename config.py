import pygame
screenWidth=1000
screenHeight=900
walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')
obs1=pygame.image.load('images/obstacle1.jpg')
obs2=pygame.image.load('images/obstacle3.jpg')
fontSize=50
fontStyle='comicsans'
fillColour=(0,0,0)
textColour=(223,91,243)
frameRate=25
boxOneColour=(35,65,252)
boxTwoColour=(245, 180,118)
velocityOfWarrior=8
velocityOfWarman=9
resultOne='Player 1 won'
resultTwo='Player 2 won'
resultThree='Both are Winnes'
alertingPlayer1='Player1 turn'
alertingPlayer2='Player2 turn'
instructTextColour=(13,62,100)
homePageTextColour =(251,206,255)


