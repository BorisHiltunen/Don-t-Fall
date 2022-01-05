"""
game_data.py:
Initializes and preserves the needed attributes for future use.
"""

import pygame
from app import file_management
from app import path_management

pygame.init()

calculations = [
    "0 + 0 = ?", "0 + 1 = ?", "1 + 0 = ?",
    "0 + 2 = ?", "2 + 0 = ?", "1 + 1 = ?",
    "0 + 3 = ?", "1 + 2 = ?", "2 + 1 = ?",
    "3 + 0 = ?"
    ]
all_cubes = [
    (0, (300, 150)), (1, (200, 250)), (2, (300, 250)),
    (3, (400, 250)), (4, (200, 350)), (5, (300, 350)),
    (6, (400, 350)), (7, (200, 450)), (8, (300, 450)),
    (9, (400, 450)), (10, (300, 550))
    ]
right_path = []
chosen_answers = {}
chosen_calculations = {}

width = 640
height = 700
x = 313
y = 563
movement_x = False
movement_y = False
cube_x = False
cube_y = False
cube = ""

right = False
left = False
down = False
up = False

locked = False
sound_lock = False
done = False

display = pygame.display.set_mode((width, height))

pygame.display.set_caption("Don't Fall")

file_management.download_pictures()
file_management.sound_management()
path_management.path_manager()
