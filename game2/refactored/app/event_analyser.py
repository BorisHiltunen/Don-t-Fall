"""event_analyser.py: Contains function that analyses the game's events."""

import pygame
from app import game_data


def analyse_events():
    """
    Function that is mostly responsible
    for the way the character is moving.
    """

    count = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_data.left = True
            if event.key == pygame.K_RIGHT:
                game_data.right = True
            if event.key == pygame.K_UP:
                game_data.up = True
            if event.key == pygame.K_DOWN:
                game_data.down = True
            game_data.sound_lock = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                game_data.left = False
            if event.key == pygame.K_RIGHT:
                game_data.right = False
            if event.key == pygame.K_UP:
                game_data.up = False
            if event.key == pygame.K_DOWN:
                game_data.down = False
            game_data.locked = False
        if event.type == pygame.QUIT:
            exit()

    if game_data.locked is False:
        if game_data.y == 163:
            for i in range(70999999):
                if i == 70999998:
                    game_data.done = True
        while count < 11:
            if game_data.up:
                if game_data.locked is False:
                    first_condition_for_movement_x = (
                        game_data.all_cubes[count][1][0] >=
                        game_data.x-game_data.ball.get_width()
                        )
                    second_condition_for_movement_x = (
                        game_data.all_cubes[count][1][0] <=
                        game_data.x+game_data.ball.get_width()
                        )
                    game_data.movement_x = (
                        first_condition_for_movement_x and
                        second_condition_for_movement_x
                        )

                    first_condition_for_movement_y = (
                        game_data.all_cubes[count][1][1] >=
                        (game_data.y-100)-game_data.ball.get_height()
                        )
                    second_condition_for_movement_y = (
                        game_data.all_cubes[count][1][1] <=
                        (game_data.y-100)+game_data.ball.get_height()
                        )
                    game_data.movement_y = (
                        first_condition_for_movement_y and
                        second_condition_for_movement_y
                        )
                    if game_data.movement_x and game_data.movement_y:
                        game_data.y -= 100
                        game_data.locked = True
            if game_data.right:
                if game_data.locked is False:
                    first_condition_for_movement_x = (
                        game_data.all_cubes[count][1][0] >=
                        (game_data.x+100)-game_data.ball.get_width()
                        )
                    second_condition_for_movement_x = (
                        game_data.all_cubes[count][1][0] <=
                        (game_data.x+100)+game_data.ball.get_width()
                        )
                    game_data.movement_x = (
                        first_condition_for_movement_x and
                        second_condition_for_movement_x
                        )

                    first_condition_for_movement_y = (
                        game_data.all_cubes[count][1][1] >=
                        game_data.y-game_data.ball.get_height()
                        )
                    second_condition_for_movement_y = (
                        game_data.all_cubes[count][1][1] <=
                        game_data.y+game_data.ball.get_height()
                        )
                    game_data.movement_y = (
                        first_condition_for_movement_y and
                        second_condition_for_movement_y
                        )
                    if game_data.movement_x and game_data.movement_y:
                        game_data.x += 100
                        game_data.locked = True
            if game_data.down:
                if game_data.locked is False:
                    first_condition_for_movement_x = (
                        game_data.all_cubes[count][1][0] >=
                        game_data.x-game_data.ball.get_width()
                        )
                    second_condition_for_movement_x = (
                        game_data.all_cubes[count][1][0] <=
                        game_data.x+game_data.ball.get_width()
                        )
                    game_data.movement_x = (
                        first_condition_for_movement_x and
                        second_condition_for_movement_x
                        )

                    first_condition_for_movement_y = (
                        game_data.all_cubes[count][1][1] >=
                        (game_data.y+100)-game_data.ball.get_height()
                        )
                    second_condition_for_movement_y = (
                        game_data.all_cubes[count][1][1] <=
                        (game_data.y+100)+game_data.ball.get_height()
                        )
                    game_data.movement_y = (
                        first_condition_for_movement_y and
                        second_condition_for_movement_y
                        )
                    if game_data.movement_x and game_data.movement_y:
                        game_data.y += 100
                        game_data.locked = True
            if game_data.left:
                if game_data.locked is False:
                    first_condition_for_movement_x = (
                        game_data.all_cubes[count][1][0] >=
                        (game_data.x-100)-game_data.ball.get_width()
                        )
                    second_condition_for_movement_x = (
                        game_data.all_cubes[count][1][0] <=
                        (game_data.x-100)+game_data.ball.get_width()
                        )
                    game_data.movement_x = (
                        first_condition_for_movement_x and
                        second_condition_for_movement_x
                        )

                    first_condition_for_movement_y = (
                        game_data.all_cubes[count][1][1] >=
                        game_data.y-game_data.ball.get_height()
                        )
                    second_condition_for_movement_y = (
                        game_data.all_cubes[count][1][1] <=
                        game_data.y+game_data.ball.get_height()
                        )
                    game_data.movement_y = (
                        first_condition_for_movement_y and
                        second_condition_for_movement_y
                        )
                    if game_data.movement_x and game_data.movement_y:
                        game_data.x -= 100
                        game_data.locked = True
            count += 1
