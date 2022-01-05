"""main.py: Contains DontFall class."""

from random import randint
import pygame


class DontFall:
    """
    Class that contains necessary functions
    to make DontFall app work as intended.
    """

    def __init__(self):
        pygame.init()

        self.calculations = [
            "0 + 0 = ?", "0 + 1 = ?", "1 + 0 = ?",
            "0 + 2 = ?", "2 + 0 = ?", "1 + 1 = ?",
            "0 + 3 = ?", "1 + 2 = ?", "2 + 1 = ?",
            "3 + 0 = ?"
            ]
        self.all_cubes = [
            (0, (300, 150)), (1, (200, 250)), (2, (300, 250)),
            (3, (400, 250)), (4, (200, 350)), (5, (300, 350)),
            (6, (400, 350)), (7, (200, 450)), (8, (300, 450)),
            (9, (400, 450)), (10, (300, 550))
            ]
        self.right_path = []
        self.chosen_answers = {}
        self.chosen_calculations = {}

        self.width = 640
        self.height = 700
        self.x = 313
        self.y = 563
        self.movement_x = False
        self.movement_y = False
        self.cube_x = False
        self.cube_y = False
        self.cube = ""

        self.right = False
        self.left = False
        self.down = False
        self.up = False

        self.locked = False
        self.sound_lock = False
        self.done = False

        self.display = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Don't Fall")

        self.download_pictures()
        self.sound_management()
        self.path_management()
        self.loop()

    def download_pictures(self):
        """Function that downloads pictures."""

        self.background = pygame.image.load("background.png")
        self.calculation_board = pygame.image.load("calculation_board.png")
        self.normal0 = pygame.image.load("normal_wooden_slab0.png")
        self.normal1 = pygame.image.load("normal_wooden_slab1.png")
        self.normal2 = pygame.image.load("normal_wooden_slab2.png")
        self.normal3 = pygame.image.load("normal_wooden_slab3.png")
        self.ball = pygame.image.load("ball_on_wooden_slab.png")
        self.wooden_slab_down = pygame.image.load("wooden_slab_down.png")

    def sound_management(self):
        """Function that initializes game's music and sounds."""

        self.creak = pygame.mixer.Sound("thud1.wav")
        self.fall = pygame.mixer.Sound("falling.wav")
        self.win = pygame.mixer.Sound("won.wav")
        self.music = pygame.mixer.music.load("music.wav")

        pygame.mixer.music.play(loops=-1)

    def path_management(self):
        """Function that initializes the correct path."""

        eight = [7, 5, 9]
        six = [5, 3]
        five = [4, 2, 6]
        four = [1, 5]

        self.right_path.append(10)

        while True:
            if self.right_path[len(self.right_path)-1] == 10:
                self.right_path.append(8)
            if self.right_path[len(self.right_path)-1] == 9:
                self.right_path.append(6)
            if self.right_path[len(self.right_path)-1] == 8:
                self.right_path.append(eight[randint(0, 2)])
            if self.right_path[len(self.right_path)-1] == 7:
                self.right_path.append(4)
            if self.right_path[len(self.right_path)-1] == 6:
                self.right_path.append(six[randint(0, 1)])
            if self.right_path[len(self.right_path)-1] == 5:
                self.right_path.append(five[randint(0, 2)])
            if self.right_path[len(self.right_path)-1] == 4:
                self.right_path.append(four[randint(0, 1)])
            if self.right_path[len(self.right_path)-1] == 3:
                self.right_path.append(2)
            if self.right_path[len(self.right_path)-1] == 2:
                self.right_path.append(0)
                break
            if self.right_path[len(self.right_path)-1] == 1:
                self.right_path.append(2)

        self.right_path.append(0)

        for number in self.right_path:
            self.chosen_answers[number] = randint(0, 3)

        self.numbers = []

        while len(self.numbers) < 11:
            self.numbers.append(randint(0, 3))

        for number in self.chosen_answers:
            if self.chosen_answers[
                    self.right_path[self.right_path.index(number) + 1]] == 0:
                self.chosen_calculations[
                    number] = self.calculations[0]
            if self.chosen_answers[
                    self.right_path[self.right_path.index(number) + 1]] == 1:
                self.chosen_calculations[
                    number] = self.calculations[randint(1, 2)]
            if self.chosen_answers[
                    self.right_path[self.right_path.index(number) + 1]] == 2:
                self.chosen_calculations[
                    number] = self.calculations[randint(3, 5)]
            if self.chosen_answers[
                    self.right_path[self.right_path.index(number) + 1]] == 3:
                self.chosen_calculations[
                    number] = self.calculations[randint(6, 9)]

    def cube_management(self):
        """
        Function that is responsibe
        for making the cubes work as intended.
        """

        fontt = pygame.font.SysFont("Arial", 50)

        pygame.draw.rect(self.display, (0, 170, 50), (40, 89, 220, 80))
        self.display.blit(self.calculation_board, (40, 89))

        count = 0

        while count < 11:
            first_condition_for_cube_x = self.all_cubes[count][1][0] >= \
                self.x-self.ball.get_width()
            second_condition_for_cube_x = self.all_cubes[count][1][0] <= \
                self.x+self.ball.get_width()
            self.cube_x = first_condition_for_cube_x and \
                second_condition_for_cube_x

            first_condition_for_cube_y = self.all_cubes[count][1][1] >= \
                self.y-self.ball.get_height()
            second_condition_for_cube_y = self.all_cubes[count][1][1] <= \
                self.y+self.ball.get_height()
            self.cube_y = first_condition_for_cube_y and \
                second_condition_for_cube_y

            if self.cube_x and self.cube_y:
                if count in self.right_path:
                    if count == 0:
                        self.win.play()
                    else:
                        if self.sound_lock is False:
                            self.creak.play()
                            self.sound_lock = True
                        text = fontt.render(
                            f"{self.chosen_calculations[count]}",
                            True,
                            (255, 255, 255)
                            )
                        self.display.blit(text, (50, 100))
                    self.cube = self.display.blit(
                        self.wooden_slab_down,
                        (
                            self.all_cubes[count][1][0],
                            self.all_cubes[count][1][1]
                            )
                        )
                else:
                    if self.sound_lock is False:
                        self.fall.play()
                        self.sound_lock = True
                    self.x = 313
                    self.y = 563
            else:
                if count in self.right_path:
                    if self.chosen_answers[count] == 0:
                        self.cube = self.display.blit(
                            self.normal0,
                            (
                                self.all_cubes[count][1][0],
                                self.all_cubes[count][1][1]
                                )
                            )
                    elif self.chosen_answers[count] == 1:
                        self.cube = self.display.blit(
                            self.normal1,
                            (
                                self.all_cubes[count][1][0],
                                self.all_cubes[count][1][1]
                                )
                            )
                    elif self.chosen_answers[count] == 2:
                        self.cube = self.display.blit(
                            self.normal2,
                            (
                                self.all_cubes[count][1][0],
                                self.all_cubes[count][1][1]
                                )
                            )
                    elif self.chosen_answers[count] == 3:
                        self.cube = self.display.blit(
                            self.normal3,
                            (
                                self.all_cubes[count][1][0],
                                self.all_cubes[count][1][1]
                                )
                            )
                else:
                    if self.numbers[count] == 0:
                        self.cube = self.display.blit(
                            self.normal0, (
                                self.all_cubes[count][1][0],
                                self.all_cubes[count][1][1]
                                )
                            )
                    elif self.numbers[count] == 1:
                        self.cube = self.display.blit(
                            self.normal1, (
                                self.all_cubes[count][1][0],
                                self.all_cubes[count][1][1]
                                )
                            )
                    elif self.numbers[count] == 2:
                        self.cube = self.display.blit(
                            self.normal2, (
                                self.all_cubes[count][1][0],
                                self.all_cubes[count][1][1]
                                )
                            )
                    elif self.numbers[count] == 3:
                        self.cube = self.display.blit(
                            self.normal3, (
                                self.all_cubes[count][1][0],
                                self.all_cubes[count][1][1]
                                )
                            )
            count += 1

    def win_message(self):
        """Function that prints that you won the game if you did."""

        print("you won!")

    def loop(self):
        """
        Function that loops over and over
        Thus making the game flow.
        """

        clock = pygame.time.Clock()

        while True:

            self.draw_the_game()
            self.analyse_events()

            clock.tick(60)

            if self.done:
                self.win_message()
                break

    def analyse_events(self):
        """
        Function that is mostly responsible
        for the way the character is moving.
        """

        count = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_DOWN:
                    self.down = True
                self.sound_lock = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False
                if event.key == pygame.K_UP:
                    self.up = False
                if event.key == pygame.K_DOWN:
                    self.down = False
                self.locked = False
            if event.type == pygame.QUIT:
                exit()

        if self.locked is False:
            if self.y == 163:
                for i in range(70999999):
                    if i == 70999998:
                        self.done = True
            while count < 11:
                if self.up:
                    if self.locked is False:
                        first_condition_for_movement_x = (
                            self.all_cubes[count][1][0] >=
                            self.x-self.ball.get_width()
                            )
                        second_condition_for_movement_x = (
                            self.all_cubes[count][1][0] <=
                            self.x+self.ball.get_width()
                            )
                        self.movement_x = (
                            first_condition_for_movement_x and
                            second_condition_for_movement_x
                            )

                        first_condition_for_movement_y = (
                            self.all_cubes[count][1][1] >=
                            (self.y-100)-self.ball.get_height()
                            )
                        second_condition_for_movement_y = (
                            self.all_cubes[count][1][1] <=
                            (self.y-100)+self.ball.get_height()
                            )
                        self.movement_y = (
                            first_condition_for_movement_y and
                            second_condition_for_movement_y
                            )
                        if self.movement_x and self.movement_y:
                            self.y -= 100
                            self.locked = True
                if self.right:
                    if self.locked is False:
                        first_condition_for_movement_x = (
                            self.all_cubes[count][1][0] >=
                            (self.x+100)-self.ball.get_width()
                            )
                        second_condition_for_movement_x = (
                            self.all_cubes[count][1][0] <=
                            (self.x+100)+self.ball.get_width()
                            )
                        self.movement_x = (
                            first_condition_for_movement_x and
                            second_condition_for_movement_x
                            )

                        first_condition_for_movement_y = (
                            self.all_cubes[count][1][1] >=
                            self.y-self.ball.get_height()
                            )
                        second_condition_for_movement_y = (
                            self.all_cubes[count][1][1] <=
                            self.y+self.ball.get_height()
                            )
                        self.movement_y = (
                            first_condition_for_movement_y and
                            second_condition_for_movement_y
                            )
                        if self.movement_x and self.movement_y:
                            self.x += 100
                            self.locked = True
                if self.down:
                    if self.locked is False:
                        first_condition_for_movement_x = (
                            self.all_cubes[count][1][0] >=
                            self.x-self.ball.get_width()
                            )
                        second_condition_for_movement_x = (
                            self.all_cubes[count][1][0] <=
                            self.x+self.ball.get_width()
                            )
                        self.movement_x = (
                            first_condition_for_movement_x and
                            second_condition_for_movement_x
                            )

                        first_condition_for_movement_y = (
                            self.all_cubes[count][1][1] >=
                            (self.y+100)-self.ball.get_height()
                            )
                        second_condition_for_movement_y = (
                            self.all_cubes[count][1][1] <=
                            (self.y+100)+self.ball.get_height()
                            )
                        self.movement_y = (
                            first_condition_for_movement_y and
                            second_condition_for_movement_y
                            )
                        if self.movement_x and self.movement_y:
                            self.y += 100
                            self.locked = True
                if self.left:
                    if self.locked is False:
                        first_condition_for_movement_x = (
                            self.all_cubes[count][1][0] >=
                            (self.x-100)-self.ball.get_width()
                            )
                        second_condition_for_movement_x = (
                            self.all_cubes[count][1][0] <=
                            (self.x-100)+self.ball.get_width()
                            )
                        self.movement_x = (
                            first_condition_for_movement_x and
                            second_condition_for_movement_x
                            )

                        first_condition_for_movement_y = (
                            self.all_cubes[count][1][1] >=
                            self.y-self.ball.get_height()
                            )
                        second_condition_for_movement_y = (
                            self.all_cubes[count][1][1] <=
                            self.y+self.ball.get_height()
                            )
                        self.movement_y = (
                            first_condition_for_movement_y and
                            second_condition_for_movement_y
                            )
                        if self.movement_x and self.movement_y:
                            self.x -= 100
                            self.locked = True
                count += 1

    def draw_the_game(self):
        """Function that basically draws the game."""

        self.display.fill((0, 100, 100))

        self.display.blit(self.background, (0, 0))

        self.cube_management()

        self.display.blit(
            self.ball,
            (self.x, self.y)
            )

        pygame.display.flip()


if __name__ == "__main__":
    DontFall()
