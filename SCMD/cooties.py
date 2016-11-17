#-------------------------------------------------------------------------------
# Name:        Space Cooties Must Die
# Purpose:      Action
#
# Author:      James Newman
#
# Created:     08/08/2016
# Copyright:   (c) James Newman 2016
# Licence:     TO KILL
#-------------------------------------------------------------------------------


#  This is my first project in python, first game ever. It has been a lot of fun
#  to write. I had some artistic help from my son. One of the sounds is from the
#  Blender foundation, the deathflash sound. I got it off OpenGameArt.org. Also
#  found the music there. The title music is called Dark Fallout, by some guy named
#  remaxim. The action music also came from there, but I cant find the attribution info
#  now... so if its yours, let me know and I'll fix it. This ends my feeble attempt
#  at complying with license requirements.




import pygame, sys, random, time
screenwidth = 600                   #set screen width
screenheight = 600                  #set screen height
ceiling = 200                       #Set size of 'house'
maxshots = 3                       #set number of shots player can have on screen
black = 0, 0, 0                     #defines black color for background
playerspeed = 5                     #sets per frame speed of player ship
shotspeed = 15                     #speed of player shots
isalive = True                      #leave this alone
playerlives = 3                     #number of lives for player
collisions = True                   #set to False, player is invincible
showlevel = True                    #leave alone

pygame.mixer.pre_init(22050 , -16, 2, 2048)                      #Initialize pygame mixer
pygame.mixer.init()
pygame.font.init()                                              #Initialize pygame font object
screen = pygame.display.set_mode((screenwidth, screenheight))
clock = pygame.time.Clock()
myfont = pygame.font.SysFont(None ,24)


gamelevels = [(2,4,5, False, 0), (3,5,6, False, 0), (3,5,6, True, 0),
          (3,7,6, False, 1), (4,7,6, True, 1), (4,8,6, False, 2),
          (4,8,5, True, 2), (12,3, 4, True, 1), (5,10,5, True, 2)]



spaceship = pygame.image.load("ship.png").convert()                  #this section loads images and sounds
cootieball = pygame.image.load("ball1.png").convert()
cootieball2 = pygame.image.load("ball2.png").convert()
bomber1 = pygame.image.load("bomber1.png")
bomber2 = pygame.image.load("bomber2.png")
house1 = pygame.image.load("house1.png")
house2 = pygame.image.load("house2.png")
bomb = pygame.image.load("ball.png").convert()
cootieshot = pygame.image.load("cootieshot.png").convert()
title = pygame.image.load("title1.png")
title2 = pygame.image.load("title2.png")
gameovertitle = pygame.image.load("gameover.png")
explosionimg = pygame.image.load("explode.png")
shotsnd = pygame.mixer.Sound("shot.wav")
shotsnd.set_volume(.6)
deathsnd = pygame.mixer.Sound("DeathFlash.wav")
splodesnd = pygame.mixer.Sound("splode.wav")
titlemusic = pygame.mixer.Sound("darkfallout.ogg")
titlemusic.play(-1)
music = pygame.mixer.Sound("action.ogg")
music.set_volume(1)
#music.play(-1)

score = myfont.render(" SCORE:", True, (255,255,255))            #these setup rect objects for score and lives display
scorerect = score.get_rect()
lives = myfont.render(" LIVES:", True, (255,255,255))
livesrect = lives.get_rect()
livesrect.top = 785
leveltext = myfont.render("LEVEL 0", True, (255,255,255))
levelrect = leveltext.get_rect()
levelrect.center = (screenwidth / 2, screenheight / 2)
instructions = myfont.render("SPACE TO FIRE - ARROWS OR W/A/S/D TO MOVE - SPACE TO START", True, (255,255,255))
instructrect = instructions.get_rect()
instructrect.center = (screenwidth / 2, screenheight - 40)



