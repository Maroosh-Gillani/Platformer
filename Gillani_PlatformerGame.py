#Maroosh Gillani
#Date: January 21st, 2020
#Gillani_CulminatingGame.py
#Description: Culminating Platformer

import pygame

#Screen Setup 
pygame.init()
width = 700
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Culminating Game: Platformer by Maroosh Gillani")
done = False
clock = pygame.time.Clock()

#General variables used throughout the game
x = 10
y = 50
spd = 7
state = 1
coins = True
coins2 = True
coins3 = True
coins4 = True
coinCheck = True
coinCheck2 = True
coinCheck3 = True
coinCheck4 = True
coinCount = 0
gravity = True

#Functions for the many aspects of the game including the player, coins, platforms, enemies etc.
def player():
    pygame.draw.rect(screen, (250,0,0), pygame.Rect(x, y, 40, 40))#Moveable Square

def enemy():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(ex, ey, ew, eh))

def enemy2():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(e2x, e2y, e2w, e2h))

def enemy3():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(e3x, e3y, e3w, e3h))

def enemy4():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(e4x, e4y, e4w, e4h))

def coin():
    pygame.draw.circle(screen, (250,250,0), (cx, cy), 15)

def coin2():
    pygame.draw.circle(screen, (250,250,0), (c2x, c2y), 15)

def coin3():
    pygame.draw.circle(screen, (250,250,0), (c3x, c3y), 15)

def coin4():
    pygame.draw.circle(screen, (250,250,0), (c4x, c4y), 15)

def platform1():#floor
    pygame.draw.rect(screen, (0,250,0), pygame.Rect(px, py, pw, ph))

#mid air platforms
def platform2():
    pygame.draw.rect(screen, (0,250,0), pygame.Rect(p2x, p2y, p2w, p2h))
        
def platform3():
    pygame.draw.rect(screen, (0,250,0), pygame.Rect(p3x, p3y, p3w, p3h))

def platform4():
    pygame.draw.rect(screen, (0,250,0), pygame.Rect(p4x, p4y, p4w, p4h))

def platform5():
    pygame.draw.rect(screen, (0,250,0), pygame.Rect(p5x, p5y, p5w, p5h))

def movement():
    global x
    global y
    global jump
    global jump2
    global jump3
    global jump4
    global jump5
    global gravity

    pressed = pygame.key.get_pressed()

    #Movement code
    if pressed[pygame.K_LEFT] and x>0:#left
        x -= spd
    if pressed[pygame.K_RIGHT] and x<(width-40):#right
        x += spd

    if y < (py - 40) and gravity == True:#gravity
        y += 10
    #Enabeling player to stand on top of the mid-air platforms
    if (((p2x - 35) < x <(p2x + p2w)) and ((p2y - 45) < y < (p2y + p2h - 45))) or (((p3x - 35) < x <(p3x + p3w)) and ((p3y - 45) < y < (p3y + p3h - 45))) or (((p4x - 35) < x <(p4x + p4w)) and ((p4y - 45) < y < (p4y + p4h - 45))) or (((p5x - 35) < x <(p5x + p5w)) and ((p5y - 45) < y < (p5y + p5h - 45))):#Where player can stand
        gravity = False
    elif (x < (p2x - 15) or x > (p2x + p2w)) or (y < (p2y - 40) or y > (p2y + p2h - 40)) or (x < (p3x - 15) or x > (p3x + p3w)) or (y < (p3y - 40) or y > (p3y + p3h - 40)) or (x < (p4x - 15) or x > (p4x + p4w)) or (y < (p4y - 40) or y > (p4y + p4h - 40)) or (x < (p5x - 15) or x > (p5x + p5w)) or (y < (p5y - 40) or y > (p5y + p5h - 40)):
        gravity = True
                
    if (pressed[pygame.K_SPACE] and (y>(py - 150)) and (jump == True)):#Jump platform1
        y -= 25
    if (y == (py - 150)):
        jump = False
    if (y >= (py - 40)):
        jump = True

    elif (pressed[pygame.K_SPACE] and (y>(p2y - 150)) and (jump2 == True) and ((p2x - 20) < x < (p2x + p2w))):#Jump platform2
        y -= 25
    if (y == (p2y - 150)):
        jump2 = False
    if (y >= (p2y - 40)):
        jump2 = True

    elif (pressed[pygame.K_SPACE] and (y>(p3y - 150)) and (jump3 == True) and ((p3x - 20) < x < (p3x + p3w))):#Jump platform3
        y -= 25
    if (y == (p3y - 150)):
        jump3 = False
    if (y >= (p3y - 40)):
        jump3 = True

    elif (pressed[pygame.K_SPACE] and (y>(p4y - 150)) and (jump4 == True) and ((p4x - 20) < x < (p4x + p4w))):#Jump platform3
        y -= 25
    if (y == (p4y - 150)):
        jump4 = False
    if (y >= (p4y - 40)):
        jump4 = True

    elif (pressed[pygame.K_SPACE] and (y>(p5y - 150)) and (jump5 == True) and ((p5x - 20) < x < (p5x + p5w))):#Jump platform3
        y -= 25
    if (y == (p5y - 150)):
        jump5 = False
    if (y >= (p5y - 40)):
        jump5 = True
                
