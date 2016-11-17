def SCMD():

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
            self.speed = 2
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
        gamescore = 0
        gamescore += points
        score = myfont.render("SCORE: {0}".format(gamescore), True, (255,255,255))

    def updatelives(life):
        global lives
        global gamelives
        gamelives = 0
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

def Bullets():

    import pygame
    import random

    # Define some colors
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    RED      = ( 255,   0,   0)
    BLUE     = (   0,   0, 255)

    # --- Classes

    class Block(pygame.sprite.Sprite):
        """ This class represents the block. """
        def __init__(self, color):
            # Call the parent class (Sprite) constructor
            super().__init__()

            self.image = pygame.Surface([20, 15])
            self.image.fill(color)

            self.rect = self.image.get_rect()

    class Player(pygame.sprite.Sprite):
        """ This class represents the Player. """

        def __init__(self):
            """ Set up the player on creation. """
            # Call the parent class (Sprite) constructor
            super().__init__()

            self.image = pygame.Surface([20, 20])
            self.image.fill(RED)

            self.rect = self.image.get_rect()

        def update(self):
            """ Update the player's position. """
            # Get the current mouse position. This returns the position
            # as a list of two numbers.
            pos = pygame.mouse.get_pos()

            # Set the player x position to the mouse x position
            self.rect.x = pos[0]

    class Bullet(pygame.sprite.Sprite):
        """ This class represents the bullet . """
        def __init__(self):
            # Call the parent class (Sprite) constructor
            super().__init__()

            self.image = pygame.Surface([4, 10])
            self.image.fill(BLACK)

            self.rect = self.image.get_rect()

        def update(self):
            """ Move the bullet. """
            self.rect.y -= 3


    # --- Create the window

    # Initialize Pygame
    pygame.init()

    # Set the height and width of the screen
    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])

    # --- Sprite lists

    # This is a list of every sprite. All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()

    # List of each block in the game
    block_list = pygame.sprite.Group()

    # List of each bullet
    bullet_list = pygame.sprite.Group()

    # --- Create the sprites

    for i in range(50):
        # This represents a block
        block = Block(BLUE)

        # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(350)

        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)

    # Create a red player block
    player = Player()
    all_sprites_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    score = 0
    player.rect.y = 370

    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)

        # --- Game logic

        # Call the update() method on all the sprites
        all_sprites_list.update()

        # Calculate mechanics for each bullet
        for bullet in bullet_list:

            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

            # For each block hit, remove the bullet and add to the score
            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1
                print(score)

            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

        # --- Draw a frame

        # Clear the screen
        screen.fill(WHITE)

        # Draw all the spites
        all_sprites_list.draw(screen)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 20 frames per second
        clock.tick(60)

    pygame.quit()