class explosion:
    def __init__(self, pos):
        self.fc = 0
        self.exploderect = explosionimg.get_rect()
        self.exploderect.size = (32, 32)
        self.exploderect.center = pos


    def update(self):
        #exframe = ((self.fc // 4) * 32, ((self.fc+4)%4) * 32, (self.fc // 4) * 32 + 32, ((self.fc+4) % 4)* 32 + 32)
        #exframe = ((self.fc // 4) * 32, ((self.fc+4)%4) * 32, 32, 32)
        exframe = (((self.fc+4)%4) * 32, (self.fc // 4) * 32, 32, 32)
        screen.blit(explosionimg, self.exploderect, exframe)
        self.fc += 1
        if self.fc > 15:
            self.killsplode()


    def killsplode(self):
        mysegs.remove(self)

    def iscollided(self, x):
        pass









class shot:               #player shot object
    def __init__(self):
        self.pos = player1.pos
        self.speed = shotspeed
        self.img = cootieshot
        self.shotrect = cootieshot.get_rect()
        self.shotrect.center = self.pos

    def update(self):
        if self.pos[1] < 10:
            myshots.remove(self)
        else:


            self.pos = (self.pos[0], self.pos[1]-self.speed)
            self.shotrect.center = self.pos
            self.checkcollision()
            screen.blit(self.img, self.shotrect)


    def checkcollision(self):

        for coot in mysegs:
            if coot.iscollided(self.shotrect) != None:
                myshots.remove(self)
                break


class segment:              #basic space cootie segment class
    def __init__(self, nextseg = None, pos = (-20,20)):
        self.pos = pos
        self.speed = 10
        self.right = True
        self.fall = True
        self.nextseg = nextseg
        self.pos2 = pos
        self.pos3 = pos
        self.frame = cootieball
        self.cootieballrect = cootieball.get_rect()
        self.cootieballrect.center = pos
        self.framecount = random.randint(0,5)
        self.bombcounter = 0


    def update(self):

        if self.framecount == 5:
            if self.frame == cootieball:
                self.frame = cootieball2
                2
            else:
                self.frame = cootieball
            self.framecount = 0
        self.framecount += 1
        self.pos3 = self.pos2
        self.pos2 = self.pos

        if self.nextseg != None:
            self.pos = self.nextseg.pos3
            self.right = self.nextseg.right
            self.nextseg.update()
        else:

            if self.right:
                self.pos = (self.pos[0]+self.speed, self.pos[1])
                if self.cootieballrect.center[0] > screenwidth - 20:
                    if self.fall == True:
                        self.pos = (self.pos[0], self.pos[1]+30)
                        if self.pos[1] > screenheight -40:
                            self.fall = False
                    else:
                        self.pos =(self.pos[0], self.pos[1]-30)
                        if self.pos[1] < screenheight-200:
                            self.fall = True
                    self.right = False
            else:
                self.pos = (self.pos[0]-self.speed, self.pos[1])
                if self.cootieballrect.center[0] < 20:
                    if self.fall == True:
                        self.pos = (self.pos[0], self.pos[1]+30)
                        if self.pos[1] > screenheight-40:
                            self.fall = False
                    else:
                        self.pos =(self.pos[0], self.pos[1]-30)
                        if self.pos[1] < screenheight-200:
                            self.fall = True
                    self.right = True
            self.bombcheck()
        self.cootieballrect.center = self.pos
        screen.blit(self.frame, self.cootieballrect)


    def iscollided(self, somerect):
        hits = None
        if self.nextseg != None:
            hits = self.nextseg.iscollided(somerect)
            if self.nextseg == hits:
                self.pos =(self.pos[0], self.pos[1] + 30)
                if self.right == True:
                    self.right = False
                else:
                    self.right = True
                self.nextseg = None


        if self.cootieballrect.colliderect(somerect):
            splodesnd.play()
            self.explode()

            updatescore(20)
            hits = self
            if self.nextseg != None:
                mysegs.append(self.nextseg)
                self.nextseg = None
            if self in mysegs:
                self.killseg()

        return hits

    def killseg(self):
        #insert explosion code?

        mysegs.remove(self)




    def grow(self, length):
        for i in range(length):
            self.spawn()

    def spawn(self):
        if self.nextseg == None:
            self.nextseg = segment()
            self.nextseg.pos = self.pos

        else:
            self.nextseg.spawn()

    def showpos(self):
        if self.nextseg!= None:
            self.nextseg.showpos()
        print("({0},{1})".format(self.pos[0], self.pos[1]), end = "")
        if self.nextseg == None:
            print(" I'm the head!")

    def dropbomb(self):
        mybomb = bombseg(None, self.pos)
        mysegs.append(mybomb)
        self.bombcounter = 0

    def explode(self):
        mysplode = explosion(self.pos)
        mysegs.append(mysplode)

    def bombcheck(self):
        self.bombcounter += 1
        if self.bombcounter > 500 and random.randint(0,50) == 20:
            self.dropbomb()



class bombseg(segment):      #cootie bombs inherit from segment for collisions etc

    def __init__(self, nextseg = None, pos = (-20,20)):
        self.pos = pos
        self.speed = 3
        self.right = True
        self.nextseg = nextseg
        self.pos2 = pos
        self.pos3 = pos
        self.frame = bomb
        self.cootieballrect = bomb.get_rect()
        self.cootieballrect.center = pos
        self.framecount = random.randint(0,5)


    def update(self):

        self.pos = (self.pos[0], self.pos[1]+self.speed)
        self.speed += 1
        self.cootieballrect.center = self.pos
        if self.pos[1] >= screenheight:
            self.killseg()

        screen.blit(self.frame, self.cootieballrect)


class housecootie(segment):   #this guy runs around the house
    def __init__(self, nextseg = None, pos = (-20 ,screenheight - ceiling)):
        self.pos = pos
        self.speed = 1
        self.right = True
        self.nextseg = nextseg
        self.pos2 = pos
        self.pos3 = pos
        self.frame = house1
        self.cootieballrect = house1.get_rect()
        self.cootieballrect.center = pos
        self.framecount = random.randint(0,5)
        self.fallspeed = 1

    def update(self):

        if self.fallspeed < 0:
            self.frame = house1

        else:
            self.frame = house2




        if self.right:
            self.pos = (self.pos[0]+self.speed, self.pos[1]+self.fallspeed)
            self.cootieballrect.center = self.pos
            if self.cootieballrect.center[0] > screenwidth:
                self.right = False


        else:
            self.pos = (self.pos[0]-self.speed, self.pos[1]+self.fallspeed)
            self.cootieballrect.center = self.pos
            if self.cootieballrect.center[0] < 0:
                self.right = True

        self.fallspeed += 1
        if self.pos[1] >= screenheight - 15:
            self.fallspeed = -random.randint(10,25)
            print(self.fallspeed)

        screen.blit(self.frame, self.cootieballrect)

    def killseg(self):
        #insert explosion code?

        mysegs.remove(self)
        level.remhc()

class bomber(segment): #bomber segment class to drop many bombs, boooom
    def __init__(self, nextseg = None, pos = (-20 ,20)):
        self.pos = pos
        self.speed = 2
        self.right = True
        self.nextseg = nextseg
        self.pos2 = pos
        self.pos3 = pos
        self.frame = bomber1
        self.cootieballrect = bomber1.get_rect()
        self.cootieballrect.center = pos
        self.framecount = random.randint(0,5)
        self.bombcounter = 0

    def bombcheck(self):
        self.bombcounter += 1
        if self.bombcounter > 5 and random.randint(0,10) == 10:
            self.dropbomb()

    def update(self):

        if self.framecount == 10:
            if self.frame == bomber1:
                self.frame = bomber2
                2
            else:
                self.frame = bomber1
            self.framecount = 0
        self.framecount += 1


        if self.right:
            self.pos = (self.pos[0]+self.speed, self.pos[1])
            self.cootieballrect.center = self.pos
            if self.cootieballrect.center[0] > screenwidth:
                self.killseg()


        else:
            self.pos = (self.pos[0]-self.speed, self.pos[1])
            self.cootieballrect.center = self.pos
            if self.cootieballrect.center[0] < 0:
                self.killseg()

        self.bombcheck()
        #self.cootieballrect.center = self.pos
        screen.blit(self.frame, self.cootieballrect)



class player:
    def __init__(self):
        self.pos = (screenwidth // 2, screenheight - 40)
        self.img = spaceship   # make player image
        self.uboundary = screenheight - ceiling
        self.lboundary = screenheight -30
        self.speed = (0,0)
        self.playerrect=self.img.get_rect()

    def reset(self):
        self.pos = (screenwidth // 2, screenheight - 40)


    def update(self):


        self.pos =(self.pos[0] + self.speed[0], self.pos[1] + self.speed[1])
        if self.pos[1] < self.uboundary or self.pos[1] > self.lboundary:
            self.pos =(self.pos[0], self.pos[1] - self.speed[1])
        if self.pos[0] < 20 or self.pos[0] > screenwidth - 20:
            self.pos = (self.pos[0] - self.speed[0], self.pos[1])
        self.playerrect.center = self.pos
        if collisions:
            self.checkcollision()
        screen.blit(self.img, self.playerrect)


    def checkcollision(self):
        global isalive
        global gamelives
        for coot in mysegs:
            if coot.iscollided(self.playerrect) != None:
                #print("I'm Dead!")
                deathsnd.play()
                for i in range(255, 0, -1):
                    screen.fill( (i, i, i))
                    clock.tick(60)
                    pygame.display.flip()


                isalive = False
                updatelives(-1)



def updatescore(points):
    global score
    global gamescore
    gamescore += points
    score = myfont.render("SCORE: {0}".format(gamescore), True, (255,255,255))

def updatelives(life):
    global lives
    global gamelives
    gamelives += life
    lives = myfont.render(" LIVES: {0}".format(gamelives), True, (255,255,255))

def updatelevel(lev):
    global leveltext
    leveltext = myfont.render("LEVEL {0}".format(lev), True, (200, 0, 0))


class levelstate:
    def __init__(self):
        self.level = 0
        self.timer = time.clock()
        #self.nextspawn = 5
        self.levels = gamelevels
        self.level = None
        self.levelnum = 0
        self.segments = 0
        self.length = 0
        self.interval = 0
        self.numhc = 0
        self.restarted = True
        self.displaycount = 0


    def getlevel(self):
        if self.levelnum < len(self.levels):
            self.segments, self.length, self.interval, self.bombers, self.housecooties = self.levels[self.levelnum]
##            if restarted == False:
##                del self.levels[0]

        else:
            self.segments = 5
            self.length = 12
            self.interval = 3
            self.bombers = True
            self.housecooties = 3
        self.levelnum += 1




    def remhc(self):
        self.numhc -= 1

    def levelcheck(self):
        global showlevel

        if self.displaycount <=0:
            showlevel = False
        else:
            self.displaycount -= 1
        if time.clock() > self.timer + self.interval or self.restarted: #hacky check to see if the level is starting
            if self.segments == 0:
                if len(mysegs) == 0:
                    self.getlevel()
                    updatelevel(self.levelnum)
                    showlevel = True
                    self.displaycount = 120
                else:
                    if self.numhc < self.housecooties:
                        if self.bombers:
                            if random.randint(0,6) == 3:
                                self.spawnbomber()
                        self.spawnhousecootie()
                        self.numhc += 1
            elif self.segments > 0:
                self.spawnseg()
                self.segments -= 1
                if self.segments == 0:
                    if self.bombers:
                        self.spawnbomber()

            if self.restarted:
                self.timer = time.clock() - (self.interval - 1)
                self.restarted = False
            else:
                self.timer = time.clock()

    def restart(self):
        self.restarted = True
        self.levelnum -= 1



    def spawnseg(self):
        newseg = segment()
        if random.randint(0,1) == 1:
            newseg.pos = (screenwidth + 20, -10)
        newseg.grow(self.length)
        mysegs.append(newseg)

    def spawnbomber(self):
        newseg = bomber()
        if random.randint(0,1) == 1:
            newseg.pos = (screenwidth + 20, 30)
            newseg.right = False
        mysegs.append(newseg)

    def spawnhousecootie(self):
        newseg = housecootie()
        if random.randint(0,1) == 1:
            newseg.pos = (screenwidth + 20, screenheight - ceiling)
            newseg.right = False
        mysegs.append(newseg)



def titlescreen():
    mytitle = title
    titlerect = mytitle.get_rect()
    titlerect.center = (screenwidth / 2, 300)
    timer = time.clock()
    pygame.event.clear()
    while True:
        if time.clock() > timer + 2:
            if mytitle == title:
                mytitle = title2
            else:
                mytitle = title
            timer = time.clock()

        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:

            pygame.quit()
            sys.exit()
            break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict['key']
            #print(key)
            if key == 27:                  # On Escape key ...
                pygame.quit()
                sys.exit()
                break                      #   leave the game loop.

            if key == 32:
                break



        screen.fill( (0, 0, 0))
        screen.blit(mytitle, titlerect)
        screen.blit(instructions, instructrect)
        clock.tick(60)
        pygame.display.flip()

    return


def gameover():
    titlerect = gameovertitle.get_rect()
    titlerect.center = (screenwidth / 2, 300)
    timer = time.clock()
    while time.clock() < timer + 5:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:

            pygame.quit()
            sys.exit()
            break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict['key']
            #print(key)
            if key == 27:                  # On Escape key ...
                pygame.quit()
                sys.exit()
                break

        screen.fill( (0, 0, 0))
        screen.blit(gameovertitle, titlerect)
        screen.blit(score, scorerect)
        screen.blit(lives, livesrect)

        clock.tick(60)
        pygame.display.flip()

    return



def quitgame():
    pygame.quit()
    sys.exit()



def gameloop():

    #player1 = player()
    #mysegs = []
    #myshots = []

##myshot = shot()
##myshots.append(myshot)
    #mypos = (25, 300)
    #myseg=segment()
    #myseg.grow(5)
    #mysegs.append(myseg)
    #mybomb = bombseg(None, mypos)

    #mysegs.append(mybomb)

    #level.levelcheck()
    #level.spawnseg()

    while isalive:

        level.levelcheck()
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            quitgame()
            break;
        if ev.type == pygame.KEYDOWN:
            key = ev.dict['key']
            #print(key)
            if key == 27:                  # On Escape key ...
                quitgame()
                break                      #   leave the game loop.
            if key == ord('p'):
                newseg=segment()
                newseg.grow(5)
                mysegs.append(newseg)
            if key == ord('w') or key == 273:
                player1.speed = (player1.speed[0], player1.speed[1]-playerspeed)
            if key == ord('s') or key == 274:
                player1.speed = (player1.speed[0], player1.speed[1]+playerspeed)
            if key == ord('a') or key == 276:
                player1.speed = (player1.speed[0] -playerspeed, player1.speed[1])
            if key == ord('d') or key == 275:
                player1.speed = (player1.speed[0] +playerspeed, player1.speed[1])
            if key == 32:
                if len(myshots) < maxshots:
                    shotsnd.play()
                    newshot = shot()
                    myshots.append(newshot)



        if ev.type == pygame.KEYUP:
            key = ev.dict['key']
            #print(key)
            if key == ord('w') or key == 273:
                player1.speed = (player1.speed[0], player1.speed[1]+playerspeed)
            if key == ord('s') or key == 274:
                player1.speed = (player1.speed[0], player1.speed[1]-playerspeed)
            if key == ord('a') or key == 276:
                player1.speed = (player1.speed[0] +playerspeed, player1.speed[1])
            if key == ord('d') or key == 275 :
                player1.speed = (player1.speed[0] -playerspeed, player1.speed[1])


        screen.fill( (0, 0, 0))

        if showlevel:
            screen.blit(leveltext, levelrect)
        screen.blit(score, scorerect)
        screen.blit(lives, livesrect)
        for seg in mysegs:
            seg.update()

        for shooted in myshots:
            shooted.update()



        player1.update()
        clock.tick(60)
        pygame.display.flip()
        #print(player1.speed)

while True:
    titlescreen()
    titlemusic.stop()
    music.play(-1)
    player1 = player()
    mysegs = []
    myshots = []
    level = levelstate()
    gamescore = 0
    updatescore(0)
    gamelives = playerlives
    updatelives(0)


    while gamelives:

        gameloop()
        mysegs = []
        player1.reset()
        level.restart()
        isalive = True

    gameover()
    music.stop()
    titlemusic.play(-1)

quitgame()






