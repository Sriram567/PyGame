import pygame
from config import *
pygame.init()


def instructions():
    winIns = pygame.display.set_mode((screenWidth, screenHeight))
    show = True
    pygame.display.set_caption("Instructions")
    while show:
        winIns.fill((245, 190, 140))
        font = pygame.font.SysFont('comicsans', 25, False, True)
        font2 = pygame.font.SysFont('comicsans', 40, False, True)
        text = font2.render('Instructions Page', 1, instructTextColour)
        winIns.blit(text, ((screenWidth / 2) - 100, 30))
        text = font.render('1) There will be two players',
                           1, instructTextColour)
        winIns.blit(text, (30, 90))
        text = font.render(
            '2) Score will be based on time and crossing obstacles',
            1,
            instructTextColour)
        winIns.blit(text, (30, 120))
        text = font.render(
            '3) The player with greater score wins',
            1,
            instructTextColour)
        winIns.blit(text, (30, 150))
        text = font.render(
            '4) There will be two rounds for each player',
            1,
            instructTextColour)
        winIns.blit(text, (30, 180))
        text = font.render(
            '5) If you hit a obstacle then the round will be completed',
            1,
            instructTextColour)
        winIns.blit(text, (30, 210))
        text = font.render(
            '-> Press key ENTER to start the game',
            1,
            instructTextColour)
        winIns.blit(text, (30, 340))
# the above lines print the instructions.

        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False
    pygame.quit()
# game function


def game():

    win = pygame.display.set_mode((screenWidth, screenHeight))
    global noOfHits
    noOfHits = 0
    noOfHits1 = 0
    noOfHits2 = 0
    global noOfComp
    noOfComp = 0
    noOfComp1 = 0
    noOfComp2 = 0
    pygame.display.set_caption("Warrior")
    var = 0
    pygame.display.update()
    global score1
    global score2
    score1 = 0
    score2 = 0
    g1 = 1
    g2 = 1
    g3 = 1
    g4 = 1