def Brick_Breaker():

    # --- Import libraries used for this program

    import math
    import pygame

    # Define some colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)

    # Size of break-out blocks
    block_width = 23
    block_height = 15

    class Block(pygame.sprite.Sprite):
        """This class represents each block that will get knocked out by the ball
        It derives from the "Sprite" class in Pygame """

        def __init__(self, color, x, y):
            """ Constructor. Pass in the color of the block, 
                and its x and y position. """
            
            # Call the parent class (Sprite) constructor
            super().__init__()
            
            # Create the image of the block of appropriate size
            # The width and height are sent as a list for the first parameter.
            self.image = pygame.Surface([block_width, block_height])
            
            # Fill the image with the appropriate color
            self.image.fill(color)
            
            # Fetch the rectangle object that has the dimensions of the image
            self.rect = self.image.get_rect()
            
            # Move the top left of the rectangle to x,y.
            # This is where our block will appear..
            self.rect.x = x
            self.rect.y = y


    class Ball(pygame.sprite.Sprite):
        """ This class represents the ball        
            It derives from the "Sprite" class in Pygame """
        
        # Speed in pixels per cycle
        speed = 10.0
        
        # Floating point representation of where the ball is
        x = 0.0
        y = 180.0
        
        # Direction of ball (in degrees)
        direction = 200

        width = 10
        height = 10
        
        # Constructor. Pass in the color of the block, and its x and y position
        def __init__(self):
            # Call the parent class (Sprite) constructor
            super().__init__()
            
            # Create the image of the ball
            self.image = pygame.Surface([self.width, self.height])
            
            # Color the ball
            self.image.fill(white)
            
            # Get a rectangle object that shows where our image is
            self.rect = self.image.get_rect()
            
            # Get attributes for the height/width of the screen
            self.screenheight = pygame.display.get_surface().get_height()
            self.screenwidth = pygame.display.get_surface().get_width()
        
        def bounce(self, diff):
            """ This function will bounce the ball 
                off a horizontal surface (not a vertical one) """
            
            self.direction = (180 - self.direction) % 360
            self.direction -= diff
        
        def update(self):
            """ Update the position of the ball. """
            # Sine and Cosine work in degrees, so we have to convert them
            direction_radians = math.radians(self.direction)
            
            # Change the position (x and y) according to the speed and direction
            self.x += self.speed * math.sin(direction_radians)
            self.y -= self.speed * math.cos(direction_radians)
            
            # Move the image to where our x and y are
            self.rect.x = self.x
            self.rect.y = self.y
            
            # Do we bounce off the top of the screen?
            if self.y <= 0:
                self.bounce(0)
                self.y = 1
                
            # Do we bounce off the left of the screen?
            if self.x <= 0:
                self.direction = (360 - self.direction) % 360
                self.x = 1
                
            # Do we bounce of the right side of the screen?
            if self.x > self.screenwidth - self.width:
                self.direction = (360 - self.direction) % 360
                self.x = self.screenwidth - self.width - 1
            
            # Did we fall off the bottom edge of the screen?
            if self.y > 600:
                return True
            else:
                return False

    class Player(pygame.sprite.Sprite):
        """ This class represents the bar at the bottom that the player controls. """
        
        def __init__(self):
            """ Constructor for Player. """
            # Call the parent's constructor
            super().__init__()
            
            self.width = 75
            self.height = 15
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill((white))
            
            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.screenheight = pygame.display.get_surface().get_height()
            self.screenwidth = pygame.display.get_surface().get_width()

            self.rect.x = 0
            self.rect.y = self.screenheight-self.height
        
        def update(self):
            """ Update the player position. """
            # Get where the mouse is
            pos = pygame.mouse.get_pos()
            # Set the left side of the player bar to the mouse position
            self.rect.x = pos[0]
            # Make sure we don't push the player paddle 
            # off the right side of the screen
            if self.rect.x > self.screenwidth - self.width:
                self.rect.x = self.screenwidth - self.width

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])

    # Set the title of the window
    pygame.display.set_caption('Breakout')

    # Enable this to make the mouse disappear when over our window
    pygame.mouse.set_visible(0)

    # This is a font we use to draw text on the screen (size 36)
    font = pygame.font.Font(None, 36)

    # Create a surface we can draw on
    background = pygame.Surface(screen.get_size())

    # Create sprite lists
    blocks = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()

    # Create the player paddle object
    player = Player()
    allsprites.add(player)

    # Create the ball
    ball = Ball()
    allsprites.add(ball)
    balls.add(ball)

    # The top of the block (y position)
    top = 80

    # Number of blocks to create
    blockcount = 32

    # --- Create blocks

    # Five rows of blocks
    for row in range(5):
        # 32 columns of blocks
        for column in range(0, blockcount):
            # Create a block (color,x,y)
            block = Block(blue, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        # Move the top of the next row down
        top += block_height + 2

    # Clock to limit speed
    clock = pygame.time.Clock()

    # Is the game over?
    game_over = False

    # Exit the program?
    exit_program = False

    # Main program loop
    while exit_program != True:

        # Limit to 30 fps
        clock.tick(30)

        # Clear the screen
        screen.fill(black)
        
        # Process the events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program = True
        
        # Update the ball and player position as long
        # as the game is not over.
        if not game_over:
            # Update the player and ball positions
            player.update()
            game_over = ball.update()
        
        # If we are done, print game over
        if game_over:
            text = font.render("Game Over", True, white)
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos.top = 300
            screen.blit(text, textpos)
        
        # See if the ball hits the player paddle
        if pygame.sprite.spritecollide(player, balls, False):
            # The 'diff' lets you try to bounce the ball left or right 
            # depending where on the paddle you hit it
            diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)
            
            # Set the ball's y position in case 
            # we hit the ball on the edge of the paddle
            ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
            ball.bounce(diff)
        
        # Check for collisions between the ball and the blocks
        deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
        
        # If we actually hit a block, bounce the ball
        if len(deadblocks) > 0:
            ball.bounce(0)
            
            # Game ends if all the blocks are gone
            if len(blocks) == 0:
                game_over = True
        
        # Draw Everything
        allsprites.draw(screen)

        # Flip the screen and show what we've drawn
        pygame.display.flip()

    pygame.quit()