#Main loop
while not done:
    for event in pygame.event.get():#Quit the game.
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    
    if state == 1:#Start Menu
        screen.fill((250,250,250))
        font = pygame.font.Font('freesansbold.ttf', 20)
        
        text1 = font.render('Pygame Platformer', True, (0,250,0), (250,250,250))
        text1Rect = text1.get_rect()  
        text1Rect.center = (width // 2, 120)
        screen.blit(text1, text1Rect)

        text2 = font.render('Instructions:', True, (0,200,100), (250,250,250))
        text2Rect = text2.get_rect()
        text2Rect.center = (width//2, 160)
        screen.blit(text2, text2Rect)

        text3 = font.render('Left and Right Arrow keys to move, Space to jump', True, (0,200,100), (250,250,250))
        text3Rect = text3.get_rect()
        text3Rect.center = (width//2, 200)
        screen.blit(text3, text3Rect)

        text4 = font.render('Get as many coins as possible', True, (0,200,100), (250,250,250))
        text4Rect = text4.get_rect()
        text4Rect.center = (width//2, 240)
        screen.blit(text4, text4Rect)

        text5 = font.render('Avoid the black blocks; hitting them will result in Game Over', True, (0,200,100), (250,250,250))
        text5Rect = text5.get_rect()
        text5Rect.center = (width//2, 280)
        screen.blit(text5, text5Rect)

        text6 = font.render('Press the Up Arrow Key to Continue', True, (200,0,0), (250,250,250))
        text6Rect = text6.get_rect()
        text6Rect.center = (width//2, 320)
        screen.blit(text6, text6Rect)
        
    if pressed[pygame.K_UP] and state == 1:
        state = 2
        x = 10
        coins = True
        coins2 = True
        coins3 = True
        coins4 = True
        coinCheck = True
        coinCheck2 = True
        coinCheck3 = True
        coinCheck4 = True
        coinCount = 0 

    if state == 2:
        #Update

        #Text
        font = pygame.font.Font('freesansbold.ttf', 20)
        text1 = font.render('Coins: '+(str(coinCount)), True, (250,250,250), (0,145,222))
        text1Rect = text1.get_rect()
        text1Rect.center = (width //2, 40)
                
        #platform1 coordinates coordinates
        px = 0
        py = height - 40
        pw = width
        ph = 40

        #platform2 coordinates
        p2x = 50
        p2y = 350
        p2w = 100
        p2h = 20

        #platform3 coordinates
        p3x = 170
        p3y = 300
        p3w = 200
        p3h = 20

        #platform4 coordinates(Off screen)
        p4x = -450
        p4y = -250
        p4w = 1
        p4h = 2

        #platform5 coordinates(Off screen)
        p5x = -450
        p5y = -250
        p5w = 1
        p5h = 2

        #coin coordinates
        cx = 250
        cy = (p3y - 20)

        #coin2 coordinates
        c2x = 300
        c2y = (p3y - 20)

        #enemy coordinates
        ex = 500
        ey = (py - 40)
        ew = 40
        eh = 40
        
        #player movement
        movement()

        #Draw
        
        screen.fill((0,145,222))
        screen.blit(text1, text1Rect)
        platform1()
        platform2()
        platform3()
        
        #Everything to do with coins
        if coins == True:
            coin()
        if((cx-30) <= x <= (cx+20)) and ((cy-20) <= y <= (cy+20)):
            coins = False
        if((cx-30) <= x <= (cx+20)) and ((cy-20) <= y <= (cy+20)) and coinCheck == True:
            coinCount += 1
            coinCheck = False

        if coins2 == True:
            coin2()
        if((c2x-30) <= x <= (c2x+20)) and ((c2y-20) <= y <= (c2y+20)):
            coins2 = False
        if((c2x-30) <= x <= (c2x+20)) and ((c2y-20) <= y <= (c2y+20)) and coinCheck2 == True:
            coinCount += 1
            coinCheck2 = False
            
        #Enemy collision stuff
        enemy()

        if state == 2 and ((ex - 20 <= x <= ex + 40) and ((ey-10) <= y <= (ey+eh))):#get hit by enemy
            state = 20
            
        player()

    if (state == 2) and (x > 650):
        state = 3
        x = 10
        coins = True
        coins2 = True
        coins3 = True
        coins4 = True
        coinCheck = True
        coinCheck2 = True
        coinCheck3 = True
        coinCheck4 = True

    if state == 3:
        #Update

        #Text
        font = pygame.font.Font('freesansbold.ttf', 20)
        text1 = font.render('Coins: '+(str(coinCount)), True, (250,250,250), (0,145,222))
        text1Rect = text1.get_rect()
        text1Rect.center = (width //2, 40)
                
        #platform1 coordinates coordinates
        px = 0
        py = height - 40
        pw = width
        ph = 40

        #platform2 coordinates
        p2x = 500
        p2y = 350
        p2w = 100
        p2h = 20

        #platform3 coordinates
        p3x = 200
        p3y = 270
        p3w = 270
        p3h = 20

        #platform4 coordinates
        p4x = 100
        p4y = 200
        p4w = 100
        p4h = 20

        #platform5 coordinates (Off screen)
        p5x = -450
        p5y = -250
        p5w = 1
        p5h = 2

        #enemy coordinates
        ex = 200
        ey = (py - 40)
        ew = 40
        eh = 40

        #enemy2 coordinates
        e2x = 320
        e2y = (py - 40)
        e2w = 40
        e2h = 40

        #enemy3 coordinates
        e3x = 440
        e3y = (py - 40)
        e3w = 40
        e3h = 40

        #coin coordinates
        cx = ex + 80
        cy = (py - 20)

        #coin2 coordinates
        c2x = e2x + 80
        c2y = (py - 20)

        #coin3 coordinates
        c3x = p2x + 20
        c3y = (p2y - 20)

        #coin4 coordinates
        c4x = p4x + 20
        c4y = (p4y - 20)
        
        #player movement
        movement()

        #Draw
        
        screen.fill((0,145,222))
        screen.blit(text1, text1Rect)
        platform1()
        platform2()
        platform3()
        platform4()

        #Everything to do with coins
        if coins == True:
            coin()
        if((cx-30) <= x <= (cx+20)) and ((cy-20) <= y <= (cy+20)):
            coins = False
        if((cx-30) <= x <= (cx+20)) and ((cy-20) <= y <= (cy+20)) and coinCheck == True:
            coinCount += 1
            coinCheck = False

        if coins2 == True:
            coin2()
        if((c2x-30) <= x <= (c2x+20)) and ((c2y-20) <= y <= (c2y+20)):
            coins2 = False
        if((c2x-30) <= x <= (c2x+20)) and ((c2y-20) <= y <= (c2y+20)) and coinCheck2 == True:
            coinCount += 1
            coinCheck2 = False

        if coins3 == True:
            coin3()
        if((c3x-30) <= x <= (c3x+20)) and ((c3y-20) <= y <= (c3y+20)):
            coins3 = False
        if((c3x-30) <= x <= (c3x+20)) and ((c3y-20) <= y <= (c3y+20)) and coinCheck3 == True:
            coinCount += 1
            coinCheck3 = False

        if coins4 == True:
            coin4()
        if((c4x-30) <= x <= (c4x+20)) and ((c4y-20) <= y <= (c4y+20)):
            coins4 = False
        if((c4x-30) <= x <= (c4x+20)) and ((c4y-20) <= y <= (c4y+20)) and coinCheck4 == True:
            coinCount += 1
            coinCheck4 = False
            
        #Enemy collision stuff
        enemy()
        if state == 3 and ((ex - 20 <= x <= ex + 40) and ((ey-10) <= y <= (ey+eh))):#get hit by enemy
            state = 20

        enemy2()
        if state == 3 and ((e2x - 20 <= x <= e2x + 40) and ((e2y-10) <= y <= (e2y+e2h))):#get hit by enemy
            state = 20

        enemy3()
        if state == 3 and ((e3x - 20 <= x <= e3x + 40) and ((e3y-10) <= y <= (e3y+e3h))):#get hit by enemy
            state = 20

        player()
        
    if (state == 3) and (x > 650):
        state = 4
        x = 10
        coins = True
        coins2 = True
        coins3 = True
        coins4 = True
        coinCheck = True
        coinCheck2 = True
        coinCheck3 = True
        coinCheck4 = True

    if state == 4:
        #Update

        #Text
        font = pygame.font.Font('freesansbold.ttf', 20)
        text1 = font.render('Coins: '+(str(coinCount)), True, (250,250,250), (0,145,222))
        text1Rect = text1.get_rect()
        text1Rect.center = (width //2, 40)
                
        #platform1 coordinates coordinates
        px = 0
        py = height - 40
        pw = width
        ph = 40

        #platform2 coordinates
        p2x = 100
        p2y = 370
        p2w = 100
        p2h = 20

        #platform3 coordinates
        p3x = 200
        p3y = 300
        p3w = 100
        p3h = 20

        #platform4 coordinates
        p4x = 300
        p4y = 230
        p4w = 100
        p4h = 20

        #platform5 coordinates
        p5x = 400
        p5y = 165
        p5w = 100
        p5h = 20

        #enemy coordinates
        ex = p2x + 60
        ey = (p2y - 40)
        ew = 40
        eh = 40

        #enemy2 coordinates
        e2x = p3x + 60
        e2y = (p3y - 40)
        e2w = 40
        e2h = 40

        #enemy3 coordinates
        e3x = p4x + 60
        e3y = (p4y - 40)
        e3w = 40
        e3h = 40

        #enemy4 coordinates
        e4x = p5x + 60
        e4y = (p5y - 40)
        e4w = 40
        e4h = 40

        #coin coordinates
        cx = p2x + 20
        cy = p2y - 20

        #coin2 coordinates
        c2x = p3x + 20
        c2y = p3y - 20

        #coin3 coordinates
        c3x = p4x + 20
        c3y = p4y - 20

        #coin4 coordinates
        c4x = p5x + 20
        c4y = p5y - 20
        
        #player movement
        movement()

        #Draw
        
        screen.fill((0,145,222))
        screen.blit(text1, text1Rect)
        platform1()
        platform2()
        platform3()
        platform4()
        platform5()

        #Everything to do with coins
        if coins == True:
            coin()
        if((cx-30) <= x <= (cx+20)) and ((cy-20) <= y <= (cy+20)):
            coins = False
        if((cx-30) <= x <= (cx+20)) and ((cy-20) <= y <= (cy+20)) and coinCheck == True:
            coinCount += 1
            coinCheck = False

        if coins2 == True:
            coin2()
        if((c2x-30) <= x <= (c2x+20)) and ((c2y-20) <= y <= (c2y+20)):
            coins2 = False
        if((c2x-30) <= x <= (c2x+20)) and ((c2y-20) <= y <= (c2y+20)) and coinCheck2 == True:
            coinCount += 1
            coinCheck2 = False

        if coins3 == True:
            coin3()
        if((c3x-30) <= x <= (c3x+20)) and ((c3y-20) <= y <= (c3y+20)):
            coins3 = False
        if((c3x-30) <= x <= (c3x+20)) and ((c3y-20) <= y <= (c3y+20)) and coinCheck3 == True:
            coinCount += 1
            coinCheck3 = False

        if coins4 == True:
            coin4()
        if((c4x-30) <= x <= (c4x+20)) and ((c4y-20) <= y <= (c4y+20)):
            coins4 = False
        if((c4x-30) <= x <= (c4x+20)) and ((c4y-20) <= y <= (c4y+20)) and coinCheck4 == True:
            coinCount += 1
            coinCheck4 = False
            
        #Enemy collision stuff
        enemy()
        if state == 4 and ((ex - 20 <= x <= ex + ew) and ((ey-10) <= y <= (ey+eh))):#get hit by enemy
            state = 20

        enemy2()
        if state == 4 and ((e2x - 20 <= x <= e2x + e2w) and ((e2y-10) <= y <= (e2y+e2h))):#get hit by enemy
            state = 20

        enemy3()
        if state == 4 and ((e3x - 20 <= x <= e3x + e3w) and ((e3y-10) <= y <= (e3y+e3h))):#get hit by enemy
            state = 20

        enemy4()
        if state == 4 and ((e4x - 20 <= x <= e4x + e4w) and ((e4y-10) <= y <= (e4y+e4h))):#get hit by enemy
            state = 20
        player()

    if (state == 4) and (x > 650):
        state = 5
        x = 10
        coins = True
        coins2 = True
        coins3 = True
        coins4 = True
        coinCheck = True
        coinCheck2 = True
        coinCheck3 = True
        coinCheck4 = True

    if state == 5:
        #Update

        #Text
        font = pygame.font.Font('freesansbold.ttf', 20)
        text1 = font.render('Coins: '+(str(coinCount)), True, (250,250,250), (0,145,222))
        text1Rect = text1.get_rect()
        text1Rect.center = (width //2, 40)
                
        #platform1 coordinates coordinates
        px = 0
        py = height - 40
        pw = width
        ph = 40

        #platform2 coordinates
        p2x = 100
        p2y = 370
        p2w = 100
        p2h = 20

        #platform3 coordinates
        p3x = 220
        p3y = 300
        p3w = 100
        p3h = 20

        #platform4 coordinates
        p4x = 400
        p4y = 280
        p4w = 200
        p4h = 20

        #platform5 coordinates (Off screen)
        p5x = -400
        p5y = -165
        p5w = 1
        p5h = 20

        #enemy coordinates
        ex = px + 100
        ey = (py - 40)
        ew = 600
        eh = 40

        #enemy2 coordinates
        e2x = ex + 100
        e2y = ey - 40
        e2w = 500
        e2h = 40

        #enemy3 coordinates
        e3x = p3x + 120
        e3y = e2y - 115
        e3w = 40
        e3h = 150

        #enemy4 coordinates
        e4x = -100
        e4y = -100
        e4w = 40
        e4h = 40

        #coin coordinates
        cx = p2x + 20
        cy = p2y - 20

        #coin2 coordinates
        c2x = p3x + 20
        c2y = p3y - 20

        #coin3 coordinates
        c3x = p4x + 20
        c3y = p4y - 20

        #coin4 coordinates
        c4x = p4x + p4w - 20
        c4y = p4y - 20
        
        #player movement
        movement()

        #Draw
        
        screen.fill((0,145,222))
        screen.blit(text1, text1Rect)
        platform1()
        platform2()
        platform3()
        platform4()

        #Everything to do with coins
        if coins == True:
            coin()
        if((cx-30) <= x <= (cx+20)) and ((cy-20) <= y <= (cy+20)):
            coins = False
        if((cx-30) <= x <= (cx+20)) and ((cy-20) <= y <= (cy+20)) and coinCheck == True:
            coinCount += 1
            coinCheck = False

        if coins2 == True:
            coin2()
        if((c2x-30) <= x <= (c2x+20)) and ((c2y-20) <= y <= (c2y+20)):
            coins2 = False
        if((c2x-30) <= x <= (c2x+20)) and ((c2y-20) <= y <= (c2y+20)) and coinCheck2 == True:
            coinCount += 1
            coinCheck2 = False

        if coins3 == True:
            coin3()
        if((c3x-30) <= x <= (c3x+20)) and ((c3y-20) <= y <= (c3y+20)):
            coins3 = False
        if((c3x-30) <= x <= (c3x+20)) and ((c3y-20) <= y <= (c3y+20)) and coinCheck3 == True:
            coinCount += 1
            coinCheck3 = False

        if coins4 == True:
            coin4()
        if((c4x-30) <= x <= (c4x+20)) and ((c4y-20) <= y <= (c4y+20)):
            coins4 = False
        if((c4x-30) <= x <= (c4x+20)) and ((c4y-20) <= y <= (c4y+20)) and coinCheck4 == True:
            coinCount += 1
            coinCheck4 = False
            
        #Enemy collision stuff
        enemy()
        if state == 5 and ((ex - 20 <= x <= ex + ew) and ((ey-10) <= y <= (ey+eh))):#get hit by enemy
            state = 20

        enemy2()
        if state == 5 and ((e2x - 20 <= x <= e2x + e2w) and ((e2y-10) <= y <= (e2y+e2h))):#get hit by enemy
            state = 20

        enemy3()
        if state == 5 and ((e3x - 20 <= x <= e3x + e3w) and ((e3y-10) <= y <= (e3y+e3h))):#get hit by enemy
            state = 20

        enemy4()
        if state == 5 and ((e4x - 20 <= x <= e4x + e4w) and ((e4y-10) <= y <= (e4y+e4h))):#get hit by enemy
            state = 20

        player()

    if (state == 5) and (x > 650) and coinCount == 14:# Game finished with all coins
        state = 6
        screen.fill((0,0,0))
        font = pygame.font.Font('freesansbold.ttf', 25)
        text1 = font.render('Congratulations! You beat the game!', True, (250,250,250), (0,0,0))
        text1Rect = text1.get_rect()
        text1Rect.center = (width //2, height//2 - 50)
        screen.blit(text1, text1Rect)

        text2 = font.render("You even collected all the coins. You're an epic gamer", True, (250,250,250), (0,0,0))
        text2Rect = text2.get_rect()
        text2Rect.center = (width //2, height//2)
        screen.blit(text2, text2Rect)

        text3 = font.render('Press the Down Arrow Key to restart', True, (250,250,250), (0,0,0))
        text3Rect = text3.get_rect()
        text3Rect.center = (width //2, height//2 + 50)
        screen.blit(text3, text3Rect)

    if state == 6 and pressed[pygame.K_DOWN]:#Restart Option
        state = 1

    if (state == 5) and (x > 650) and coinCount < 14:# Game finished without all coins
        state = 7
        screen.fill((0,0,0))
        font = pygame.font.Font('freesansbold.ttf', 25)
        text1 = font.render('I mean you beat the game but you really', True, (250,250,250), (0,0,0))
        text1Rect = text1.get_rect()
        text1Rect.center = (width //2, height//2 - 50)
        screen.blit(text1, text1Rect)

        text2 = font.render("skipped out on some coins, huh? That's not very epic :(", True, (250,250,250), (0,0,0))
        text2Rect = text2.get_rect()
        text2Rect.center = (width //2, height//2)
        screen.blit(text2, text2Rect)

        text3 = font.render('Press the Down Arrow Key to restart', True, (250,250,250), (0,0,0))
        text3Rect = text3.get_rect()
        text3Rect.center = (width //2, height//2 + 50)
        screen.blit(text3, text3Rect)

    if state == 7 and pressed[pygame.K_DOWN]:#Restart Option
        state = 1
            
    if state == 20:#GAME OVER SCREEN
        screen.fill((0,0,0))
        font = pygame.font.Font('freesansbold.ttf', 35)
        text1 = font.render('GAME OVER', True, (250,250,250), (0,0,0))
        text1Rect = text1.get_rect()
        text1Rect.center = (width //2, height//2)
        screen.blit(text1, text1Rect)

        text2 = font.render('Press the Down Arrow Key to restart', True, (250,250,250), (0,0,0))
        text2Rect = text2.get_rect()
        text2Rect.center = (width //2, height//2 + 50)
        screen.blit(text2, text2Rect)

    if state == 20 and pressed[pygame.K_DOWN]:#Restart Option
        state = 1

    pygame.display.flip()
    clock.tick(60)
pygame.quit()


