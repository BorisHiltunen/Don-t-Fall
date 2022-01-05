"""
cube_management:
file that contains function for game's cube's functionality.
"""

import pygame
from app import game_data


def cube_manager():
    """
    Function that is responsibe
    for making the cubes work as intended.
    """

    fontt = pygame.font.SysFont("Arial", 50)

    pygame.draw.rect(game_data.display, (0, 170, 50), (40, 89, 220, 80))
    game_data.display.blit(game_data.calculation_board, (40, 89))

    count = 0

    while count < 11:
        first_condition_for_cube_x = game_data.all_cubes[count][1][0] >= \
            game_data.x-game_data.ball.get_width()
        second_condition_for_cube_x = game_data.all_cubes[count][1][0] <= \
            game_data.x+game_data.ball.get_width()
        game_data.cube_x = first_condition_for_cube_x and \
            second_condition_for_cube_x

        first_condition_for_cube_y = game_data.all_cubes[count][1][1] >= \
            game_data.y-game_data.ball.get_height()
        second_condition_for_cube_y = game_data.all_cubes[count][1][1] <= \
            game_data.y+game_data.ball.get_height()
        game_data.cube_y = first_condition_for_cube_y and \
            second_condition_for_cube_y

        if game_data.cube_x and game_data.cube_y:
            if count in game_data.right_path:
                if count == 0:
                    game_data.win.play()
                else:
                    if game_data.sound_lock is False:
                        game_data.creak.play()
                        game_data.sound_lock = True
                    text = fontt.render(
                        f"{game_data.chosen_calculations[count]}",
                        True,
                        (255, 255, 255)
                        )
                    game_data.display.blit(text, (50, 100))
                game_data.cube = game_data.display.blit(
                    game_data.wooden_slab_down,
                    (
                        game_data.all_cubes[count][1][0],
                        game_data.all_cubes[count][1][1]
                        )
                    )
            else:
                if game_data.sound_lock is False:
                    game_data.fall.play()
                    game_data.sound_lock = True
                game_data.x = 313
                game_data.y = 563
        else:
            if count in game_data.right_path:
                if game_data.chosen_answers[count] == 0:
                    game_data.cube = game_data.display.blit(
                        game_data.normal0,
                        (
                            game_data.all_cubes[count][1][0],
                            game_data.all_cubes[count][1][1]
                            )
                        )
                elif game_data.chosen_answers[count] == 1:
                    game_data.cube = game_data.display.blit(
                        game_data.normal1,
                        (
                            game_data.all_cubes[count][1][0],
                            game_data.all_cubes[count][1][1]
                            )
                        )
                elif game_data.chosen_answers[count] == 2:
                    game_data.cube = game_data.display.blit(
                        game_data.normal2,
                        (
                            game_data.all_cubes[count][1][0],
                            game_data.all_cubes[count][1][1]
                            )
                        )
                elif game_data.chosen_answers[count] == 3:
                    game_data.cube = game_data.display.blit(
                        game_data.normal3,
                        (
                            game_data.all_cubes[count][1][0],
                            game_data.all_cubes[count][1][1]
                            )
                        )
            else:
                if game_data.numbers[count] == 0:
                    game_data.cube = game_data.display.blit(
                        game_data.normal0, (
                            game_data.all_cubes[count][1][0],
                            game_data.all_cubes[count][1][1]
                            )
                        )
                elif game_data.numbers[count] == 1:
                    game_data.cube = game_data.display.blit(
                        game_data.normal1, (
                            game_data.all_cubes[count][1][0],
                            game_data.all_cubes[count][1][1]
                            )
                        )
                elif game_data.numbers[count] == 2:
                    game_data.cube = game_data.display.blit(
                        game_data.normal2, (
                            game_data.all_cubes[count][1][0],
                            game_data.all_cubes[count][1][1]
                            )
                        )
                elif game_data.numbers[count] == 3:
                    game_data.cube = game_data.display.blit(
                        game_data.normal3, (
                            game_data.all_cubes[count][1][0],
                            game_data.all_cubes[count][1][1]
                            )
                        )
        count += 1
