"""
game_visualizer:
File that contains function that basically draws the game.
"""

from app import game_data
from app import cube_management
import pygame


def draw_the_game():
    """Function that basically draws the game."""

    game_data.display.fill((0, 100, 100))

    game_data.display.blit(game_data.background, (0, 0))

    cube_management.cube_manager()

    game_data.display.blit(
        game_data.ball,
        (game_data.x, game_data.y)
        )

    pygame.display.flip()
