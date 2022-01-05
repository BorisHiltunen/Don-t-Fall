"""
roller.py: file that contains two functions.
One for sending a message if the player won
and the other one for looping over and over
thus making the game flow.
"""

import pygame
from app import game_data
from app import game_visualizer
from app import event_analyser


def win_message():
    """Function that prints that you won the game if you did."""

    print("you won!")


def loop():
    """
    Function that loops over and over
    Thus making the game flow.
    """

    clock = pygame.time.Clock()

    while True:

        game_visualizer.draw_the_game()
        event_analyser.analyse_events()

        clock.tick(60)

        if game_data.done:
            win_message()
            break
