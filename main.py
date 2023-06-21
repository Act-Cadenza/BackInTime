# Import pygame and libraries
from pygame.locals import *
import random
import os
import pygame

import pygameMenu
from pygameMenu.locals import *

import with_highscore

#for colors
green = (0,255,0)
yellow = (255,255,0)
red = (255,0,0)
COLOR_BACKGROUND = (128, 0, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (255, 147, 126)
WINDOW_SIZE = (700, 500)


#initialization
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'


ABOUT = ['Back In Time 2019',
        'Author: Cris Orot and Ian Salac Themselves',
        PYGAMEMENU_TEXT_NEWLINE,
        'Special Thanks to: "Alagad ni Bogart"',
        'The Internet and Pizzarro',
        'Tutorials: "Tech with Tim"']

#set-up screen
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Back In Time')

clock = pygame.time.Clock()


#Global Variables
ally1_attack = 70
ally2_attack = 75
eattack = 60
modify = 60


#character assets
#idle = [pygame.image.load('assets/a_0-1.png'),pygame.image.load('assets/a_0-2.png'),pygame.image.load('assets/a_0-3.png'),pygame.image.load('assets/a_0-4.png'),pygame.image.load('assets/a_0-5.png'),pygame.image.load('assets/a_0-6.png'),pygame.image.load('assets/a_0-7.png'),]
idle = pygame.image.load('assets/char1.png')
bg1 = pygame.image.load('assets/ya.png')
bg = pygame.image.load('assets/ye.jpg')#If you want import your character and dont want to type all time pygame.image.load, just set for example ld = pygame.image.load and do Walkright = [ld('R1.png')],its simpler.?
m1 = pygame.image.load('assets/pixil-frame-0.png')
ch = pygame.image.load('assets/charicon.png')
hel = pygame.image.load('assets/heal.png')
hswap = pygame.image.load('assets/hpswap.png')
ins = pygame.image.load('assets/instantkill.png')
al1 = pygame.image.load('assets/ally.png')


al2 = pygame.image.load('assets/healer.png')
hail = [pygame.image.load('assets/hail.png')]
pot = [pygame.image.load('assets/HP25.png')]
rank = [pygame.image.load('assets/rank.png')]
ss = [pygame.image.load('assets/swap.png')]
dd = [pygame.image.load('assets/dam.png')]
ff = [pygame.image.load('assets/pop.png')]
goldfish = [pygame.image.load('assets/more.png')]
h40 = [pygame.image.load('assets/h40.png')]
fireball = [pygame.image.load('assets/fireball.png')]

goblin1 = pygame.image.load('assets/bone.png')
goblin = pygame.image.load('assets/goblin.png')
wolf1 = pygame.image.load('assets/wolf1.png')
wolf = pygame.image.load('assets/wolf.png')
flower1 = pygame.image.load('assets/flower1.png')
flower = pygame.image.load('assets/flower.png')
atk1 = [pygame.image.load('assets/char1.png'),pygame.image.load('assets/char2.png'),pygame.image.load('assets/char3.png'),pygame.image.load('assets/char4.png'),pygame.image.load('assets/char5.png')]
atk2 = [pygame.image.load('assets/char_1.png'),pygame.image.load('assets/char_2.png'),pygame.image.load('assets/char_3.png'),pygame.image.load('assets/char_4.png'),pygame.image.load('assets/char_5.png')]
hit = pygame.image.load('assets/0.png')
bird = pygame.image.load('assets/bird.png')
icheal = pygame.image.load('assets/icheal.png')


display = ''
stand = 1

#sound effects
pygame.mixer.music.load('sound/asgore.mp3')
healerjoin = pygame.mixer.Sound('sound/healcome.wav')
healeratk = pygame.mixer.Sound('sound/heal.wav')
healervoice = pygame.mixer.Sound('sound/healvoice.wav')
punch = pygame.mixer.Sound('sound/punch.wav')
fire = pygame.mixer.Sound('sound/cannonfire.wav')
end = pygame.mixer.Sound('sound/end.wav')
join = pygame.mixer.Sound('sound/joiny.wav')
coin = pygame.mixer.Sound('sound/coin.wav')
weneed = pygame.mixer.Sound('sound/nogold.wav')
pop = pygame.mixer.Sound('sound/pop.wav')
incre = pygame.mixer.Sound('sound/incre.wav')
swap = pygame.mixer.Sound('sound/swap.wav')
wolf3 = pygame.mixer.Sound('sound/wolf3.wav')
flower3 = pygame.mixer.Sound('sound/flower3.wav')
goblin3 = pygame.mixer.Sound('sound/goblin3.wav')
limit = pygame.mixer.Sound('sound/limit.wav')
fireegg = pygame.mixer.Sound('sound/fireegg.wav')




#Battle cons
player_count = 0
enemyh = 0
player_damage = 5
visible = True
Full = True
basic_ally_damage = 10
basic_ally_heal = 30
ally = False
ally2 = False
gold = 0
damage = 1
round_count = 0
done = False

font = pygame.font.SysFont(None,25)
font2 = pygame.font.SysFont('comicsans',25, True)
font3 = pygame.font.SysFont('comicsans',25, True)
font4 = pygame.font.SysFont('comicsans',25, True)
font5 = pygame.font.SysFont('comicsans',25, True)
font6 = pygame.font.SysFont('comicsans',20, True)



class Battle(object):
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = 100
        self.idlecount = 0
       
        
        
       
        

    def Health(self):
        global player_count
        global gold
        global round_count
        global pcolor
        global ecolor
        global enemyh
        global visible
        global Full
        global done
        
        if Full:
            if self.health > 75:
                pcolor = green
            elif self.health > 50:
                pcolor = yellow
            elif self.health > 30:
                pcolor = red
            elif self.health <= 0:
                pcolor = red
                self.health = 0
                done = True
                Full = False
                player_count += 1
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(end)
                with_highscore.record_high(surface, 'Highscore.txt', round_count)
                
                
               
                
            pygame.draw.rect(surface, pcolor, (75,380,self.health, 10))
            surface.blit(pygame.transform.scale(ch,(28,26)),(50,370))
            
        if visible:
            if enemyh > 75:
                ecolor = green
            elif enemyh > 50:
                ecolor = yellow
            elif enemyh > 30:
                ecolor = red
            elif enemyh <= 0:
                ecolor = red
                visible = False
                encounter_choice = [self.enemy_flower, self.enemy_wolf, self.enemy_goblin]
                random.choice(encounter_choice)()
                round_count += 1
                gold += 20


            kill = font2.render('Round ' + str(round_count),1,(100,123,255))
            surface.blit(kill,(50, 450))
            add_gold = font2.render('Gold: ' + str(gold),1, (255,255,0))
            surface.blit(add_gold, (50,430))
            pygame.draw.rect(surface, ecolor, (50,60, enemyh, 10))
            pygame.display.flip()
    
    
                                 
    def enemy_attack(self):
        global player_damage
        self.health -= player_damage

#Item in shop that swaps 30 hp for 100 gold
    def shop_greedy(self):
        global enemyh, gold
        if self.health >= 75:
            pygame.mixer.Sound.play(swap)
            FadeIn(ss[0])
            pygame.mixer.Sound.play(coin)
            self.health = self.health - 30
            gold = gold + 80
            print("Swapped 30 health for 80 gold")
        elif self.health >= 40:
            pygame.mixer.Sound.play(limit)
            FadeIn(h40[0])
            print("Can't buy item: Health Limit is 40")

    def healer_fack(self):
        global basic_ally_heal
        if self.health > 100:
            self.health = 100
        else:
            self.health += basic_ally_heal
            

    #Item in shop to restore health by 25
    def shop_healthpartial(self):
        global gold, health
        
        if gold >= 100:
            if self.health < 100:
                FadeIn(pot[0])
                pygame.mixer.Sound.play(healeratk)
                pygame.mixer.Sound.play(coin)
                self.health +=25
                gold = gold - 100
                print("Restored 25 Health")
            elif self.health > 100:
                self.health = 100
                print("Already in full health")
        elif gold < 100:
            print("Need More Gold!")
            pygame.mixer.Sound.play(weneed)
            FadeIn(goldfish[0])

    def Boss(self):
        global enemyh
        global player_damage
        global visible
        global round_count
        global display
        enemyh = 200
        visible = True
        player_damage = 20
        display = 4

    def enemy_flower(self):
        global enemyh
        global visible
        global player_damage
        global display,round_count
        if round_count >= 40:
            player_damage = 77
        else:
            player_damage = 10
        enemyh = 0
        visible = True
        enemyh = 12
        #player_damage = 10
        display = 1
        
    def enemy_wolf(self):
        global enemyh
        global visible
        global player_damage
        global display,round_count
        if round_count >= 40:
            player_damage = 80
        else:
            player_damage = 15 
        enemyh = 0
        visible = True
        enemyh = 15
        display = 2

    def enemy_goblin(self):
        global enemyh
        global visible
        global player_damage
        global display,round_count
        if round_count >= 40:
            player_damage = 69
        else:
            player_damage = 6
        enemyh = 0
        visible = True
        enemyh = 10
        #player_damage = 6
        display = 3

    def asset(self):
        global stand, ally, ally2
        surface.blit(bg,(0,0))
        surface.blit(pygame.transform.scale(m1,(400,500)),(300,0))
        surface.blit(pygame.transform.scale(m1,(300,130)),(10,350))
        surface.blit(pygame.transform.scale(m1,(300,80)),(10,20))
        surface.blit(pygame.transform.scale(hel,(200,200)),(350,0))
        surface.blit(pygame.transform.scale(hswap,(200,200)),(350,70))
        surface.blit(pygame.transform.scale(ins,(200,200)),(350,140))
        surface.blit(pygame.transform.scale(al1,(200,200)),(350,210))
        surface.blit(pygame.transform.scale(icheal,(200,200)),(350,270))
        w1 = font6.render('press a to buy',1, (255,0,255))
        w2 = font6.render('press s to buy',1, (255,0,255))
        w3 = font6.render('press f to buy',1, (255,0,255))
        w4 = font6.render('press g to buy',1, (255,0,255))
        w5 = font6.render('press h to buy',1, (255,0,255))
        surface.blit(w1, (560,100))
        surface.blit(w2, (560,170))
        surface.blit(w3, (560,230))
        surface.blit(w4, (560,310))
        surface.blit(w5, (560,370))
        #passive
        if stand == 1:
            surface.blit(pygame.transform.scale(idle, (64,96)),(self.x,self.y)) #resize char sprite using transform in a every list index (width,height)
        if display == 1:
            en = font2.render('Fishface:',1, (255,0,0))
            surface.blit(en, (50,40))
            surface.blit(pygame.transform.scale(flower,(45,100)),(240,110))
        elif display == 2:
            en = font2.render('Werewolf:',1, (255,0,0))
            surface.blit(en, (50,40))
            surface.blit(pygame.transform.scale(wolf,(45,100)),(240,110))
        elif display == 3:
            en = font2.render('Skelly:',1, (255,0,0))
            surface.blit(en, (50,40))
            surface.blit(pygame.transform.scale(goblin,(45,100)),(240,110))

        if stand == 2:
            if self.idlecount + 1 >= 5:
                self.idlecount = 0
                stand = 1
            surface.blit(atk1[self.idlecount//1], (50,250))
            surface.blit(pygame.transform.scale(hit,(45,50)),(240,120))

            #resize char sprite using transform in a every list index (width,height)
            self.idlecount += 1
            

            
           
        if stand == 3:
            if self.idlecount + 1 >= 5:
                self.idlecount = 0
                stand = 1
            surface.blit(atk2[self.idlecount//1], (50,250))
            surface.blit(pygame.transform.scale(hit,(45,50)),(250,120))

            #resize char sprite using transform in a every list index (width,height)
            self.idlecount += 1
            
        if ally:
            surface.blit(pygame.transform.scale(bird,(100,90)),(120,265))
        if ally2:
            surface.blit(pygame.transform.scale(al2,(128,128)),(180,230))


        
def message_to_screen(msg,color):
    #call this just to display text on mudaf screen
    screen_text = font.render(msg, True, color)
    surface.blit(screen_text, [(700/2),(500/2)])
    
#wala pani klaro part
def hit_damage():
    global gold, damage, enemyh
    if gold >= 200:
        pygame.mixer.Sound.play(incre)
        FadeIn(dd[0])
        pygame.mixer.Sound.play(coin)
        #enemyh -=20
        damage += 1
        gold = gold - 200
        print(enemyh)
    elif gold > 200:
        print("Need More Gold!")
        pygame.mixer.Sound.play(weneed)
        FadeIn(goldfish[0])




#for critical hit
def critical():
    global enemyh
    critical = random.randint(1,7)
    bonus = random.randint(1,10)
    if critical == 4:
        enemyh -= critical * damage
        post = critical * damage
        print("Critical Hit!", post)
    if bonus == 5:
        enemyh -= bonus * damage
        post = critical * damage
        print("Critical Hit!", post)


def shop_ally_healer():
    global ally2, gold
    if gold >= 250:
        pygame.mixer.Sound.play(join)
        FadeIn(rank[0])
        
        pygame.mixer.Sound.play(healerjoin)
        print("Healer ally joined the rank")
        gold = gold - 250
        ally2 = True
    elif gold < 250:
        print("Need More Gold!")
        pygame.mixer.Sound.play(weneed)
        FadeIn(goldfish[0])


def Ally_interval_attack():
    global ally, gold
    if gold >= 300:
        pygame.mixer.Sound.play(coin)
        pygame.mixer.Sound.play(join)
        pygame.mixer.Sound.play(fireegg)
        FadeIn(rank[0])
        print("Basic ally joined the rank")
        gold = gold - 300
        ally = True
    elif gold < 300:
        print("Need More Gold!")
        pygame.mixer.Sound.play(weneed)
        FadeIn(goldfish[0])

#For ally interval attack
def attack_ally():
    global basic_ally_damage, enemyh
    enemyh -= basic_ally_damage


    

#instantly kills the enemy but cannot be used against the boss        
def shop_instant_kill():
    global gold, enemyh, round_count
    if gold >= 200:
        pygame.mixer.Sound.play(pop)
        FadeIn(ff[0])
        pygame.mixer.Sound.play(coin)
        #if round_count < 30:
        enemyh -= enemyh
        gold = gold - 200
        print("Enemy popped!")
        """
        elif round_count == 30:
            enemyh -= 0
            print("Can't use instant kill on boss")
        """
    elif gold < 200:
        print("Need More Gold!")
        pygame.mixer.Sound.play(weneed)
        FadeIn(goldfish[0])



def FadeIn(FADE_FX):
    hi = 250
    hero = Battle(50,250,64,64)
    for FADED in range(0,10):
        #FADE_FX.set_alpha(FADED)
        hero.asset()
        surface.blit(FADE_FX,(50,hi))
        hi +=1
        pygame.time.delay(1)
        pygame.display.flip()
        

def FadeEn(FADE_FX):
    hi = 240
    ho = 110
    hero = Battle(50,250,64,64)
    for FADED in range(0,22):
        #FADE_FX.set_alpha(FADED)
        hero.asset()
        surface.blit(FADE_FX,(hi,ho))
        hi -=6
        ho +=6
        pygame.display.flip()        
    

def FadeOn(FADE_FX):
    hi = 180
    ho = 270
    hero = Battle(50,250,64,64)
    for FADED in range(0,22):
        #FADE_FX.set_alpha(FADED)
        hero.asset()
        surface.blit(FADE_FX,(hi,ho))
        hi +=3
        ho -=6
        pygame.display.flip() 





    
    

       
hero = Battle(50,250,64,64)


def game_loop():
    global done, enemyh, eattack, gold, damage, stand, display, ally1_attack, round_count, Full, ally, ally2, ally2_attack,modify
    pygame.mixer.music.play(-1)
    
    main_menu.disable()
    main_menu.reset(1)
    while not done:
        clock.tick(60)
        game_loop = pygame.event.get()
        for event in game_loop:
            if event.type == QUIT:
                done = True
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_x:
                    stand = 2
                    pygame.mixer.Sound.play(punch)
                    enemyh -= damage
                    print(enemyh)
                    critical()
                   
                    
                if event.key == K_z:
                    stand = 3
                    pygame.mixer.Sound.play(punch)
                    enemyh -= damage
                    print(enemyh)
                    critical()
               
                if event.key == K_d:
                   hit_damage()
                if event.key == K_a:
                    hero.shop_healthpartial()
                if event.key == K_s:
                    hero.shop_greedy()
                    
                if event.key == K_f:
                    shop_instant_kill()
                    
                if event.key == K_g:
                    Ally_interval_attack()
                if event.key == K_h:
                    shop_ally_healer()
                if event.key == K_r and not Full:
                    game_loop()

                if event.key == K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()
                    

       
        hero.asset()
        hero.Health()
        pygame.display.flip()

        if round_count == 30:
            modify = 30

        if round_count == 50:
            modify = 20

        
        eattack -=1 #Countdown player damage
        if eattack == 0: #countdown p dmg
            if display == 1:
                pygame.mixer.Sound.play(flower3)
                FadeEn(flower1)
            if display == 2:
                pygame.mixer.Sound.play(wolf3)
                FadeEn(wolf1)
            if display == 3:
                pygame.mixer.Sound.play(goblin3)
                FadeEn(goblin1)

                
            hero.enemy_attack()
            eattack = modify
            if ally:
                attack_ally()
                pygame.mixer.Sound.play(fireegg)
                pygame.mixer.Sound.play(fire)
                FadeOn(fireball[0])
                print("Ally attacked")
                print(enemyh)
        if eattack == 20:
            if ally2:
                hero.healer_fack()
                pygame.mixer.Sound.play(healervoice)
                FadeIn(hail[0])
                pygame.mixer.Sound.play(healeratk)
                print("Ally healed 30 HP")
        clock.tick(30)
        
        #Pass the events to main_menu
        main_menu.mainloop(game_loop)
   
   

    
    hero.health += 100
    done = False
    ally = False
    ally2 = False
    Full = True
    damage = 1
    gold = 20
    player_count = 0
    round_count = 0
    surface.fill((255,255,255))
    message_to_screen("We Lost", red)
    pygame.display.flip()
    clock.tick(15)




def high_scoress():
    global round_count 
    with_highscore.highscore(surface, 'Highscore.txt', round_count)
        
    




def main_background():
    #surface.fill(COLOR_BACKGROUND)
    surface.blit(pygame.transform.scale(bg1,(700,500)),(0,0))






about_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='About',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0])

for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option('Return to menu', PYGAME_MENU_BACK)





#This structure is from the imported pygame menu module
main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Main menu',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Play', game_loop)
main_menu.add_option('About', about_menu)
main_menu.add_option('High Scores', high_scoress)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)





while True:

    # Tick
    clock.tick(60)

    # Application events
    events = pygame.event.get()
    for e in events:
        if e.type == QUIT:
            exit()

    # Main menu
    main_menu.mainloop(events)
    # Flip surface
    pygame.display.flip()
