from multiprocessing import set_forkserver_preload
import pygame
import os
import time
import random

#enable font usage
pygame.font.init()

#game constants
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE INVADERS")

from assets import *

#background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-galaxy.jpeg")), (WIDTH, HEIGHT))

class Ship():
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.width = 50
        self.height = 50

    def draw(self, window):
       window.blit(self.ship_img, (self.x, self.y)) #draw ship in the given position

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health  
        self.width = self.get_width()
        self.height = self.get_height()

class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color] #spawn ship based on the color passed to the class
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel #move enemy ships only from top to bottom, no side wise movement


def main():
    run = True #game running status
    FPS = 60 #frame-per-second
    level = 1 #game level
    lives = 5 #player lives

    main_font = pygame.font.SysFont("comicsans", 20)
    lost_font = pygame.font.SysFont("comicsans", 30) 

    enemies = [] #spawened enemy list, blank at start
    wave_length = 5 #how many enemies to be spawned at each enemy wave
    enemy_vel = 3 #speed of enemy ships
    
    player_vel = 5 #speed of player ship movement

    player = Player(300, 650) #spawn player ship at this co-ordinate at the start of the game

    lost = False # lost status
    lost_count = 0 # for the lost screen to be displayed for that amount of seconds

    clock = pygame.time.Clock()

    def redraw_window():
        #update
        WIN.blit(BG, (0,0)) #top-left corner of window

        #draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255)) #1 = anti-aliasing 
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255)) #1 = anti-aliasing

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        #check if player has lost
        if lost:
            lost_label = lost_font.render("You Lost!", 1, (255,0,0)) #show message in white
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 - lost_label.get_height()/2)) #at the middle of the screen
        
        pygame.display.update()

    while run:
        clock.tick(FPS) #to run the game at same speed accross different devices
        redraw_window()

        #check if player is out of life or health
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1 #increase lost count

        if lost:
            if lost_count > FPS * 3: #pause window for 3 seconds and quit game
                run = False
            else:
                continue
        
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(100, WIDTH - 100), random.randrange(-1500, -100), random.choice(["red","blue","green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #quit game when user closes window
                run = False

        #move ship
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0: #left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.width < WIDTH: #right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0: #up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.height < HEIGHT: #down
            player.y += player_vel

        #move enemies from top of screen to bottom
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if(enemy.y - enemy.get_height() > HEIGHT): #check if enemy crosses the bottom limit
                lives -= 1 #reduce player life by 1
                enemies.remove(enemy) #remove this enemy from the enemies list as it has won
            


main()

