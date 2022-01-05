"""
file_management.py:
File that contains two functions that initialize files.
"""

from app import game_data
import os
import pygame


def download_pictures():
    """Function that downloads pictures."""

    game_data.background = pygame.image.load(
        os.path.join("images", "background.png")
        )
    game_data.calculation_board = pygame.image.load(
        os.path.join("images", "calculation_board.png")
        )
    game_data.normal0 = pygame.image.load(
        os.path.join("images", "normal_wooden_slab0.png")
        )
    game_data.normal1 = pygame.image.load(
        os.path.join("images", "normal_wooden_slab1.png")
        )
    game_data.normal2 = pygame.image.load(
        os.path.join("images", "normal_wooden_slab2.png")
        )
    game_data.normal3 = pygame.image.load(
        os.path.join("images", "normal_wooden_slab3.png")
        )
    game_data.ball = pygame.image.load(
        os.path.join("images", "ball_on_wooden_slab.png")
        )
    game_data.wooden_slab_down = pygame.image.load(
        os.path.join("images", "wooden_slab_down.png")
        )


def sound_management():
    """Function that initializes game's music and sounds."""

    game_data.creak = pygame.mixer.Sound(
        os.path.join("sounds", "thud1.wav")
        )
    game_data.fall = pygame.mixer.Sound(
        os.path.join("sounds", "falling.wav")
        )
    game_data.win = pygame.mixer.Sound(
        os.path.join("sounds", "won.wav")
        )
    game_data.music = pygame.mixer.music.load(
        os.path.join("music", "music.wav")
        )

    pygame.mixer.music.play(loops=-1)
