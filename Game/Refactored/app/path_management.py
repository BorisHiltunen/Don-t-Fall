"""
path_management:
contains function that initializes the game's correct path.
"""

from random import randint
from app import game_data


def path_manager():
    """Function that initializes the correct path."""

    eight = [7, 5, 9]
    six = [5, 3]
    five = [4, 2, 6]
    four = [1, 5]

    game_data.right_path.append(10)

    while True:
        if game_data.right_path[len(game_data.right_path)-1] == 10:
            game_data.right_path.append(8)
        if game_data.right_path[len(game_data.right_path)-1] == 9:
            game_data.right_path.append(6)
        if game_data.right_path[len(game_data.right_path)-1] == 8:
            game_data.right_path.append(eight[randint(0, 2)])
        if game_data.right_path[len(game_data.right_path)-1] == 7:
            game_data.right_path.append(4)
        if game_data.right_path[len(game_data.right_path)-1] == 6:
            game_data.right_path.append(six[randint(0, 1)])
        if game_data.right_path[len(game_data.right_path)-1] == 5:
            game_data.right_path.append(five[randint(0, 2)])
        if game_data.right_path[len(game_data.right_path)-1] == 4:
            game_data.right_path.append(four[randint(0, 1)])
        if game_data.right_path[len(game_data.right_path)-1] == 3:
            game_data.right_path.append(2)
        if game_data.right_path[len(game_data.right_path)-1] == 2:
            game_data.right_path.append(0)
            break
        if game_data.right_path[len(game_data.right_path)-1] == 1:
            game_data.right_path.append(2)

    game_data.right_path.append(0)

    for number in game_data.right_path:
        game_data.chosen_answers[number] = randint(0, 3)

        game_data.numbers = []

        while len(game_data.numbers) < 11:
            game_data.numbers.append(randint(0, 3))

    for number in game_data.chosen_answers:
        if game_data.chosen_answers[
                game_data.right_path[
                    game_data.right_path.index(number) + 1]] == 0:
            game_data.chosen_calculations[
                number] = game_data.calculations[0]
        if game_data.chosen_answers[
                game_data.right_path[
                    game_data.right_path.index(number) + 1]] == 1:
            game_data.chosen_calculations[
                number] = game_data.calculations[randint(1, 2)]
        if game_data.chosen_answers[
                game_data.right_path[
                    game_data.right_path.index(number) + 1]] == 2:
            game_data.chosen_calculations[
                number] = game_data.calculations[randint(3, 5)]
        if game_data.chosen_answers[
                game_data.right_path[
                    game_data.right_path.index(number) + 1]] == 3:
            game_data.chosen_calculations[
                number] = game_data.calculations[randint(6, 9)]
