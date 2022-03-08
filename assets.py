import pygame
import os

#vs spaceships
RED_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'clipart', 'enemy_ship_red.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'clipart', 'enemy_ship_blue.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'clipart', 'enemy_ship_green.png'))

#player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'clipart', 'player_ship_yellow.png'))

#Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))