# clock declaration

    clock = pygame.time.Clock()

    class nonmo1(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.hitBox = (self.x, self.y + 20, 80, 70)

        def draw(self, win):
            win.blit(obs1, (self.x, self.y))
# pygame.draw.rect(win, (255,0,0), self.hitBox,2)

    class nonmo2(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.hitBox = (self.x, self.y + 20, 115, 70)

        def draw(self, win):
            win.blit(obs2, (self.x, self.y))
# pygame.draw.rect(win, (255,0,0), self.hitBox,2)
# player function

    class player (object):
        def __init__(self, x, y, velocity, width, height, playerNum):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = velocity
            self.isJump = False
            self.left = False
            self.right = False
            self.walkCount = 0
            self.playerNum = 1
            self.hitBox = (self.x + 17, self.y + 11, 29, 52)
# the below function is called when player got hit
# show sth like pop up
# computes no of times player got hit

        def hit(self):

            if (noOfHits + noOfComp) < 4:
                if (noOfHits + noOfComp) % 2:
                    self.x = 0
                    self.y = 15
                    self.walkCount = 0
                    self.playerNum = 0
                    var = 0
                    font1 = pygame.font.SysFont('comicsans', fontSize)
                    if man.playerNum:

                        text = font1.render(alertingPlayer1, 1, textColour)
                        win.fill(fillColour)
                        win.blit(text, ((screenWidth / 2) - 10 -
                                        100, (4 * screenHeight) // 9))

                    else:

                        text = font1.render(alertingPlayer2, 1, textColour)
                        win.fill(fillColour)
                        win.blit(text, ((screenWidth / 2) - 10 -
                                        100, (4 * screenHeight) / 9))
                    pygame.display.update()
                    i = 0
                    while i < 100:
                        pygame.time.delay(10)
                        i += 1
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                i = 201
                                pygame.quit()
                                quit()
                else:
                    self.x = 0
                    self.y = (8 * screenHeight / 9) + 15
                    var = 0
                    self.walkCount = 0
                    self.playerNum = 1
                    font1 = pygame.font.SysFont('comicsans', fontSize)
                    if man.playerNum:
                        text = font1.render(alertingPlayer1, 1, (34, 52, 23))
                        win.fill((0, 0, 0))
                        win.blit(text, ((screenWidth / 2) - 10 -
                                        100, (4 * screenHeight) / 9))
                    else:
                        text = font1.render(
                            'alertingPlayer2', 1, (34, 252, 23))
                        win.fill((0, 0, 0))
                        win.blit(text, (screenWidth / 2) - 10 -
                                 100, (4 * screenHeight) / 9)
                    pygame.display.update()
                    i = 0
                    while i < 100:
                        pygame.time.delay(10)
                        i += 1
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                i = 201
                                pygame.quit()
                                quit()
# displays score

            else:
                font2 = pygame.font.SysFont('comicsans', fontSize)
                text = font2.render('statistics', 1, textColour)
                win.fill(fillColour)
                win.blit(text, ((screenWidth / 2) - 10 -
                                (text.get_width() / 2), 20))
                text = font2.render(
                    'Player1 Score:' + str(score1), 1, textColour)
                win.blit(text, ((screenWidth / 3) -
                                (text.get_width() / 2), 300))
                text = font2.render(
                    'Player2 Score:' + str(score2), 1, textColour)
                win.blit(text,
                         ((screenWidth / 3) - (text.get_width() / 2),
                          (4 * screenHeight) / 9))
                if score1 > score2:
                    text = font2.render(resultOne, 1, textColour)
                    win.blit(text, ((screenWidth / 2) - 10 -
                                    100, (2 * screenHeight) / 3))
                elif score2 > score1:
                    text = font2.render(resultTwo, 1, textColour)
                    win.blit(text, ((screenWidth / 2) - 10 -
                             (text.get_width() / 2), (2 * screenHeight) / 3))
                else:
                    text = font2.render(resultThree, 1, textColour)
                    win.blit(text, ((screenWidth / 2) - 10 -
                                    100, (2 * screenHeight) / 3))

                pygame.display.update()
                i = 0
                while i < 200:
                    pygame.time.delay(10)
                    i += 0
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 201
                            pygame.quit()
                            quit()
# draw function for  class
# Call it from redraw function

        def draw(self, win):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(char, (self.x, self.y))
            self.hitBox = (self.x + 11, self.y + 11, 34, 52)
# enemy class declaration
# all four moving obstacles are in enemyclass
# sprites are stored in array

    class enemy(object):
        walkRight = [
            pygame.image.load('images/_RUN_000.jpg'),
            pygame.image.load('images/_RUN_001.jpg'),
            pygame.image.load('images/_RUN_002.jpg'),
            pygame.image.load('images/_RUN_003.jpg'),
            pygame.image.load('images/_RUN_004.jpg'),
            pygame.image.load('images/_RUN_005.jpg'),
            pygame.image.load('images/_RUN_006.jpg')]
        walkLeft = [
            pygame.image.load('images/_RUNl_000.jpg'),
            pygame.image.load('images/_RUNl_001.jpg'),
            pygame.image.load('images/_RUNl_002.jpg'),
            pygame.image.load('images/_RUNl_003.jpg'),
            pygame.image.load('images/_RUNl_004.jpg'),
            pygame.image.load('images/_RUNl_005.jpg'),
            pygame.image.load('images/_RUNl_006.jpg')]

        def __init__(self, x, y, velocity2, width, height, end, level):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.path = [x, end]
            self.walkCount = 0
            self.level = level
            self.vel = velocity2
            self.hitBox = (self.x + 18, self.y + 2, 53, 63)
# draw function for enemy class
# it is called from redrawfunction

        def draw(self, win):
            self.move()
            if self.walkCount + 1 >= 21:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            self.hitBox = (self.x + 18, self.y + 2, 53, 63)
# pygame.draw.rect(win, (255,0,0), self.hitBox,2)
# the coordinates for enemies are calculated here

        def move(self):
            if self.vel > 0:
                if self.x < self.path[1] + self.vel:
                    if man.playerNum and noOfHits1:
                        self.x += self.vel
                    elif (1 - man.playerNum) and noOfHits2:
                        self.x += self.vel

                    else:
                        self.x += (self.vel * ((self.level // 2) + 1))
                else:
                    self.vel = self.vel * -1

                    if man.playerNum and noOfHits1:
                        self.x += self.vel
                    elif (1 - man.playerNum) and noOfHits2:
                        self.x += self.vel

                    else:
                        self.x += (self.vel * ((self.level // 2) + 1))
                    self.walkCount = 0

            else:

                if self.x > self.path[0] - self.vel:
                    if man.playerNum and noOfHits1:
                        self.x += self.vel
                    elif (1 - man.playerNum) and noOfHits2:
                        self.x += self.vel

                    else:
                        self.x += (self.vel * ((self.level // 2) + 1))
                else:
                    self.vel = self.vel * -1
                    if man.playerNum and noOfHits1:
                        self.x += self.vel
                    elif (1 - man.playerNum) and noOfHits2:
                        self.x += self.vel

                    else:
                        self.x += (self.vel * ((self.level // 2) + 1))
                    self.walkCount = 0
# in redrawfunction every draw function is called

    def redrawGameWindow():
        global score1
        global score2
        pygame.draw.rect(
            win,
            boxOneColour,
            (0,
             0 * (screenHeight) / 9,
                screenWidth,
                (screenHeight) / 9))
        pygame.draw.rect(
            win,
            boxTwoColour,
            (0,
             1 * (screenHeight) / 9,
                screenWidth,
                (screenHeight) / 9))
        pygame.draw.rect(
            win,
            boxOneColour,
            (0,
             2 * (screenHeight) / 9,
                screenWidth,
                (screenHeight) / 9))
        pygame.draw.rect(
            win,
            boxTwoColour,
            (0,
             3 * (screenHeight) / 9,
                screenWidth,
                (screenHeight) / 9))
        pygame.draw.rect(
            win,
            boxOneColour,
            (0,
             4 * (screenHeight) / 9,
                screenWidth,
                (screenHeight) / 9))
        pygame.draw.rect(
            win,
            boxTwoColour,
            (0,
             5 * (screenHeight) / 9,
                screenWidth,
                (screenHeight) / 9))
        pygame.draw.rect(
            win,
            boxOneColour,
            (0,
             6 * (screenHeight) / 9,
                screenWidth,
                (screenHeight) / 9))
        pygame.draw.rect(
            win,
            boxTwoColour,
            (0,
             7 * (screenHeight) / 9,
                screenWidth,
                (screenHeight) / 9))
        pygame.draw.rect(
            win,
            boxOneColour,
            (0,
             8 * (screenHeight) / 9,
                screenWidth,
                (screenHeight) / 9))
# prints scores
# prints round going on
# prints time
# scores decreaases as time increases

        text1 = font.render('Score1: ' + str(score1), 1, (0, 0, 0))
        win.blit(text1, (((4 * screenWidth) / 5) + 20, 10))
        text2 = font.render('Score2: ' + str(score2), 1, (0, 0, 0))
        win.blit(text2, (((4 * screenWidth) / 5) + 20, 30))
        text3 = font.render(
            'Round: ' + str((warman1.level // 2) + 1), 1, (0, 0, 0))
        win.blit(text3, (((9 * screenWidth) / 20) - 10, 10))
        text4 = font.render('Time: ' + str(var // 25), 1, (0, 0, 0))
        win.blit(text4, (((7 * screenWidth) / 10) - 10, 10))
        if man.playerNum:
            text1 = font.render('Player: 1', 1, (0, 0, 0))
            win.blit(text1, (11 * screenWidth / 20, 10))
        else:
            text1 = font.render('Player: 2', 1, (0, 0, 0))
            win.blit(text1, (((11 * screenWidth) / 20), 10))

        if (var % frameRate == 0):
            if man.playerNum:
                score1 -= 1
            else:
                score2 -= 1
        man.draw(win)
# print start end lines
        if man.playerNum:
            text1 = font.render('START', 2, textColour)
            win.blit(text1, (30, 8 * screenHeight / 9))
            text1 = font.render('END', 2, textColour)
            win.blit(text1, (((9 * screenWidth) / 20) + 20, 80))
        else:
            text1 = font.render('START', 2, (0, 0, 0))
            win.blit(text1, (30, 1 * screenHeight / 11))
            text1 = font.render('END', 2, textColour)
            win.blit(
                text1,
                (((9 * screenWidth) / 20) + 20,
                 8 * screenHeight / 9))
        warman1.draw(win)
        warman2.draw(win)
        warman3.draw(win)
        warman4.draw(win)
        rod1.draw(win)
        rod2.draw(win)
        rod3.draw(win)
        rod4.draw(win)
        rod5.draw(win)
        rod6.draw(win)
        pygame.display.update()

    # mainloopsss
    font = pygame.font.SysFont('comicsans', 30, True)
    man = player(0, (8 * screenHeight / 9) + 20,
                 velocityOfWarrior, 64, 64, True)
    warman4 = enemy(-(1 * screenWidth) / 10,
                    (7 * screenHeight / 9) + 10,
                    velocityOfWarman,
                    81,
                    70,
                    screenHeight,
                    noOfComp + noOfHits)
    warman1 = enemy(
        0,
        (1 * screenHeight / 9) + 10,
        velocityOfWarman,
        81,
        70,
        screenHeight,
        noOfComp + noOfHits)
    warman2 = enemy(-(1 * screenWidth) / 5,
                    (1 * screenHeight / 3) + 10,
                    velocityOfWarman,
                    81,
                    70,
                    screenHeight,
                    noOfComp + noOfHits)
    warman3 = enemy(-(2 * screenWidth) / 5,
                    (5 * screenHeight / 9) + 10,
                    velocityOfWarman,
                    81,
                    70,
                    screenHeight,
                    noOfComp + noOfHits)
    rod1 = nonmo1((1 * screenWidth / 4), (2 * screenHeight / 9))
    rod2 = nonmo1((3 * screenWidth / 4), (2 * screenHeight / 9))
    rod3 = nonmo1((11 * screenWidth / 20), (2 * screenHeight / 3))
    rod4 = nonmo2((7 * screenWidth / 20), (4 * screenHeight / 9))
    rod5 = nonmo2((13 * screenWidth / 20), (4 * screenHeight / 9))
    rod6 = nonmo2((1 * screenWidth / 20), (2 * screenHeight / 3))
    do = True
# while loop runs until cross is hit
    while do:
        warman1.level = noOfHits + noOfComp
        warman2.level = noOfHits + noOfComp
        warman3.level = noOfHits + noOfComp
        warman4.level = noOfHits + noOfComp

        clock.tick(frameRate)
        var += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
        elif keys[pygame.K_RIGHT] and man.x < screenWidth - 64 - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
        elif keys[pygame.K_UP] and man.y > man.vel:
            man.y -= man.vel
        elif keys[pygame.K_DOWN] and man.y < screenHeight - 64 - man.vel:
            man.y += man.vel
        else:
            man.right = False
            man.left = False
            man.walkCount = 0
# array for all enemies
# used for score calculation

        knighty = [
            warman1,
            warman2,
            warman3,
            warman4,
            rod1,
            rod2,
            rod3,
            rod4,
            rod5,
            rod6]
        if man.playerNum:
            if man.y < 30:
                noOfComp1 += 1
                noOfComp = noOfComp1 + noOfComp2
                man.hit()
                g1 = 1
                g2 = 1
                g3 = 1
                g4 = 1
        else:
            if man.y > (8 * screenHeight) / 9:
                noOfComp2 += 1
                noOfComp = noOfComp1 + noOfComp2
                man.hit()
                g1 = 1
                g2 = 1
                g3 = 1
                g4 = 1

        for i in knighty:
            if i.hitBox[1] < man.hitBox[1] + \
                    man.hitBox[3] and i.hitBox[1] + \
                    i.hitBox[3] > man.hitBox[1]:
                if i.hitBox[0] < man.hitBox[0] + \
                        man.hitBox[2] and i.hitBox[0] + \
                        i.hitBox[2] > man.hitBox[0]:
                    if man.playerNum:
                        noOfHits1 += 1
                        noOfHits = noOfHits1 + noOfHits2
                        man.hit()
                        g1 = 1
                        g2 = 1
                        g3 = 1
                        g4 = 1
                    else:
                        noOfHits2 += 1
                        noOfHits = noOfHits1 + noOfHits2
                        man.hit()
                        g1 = 1
                        g2 = 1
                        g3 = 1
                        g4 = 1
        if man.playerNum:
            if (man.y < (13 * screenHeight) / 18) and g1:
                score1 += 20
                g1 = 0
            elif (man.y < (1 * screenHeight) / 2) and g2:
                score1 += 20
                g2 = 0
            elif (man.y < (15 * screenHeight) / 18) and g3:
                score1 += 20
                g3 = 0
            elif (man.y < (1 * screenHeight) / 18) and g4:
                score1 += 20
                g4 = 0
        else:
            if (man.y > (1 * screenHeight) / 6) and g1:
                score2 += 20
                g1 = 0
            elif (man.y > (7 * screenHeight) / 18) and g2:
                score2 += 20
                g2 = 0
            elif (man.y > (11 * screenHeight) / 18) and g3:
                score2 += 20
                g3 = 0
            elif (man.y > (5 * screenHeight) / 6) and g4:
                score2 += 20
                g4 = 0
        redrawGameWindow()
    pygame.quit()
# the above section is also for calculating
# numbers of times players played
# the below function is homepage


def homepage():
    windowHome = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Homepage")
    run = True
    pygame.mixer.music.load('./images/music.mp3')
    pygame.mixer.music.play(-1)
    while run:
        bg = pygame.image.load('./images/bg.jpg')
        font2 = pygame.font.SysFont('comicsans', 30, False, True)
        font = pygame.font.SysFont('comicsans', 100, True, True)
        windowHome.blit(bg, (0, 0))
# printing some details about game

        text = font.render('Warrior', 1, (200, 140, 200))
        windowHome.blit(text, ((screenWidth / 2) - 100, 30))
        text = font2.render('->The games of warriors', 1, homePageTextColour)
        windowHome.blit(text, (30, 150))
        text = font2.render(
            '->Warrior has to survive the obstacles',
            1,
            homePageTextColour)
        windowHome.blit(text, (30, 200))
        text = font2.render(
            '->Warrior has to make him invisible from guards',
            1,
            homePageTextColour)
        windowHome.blit(text, (30, 250))
        text = font2.render(
            '-----Press enter to start the game-----',
            1,
            homePageTextColour)
        windowHome.blit(text, (30, 5 * screenHeight / 6))
        text = font2.render(
            '------Press i to read instructions-----',
            1,
            homePageTextColour)
        windowHome.blit(text, (30, 8 * screenHeight / 9))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game()
        elif keys[pygame.K_i]:
            instructions()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
    quit()
# homepage is used to call every other function


homepage()
