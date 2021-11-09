#Importing necessary modules or methods
import pygame
from random import randint

class DontFall:
    #Initializing necessary attributes
    def __init__(self):
        #Initializes all imported pygame modules
        pygame.init()

        #Accessing funktion that downloads pictures
        self.download_pictures()

        #Testing sound and music mechanincs for the game

        #Initializing sounds
        self.creak = pygame.mixer.Sound('creak2.wav')
        self.fall = pygame.mixer.Sound('fall.wav')
        self.win = pygame.mixer.Sound('win.wav')

        #Initializing music
        #self.music = pygame.mixer.music.load('music.wav')
        #pygame.mixer.music.play(-1)

        #Here are the needed calculations inside a list in ascending order
        self.calculations = ["0 + 0 = ?", "0 + 1 = ?", "1 + 0 = ?", "0 + 2 = ?", "2 + 0 = ?", "1 + 1 = ?", "0 + 3 = ?", "1 + 2 = ?", "2 + 1 = ?", "3 + 0 = ?"]

        #NB
        #Right now there are two initializions for attribue self.all_cubes

        #Initializing a list called self.all_cubes containing the numbers 0-10
        self.all_cubes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        #Every possible option for the game's right path
        #10 -> 8
        #9 -> 8, 6
        #8 -> 7, 5, 9, 10
        #7 -> 4, 8
        #6 -> 9, 5, 3
        #5 -> 8, 4, 2, 6
        #4 -> 1, 5, 7
        #3 -> 2, 6
        #2 -> 1, 0, 3, 5
        #1 -> 2, 4
        #0 -> 2

        #Only the options for moving forward
        #10 -> 8
        #9 -> 6
        #8 -> 7, 5, 9
        #7 -> 4
        #6 -> 5, 3
        #5 -> 4, 2, 6
        #4 -> 1, 5
        #3 -> 2
        #2 -> 0
        #1 -> 2

        #Several lists of possible options for the next move
        eight = [7, 5, 9]
        six = [5, 3]
        five = [4, 2, 6]
        four = [1, 5]

        #Randomizing the right path

        #Initializing a list called self.right_path
        self.right_path = []

        #Appending the number 10 to the list called self.right_path
        self.right_path.append(10)

        #While loop that fills the list called self.right_path depending on the latest value added to the list
        while True:
            if self.right_path[len(self.right_path)-1] == 10:
                self.right_path.append(8)
            if self.right_path[len(self.right_path)-1] == 9:
                self.right_path.append(6)
            if self.right_path[len(self.right_path)-1] == 8:
                self.right_path.append(eight[randint(0,2)])
            if self.right_path[len(self.right_path)-1] == 7:
                self.right_path.append(4)
            if self.right_path[len(self.right_path)-1] == 6:
                self.right_path.append(six[randint(0,1)])
            if self.right_path[len(self.right_path)-1] == 5:
                self.right_path.append(five[randint(0,2)])
            if self.right_path[len(self.right_path)-1] == 4:
                self.right_path.append(four[randint(0,1)])
            if self.right_path[len(self.right_path)-1] == 3:
                self.right_path.append(2)
            if self.right_path[len(self.right_path)-1] == 2:
                self.right_path.append(0)
                break
            if self.right_path[len(self.right_path)-1] == 1:
                self.right_path.append(2)
        
        #Appending a number to the list called self.right_path so it works as intended
        self.right_path.append(0)

        #Randomizing the answers for the calculations
        self.chosen_answers = {}
        for number in self.right_path:
            self.chosen_answers[number] = randint(0,3)

        #testing how to make all numbers random
        #for number in range(11):
            #if number not in self.chosen_answers:
                #self.chosen_answers[number] = randint(0,3)

        #Randomizing the initializing of the values for the wrong cubes
        self.number0 = randint(0,3)
        self.number1 = randint(0,3)
        self.number2 = randint(0,3)
        self.number3 = randint(0,3)
        self.number4 = randint(0,3)
        self.number5 = randint(0,3)
        self.number6 = randint(0,3)
        self.number7 = randint(0,3)
        self.number8 = randint(0,3)
        self.number9 = randint(0,3)
        self.number10 = randint(0,3)

        #Randomizing the answers
        #Initializing a dictionary called self.chosen_calculations
        self.chosen_calculations = {}

        #For loop that iterates through a dictionary called self.chosen_answers
        for number in self.chosen_answers:

            #Useful information
            #number is a key from self.chosen_answers -> right cube numbers
            #self.chosen_answers[number] is a value from self.chosen_answers -> right calculation answers
            #self.chosen_answers[self.right_path[self.chosen_answers[number]]] -> right cube numbers?

            #Several print functions inteded for testing
            #print(number)
            #print(self.chosen_answers[number])
            #print(self.chosen_answers[self.right_path[self.chosen_answers[number]]])

            #Several if sentences that will be chosen depending on the iterating object from a dictionary called self.chosen_answers
            #The following number of the iterating object  will get the next objects calculation as its value
            if self.chosen_answers[self.right_path[self.right_path.index(number) + 1]] == 0:
                self.chosen_calculations[number] = self.calculations[0]
            if self.chosen_answers[self.right_path[self.right_path.index(number) + 1]] == 1:
                self.chosen_calculations[number] = self.calculations[randint(1,2)]
            if self.chosen_answers[self.right_path[self.right_path.index(number) + 1]] == 2:
                self.chosen_calculations[number] = self.calculations[randint(3,5)]
            if self.chosen_answers[self.right_path[self.right_path.index(number) + 1]] == 3:
                self.chosen_calculations[number] = self.calculations[randint(6,9)]

        #Here we specify how large game window we want
        self.height = 700
        self.width = 640

        #Here are boolians that show which way you're going
        self.right = False
        self.left = False
        self.down = False
        self.up = False

        #This locks movement to move one block at a time
        self.locked = False

        #These locks lock sounds from making more than one sound per move
        self.sound_lock1 = False
        self.sound_lock2 = False
        self.sound_lock3 = False
        self.sound_lock4 = False
        self.sound_lock5 = False
        self.sound_lock6 = False
        self.sound_lock7 = False
        self.sound_lock8 = False
        self.sound_lock9 = False
        self.sound_lock10 = False

        #This changes the scene or adds a text that shows that you have won the game
        self.done = False

        #Here are the players coordinates
        self.x = 313
        self.y = 563
 
        #Here we initiate the window
        self.display = pygame.display.set_mode((self.width, self.height))
 
        #Here we set the caption on top of the window
        pygame.display.set_caption("Don't Fall")
 
        #Accessing a function that loops over and over
        #Thus making the game flow
        self.loop()

    #Function that downloads pictures
    def download_pictures(self):

        #Downloading picture one by one while initializing variables that we can later access with the pictures as value
        self.ball_on_cube = pygame.image.load("ball on cube2.png")
        self.normal_cube = pygame.image.load("normal cube.png")
        self.normal_cube2 = pygame.image.load("normal cube2.png")
        self.normal_cube_down = pygame.image.load("normal cube down.png")
        self.normal_cube_down2 = pygame.image.load("normal cube down2b.png")
        self.normal0 = pygame.image.load("0b.png")
        self.normal1 = pygame.image.load("1b.png")
        self.normal2 = pygame.image.load("2b.png")
        self.normal3 = pygame.image.load("3b.png")
        self.calculation_board = pygame.image.load("calculation board2.png")
        self.background = pygame.image.load("background.png")
        self.background1 = pygame.image.load("blue stars.png")
        self.background2 = pygame.image.load("Cubes.png")
        self.background3 = pygame.image.load("Green warp.png")
        self.background4 = pygame.image.load("colors.png")
        self.background6 = pygame.image.load("22.png")
        self.background7 = pygame.image.load("grass3.png")

    #Function that prints text when a player has won the game
    def won_the_game(self):
        #Prints: "you won!"
        print("you won!")

    #Ideas
    #Make a picture of the calculations?
    #Or make display of the writing
    #Kinda like in another game

    #Function that in the future will help with the display of the games calculations 
    def showing_calculations(self):
        pass
        #print(self.calculations[randint(0,8)])
        #self.display.blit(self.normal_cube_down, (100, 75))

    #NB
    #Edit the code so function called right_cubes is more usefull

    #Function that helps in the selection of the right cubes
    def right_cubes(self):
        #Initializing a list called self.all_cubes containing the numbers 0-10
        self.all_cubes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        #Initializing a dictionary called self.all_cubes2
        self.all_cubes2 = {}

        #Initializing a list called self.cube_choices that has numbers inside it
        #These numbers are used to separate right numbers from the wrong ones
        self.cube_choices = [0, 2, 1, 4, 7, 8, 10]

        #Initializing a list called self.numbers_on_cubes
        self.numbers_on_cubes = []

        #Initializing a list called self.calculation_choices
        self.calculation_choices = []

        #Initializing a dictionary called self.cube_choices2
        self.cube_choices2 = {}

        #Initializing a list called self.numbers_on_cubes2
        self.numbers_on_cubes2 = []

        #Initializing a list called self.calculation_choices2
        self.calculation_choices2 = []

        #For loop that iterates through a list called self.all_cubes while initializing keys and values to a dictionary called self.all_cubes2
        for cube in self.all_cubes:
            #Initializing a key with the name of the iterate object from self.all_cubes 
            #and the value of a random number 0 to 3 initialized with a method called randint which was imported from a module called random
            self.all_cubes2[str(cube)] = randint(0,3)

        #tänki vois tehä randomisti

        #Initializing a list called self.numbers_on_cubes again with numbers from 0 to 3 inside it
        #self.numbers_on_cubes = [0, 0, 2, 1, 1, 3, 2, 1, 2, 1, 0]

        #For loop that iterates through a list called self.all_cubes2 while appending calculations randomly to a list called self.calculation_choices
        for cube in self.all_cubes2:
            #Several if sentences which will be chosen depending on the number of the iterate object from a list called self.all_cubes2
            if self.all_cubes2[cube] == 0:
                #Appending the first calculation to a list called self.calculation_choices
                self.calculation_choices.append(self.calculations[0])
            elif self.all_cubes2[cube] == 1:
                #Appending a calculation to a list called self.calculation_choices depending on which index number will be chosen randomly with a method called randint
                #In this case randint chooses randomly either 1 or 2 which will indicate the index number of a list called self.calculations
                #The chosen calculation will be then appended to a list called self.calculation_choices
                self.calculation_choices.append(self.calculations[randint(1,2)])
            elif self.all_cubes2[cube] == 2:
                self.calculation_choices.append(self.calculations[randint(3,5)])
            elif self.all_cubes2[cube] == 3:
                self.calculation_choices.append(self.calculations[randint(6,9)])

        #Here are ideas to the randomizing of the selection of the correct cubes
        #ja random
        #cube_choices.append(randint(0,2))
        #while True:
            #cube_choices.append()

    #Function that is responsible for making the squares work as intended
    def cubes(self):
        #selvennä tätä o.O

        #Initializing a attribute called fontt that gets pygame font as its value
        #The chosen font is Arial and the chosen size is 50
        fontt = pygame.font.SysFont("Arial", 50)

        #Draws a shape to the surface of the game
        #The shapes color is black -> (0, 0, 0)
        #The coordinations of the shape are as follows: x = 10 and y = 10
        #And the size of the shape is 220 X 80
        pygame.draw.rect(self.display, (0, 170, 50), (40, 89, 220, 80))
        self.display.blit(self.calculation_board, (40, 89))

        #Initializing a dictionary called self.cube_info
        self.cube_info = {}

        #Here we initialize the game's squares and make them work as intended
        #In a slightly lazy way the same code will be repeated several times
        #This will be fixed in the future but for now the idea is to just make the game work as intended
        #Since the code will be repeated just the first lines of code will be documented

        #First row

        #Initializing two attributes called self.firstrow_1_on_cube_x and self.firstrow_1_on_cube_y
        #These attributes are booleans and they return truth values based on the coordinates of the playable character and the game's squares
        #If the playable character on this instance is on the first square as in the top square these attributes return True
        self.firstrow_1_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.firstrow_1_on_cube_y = 150 >= self.y-self.ball_on_cube.get_height() and 150 <= self.y+self.ball_on_cube.get_height()

        #If sentence that will be chosen if both attributes self.firstrow_1_on_cube_x and self.firstrow_1_on_cube_y return True
        if self.firstrow_1_on_cube_x and self.firstrow_1_on_cube_y:
            #winning sound
            self.win.play()
            #If sentence that will be chosen if number 0 is in a list called self.cube_choices
            if 0 in self.cube_choices:
                #Initializing attribute called self.firstrow_1 that gets a picture of a pushed down square and it's coordinates as its value
                self.firstrow_1 = self.display.blit(self.normal_cube_down2, (300, 150))
            #If sentence that will be chosen if number 0 is not in a list called self.cube_choices
            else:
                #Initializing attributes sel.x and self.y again this time with the number values of 313 and 563
                self.x = 313
                self.y = 563
        #If sentence that will be chosen if both attributes self.firstrow_1_on_cube_x and self.firstrow_1_on_cube_y return False
        else:
            #Top

            #Initializing attribute called self.firstrow_1 that gets a picture of a square that is not pushed down and it's coordinates as its value
            if 0 in self.right_path:

                #Several if sentences that will be chosen depending on the number that is will be on the cube
                if self.chosen_answers[0] == 0:
                    self.firstrow_1 = self.display.blit(self.normal0, (300, 150))
                elif self.chosen_answers[0] == 1:
                    self.firstrow_1 = self.display.blit(self.normal1, (300, 150))
                elif self.chosen_answers[0] == 2:
                    self.firstrow_1 = self.display.blit(self.normal2, (300, 150))
                elif self.chosen_answers[0] == 3:
                    self.firstrow_1 = self.display.blit(self.normal3, (300, 150))
            else:
                if self.number0 == 0:
                    self.firstrow_1 = self.display.blit(self.normal0, (300, 150))
                elif self.number0 == 1:
                    self.firstrow_1 = self.display.blit(self.normal1, (300, 150))
                elif self.number0 == 2:
                    self.firstrow_1 = self.display.blit(self.normal2, (300, 150))
                elif self.number0 == 3:
                    self.firstrow_1 = self.display.blit(self.normal3, (300, 150))
        #Adding the firsth row to a dictionary called self.cube_info
        self.cube_info["firstrow_1"] = (self.firstrow_1.y, self.firstrow_1.x)

        #Second row
        self.secondrow_1_on_cube_x = 200 >= self.x-self.ball_on_cube.get_width() and 200 <= self.x+self.ball_on_cube.get_width()
        self.secondrow_1_on_cube_y = 250 >= self.y-self.ball_on_cube.get_height() and 250 <= self.y+self.ball_on_cube.get_height()

        if self.secondrow_1_on_cube_x and self.secondrow_1_on_cube_y:
            if 1 in self.right_path:
                if self.sound_lock1 == False:
                    self.creak.play()
                    self.sound_lock1 = True
                text = fontt.render(f"{self.chosen_calculations[1]}", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.secondrow_1 = self.display.blit(self.normal_cube_down2, (200, 250))
            else:
                if self.sound_lock1 == False:
                    self.fall.play()
                    self.sound_lock1 = True
                self.x = 313
                self.y = 563
        else:
            self.sound_lock1 = False
            #Fourth lowest
            if 1 in self.right_path:
                if self.chosen_answers[1] == 0:
                    self.secondrow_1 = self.display.blit(self.normal0, (200, 250))
                elif self.chosen_answers[1] == 1:
                    self.secondrow_1 = self.display.blit(self.normal1, (200, 250))
                elif self.chosen_answers[1] == 2:
                    self.secondrow_1 = self.display.blit(self.normal2, (200, 250))
                elif self.chosen_answers[1] == 3:
                    self.secondrow_1 = self.display.blit(self.normal3, (200, 250))
            else:
                if self.number1 == 0:
                    self.secondrow_1 = self.display.blit(self.normal0, (200, 250))
                elif self.number1 == 1:
                    self.secondrow_1 = self.display.blit(self.normal1, (200, 250))
                elif self.number1 == 2:
                    self.secondrow_1 = self.display.blit(self.normal2, (200, 250))
                elif self.number1 == 3:
                    self.secondrow_1 = self.display.blit(self.normal3, (200, 250))

        self.secondrow_2_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.secondrow_2_on_cube_y = 250 >= self.y-self.ball_on_cube.get_height() and 250 <= self.y+self.ball_on_cube.get_height()

        if self.secondrow_2_on_cube_x and self.secondrow_2_on_cube_y:
            if 2 in self.right_path:
                if self.sound_lock2 == False:
                    self.creak.play()
                    self.sound_lock2 = True
                text = fontt.render(f"{self.chosen_calculations[2]}", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.secondrow_2 = self.display.blit(self.normal_cube_down2, (300, 250))
            else:
                if self.sound_lock2 == False:
                    self.fall.play()
                    self.sound_lock = True
                self.x = 313
                self.y = 563
        else:
            self.sound_lock2 = False
            if 2 in self.right_path:
                if self.chosen_answers[2] == 0:
                    self.secondrow_2 = self.display.blit(self.normal0, (300, 250))
                elif self.chosen_answers[2] == 1:
                    self.secondrow_2 = self.display.blit(self.normal1, (300, 250))
                elif self.chosen_answers[2] == 2:
                    self.secondrow_2 = self.display.blit(self.normal2, (300, 250))
                elif self.chosen_answers[2] == 3:
                    self.secondrow_2 = self.display.blit(self.normal3, (300, 250))
            else:
                if self.number2 == 0:
                    self.secondrow_2 = self.display.blit(self.normal0, (300, 250))
                elif self.number2 == 1:
                    self.secondrow_2 = self.display.blit(self.normal1, (300, 250))
                elif self.number2 == 2:
                    self.secondrow_2 = self.display.blit(self.normal2, (300, 250))
                elif self.number2 == 3:
                    self.secondrow_2 = self.display.blit(self.normal3, (300, 250))

        self.secondrow_3_on_cube_x = 400 >= self.x-self.ball_on_cube.get_width() and 400 <= self.x+self.ball_on_cube.get_width()
        self.secondrow_3_on_cube_y = 250 >= self.y-self.ball_on_cube.get_height() and 250 <= self.y+self.ball_on_cube.get_height()

        if self.secondrow_3_on_cube_x and self.secondrow_3_on_cube_y:
            if 3 in self.right_path:
                if self.sound_lock3 == False:
                    self.creak.play()
                    self.sound_lock3 = True
                text = fontt.render(f"{self.chosen_calculations[3]}", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.secondrow_3 = self.display.blit(self.normal_cube_down2, (400, 250))
            else:
                if self.sound_lock3 == False:
                    self.fall.play()
                    self.sound_lock3 = True
                self.x = 313
                self.y = 563
        else:
            self.sound_lock3 = False
            if 3 in self.right_path:
                if self.chosen_answers[3] == 0:
                    self.secondrow_3 = self.display.blit(self.normal0, (400, 250))
                elif self.chosen_answers[3] == 1:
                    self.secondrow_3 = self.display.blit(self.normal1, (400, 250))
                elif self.chosen_answers[3] == 2:
                    self.secondrow_3 = self.display.blit(self.normal2, (400, 250))
                elif self.chosen_answers[3] == 3:
                    self.secondrow_3 = self.display.blit(self.normal3, (400, 250))
            else:
                if self.number3 == 0:
                    self.secondrow_3 = self.display.blit(self.normal0, (400, 250))
                elif self.number3 == 1:
                    self.secondrow_3 = self.display.blit(self.normal1, (400, 250))
                elif self.number3 == 2:
                    self.secondrow_3 = self.display.blit(self.normal2, (400, 250))
                elif self.number3 == 3:
                    self.secondrow_3 = self.display.blit(self.normal3, (400, 250))
        #Adding the second row to a dictionary called self.cube_info
        self.cube_info["secondrow_1"] = (self.secondrow_1.y, self.secondrow_1.x)
        self.cube_info["secondrow_2"] = (self.secondrow_2.y, self.secondrow_2.x)
        self.cube_info["secondrow_3"] = (self.secondrow_3.y, self.secondrow_3.x)

        #Third row
        self.thirdrow_1_on_cube_x = 200 >= self.x-self.ball_on_cube.get_width() and 200 <= self.x+self.ball_on_cube.get_width()
        self.thirdrow_1_on_cube_y = 350 >= self.y-self.ball_on_cube.get_height() and 350 <= self.y+self.ball_on_cube.get_height()

        if self.thirdrow_1_on_cube_x and self.thirdrow_1_on_cube_y:
            if 4 in self.right_path:
                if self.sound_lock4 == False:
                    self.creak.play()
                    self.sound_lock4 = True
                text = fontt.render(f"{self.chosen_calculations[4]}", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.thirdrow_1 = self.display.blit(self.normal_cube_down2, (200, 350))
            else:
                if self.sound_lock4 == False:
                    self.fall.play()
                    self.sound_lock4 = True
                self.x = 313
                self.y = 563
        else:
            #Third lowest
            self.sound_lock4 = False
            if 4 in self.right_path:
                if self.chosen_answers[4] == 0:
                    self.thirdrow_1 = self.display.blit(self.normal0, (200, 350))
                elif self.chosen_answers[4] == 1:
                    self.thirdrow_1 = self.display.blit(self.normal1, (200, 350))
                elif self.chosen_answers[4] == 2:
                    self.thirdrow_1 = self.display.blit(self.normal2, (200, 350))
                elif self.chosen_answers[4] == 3:
                    self.thirdrow_1 = self.display.blit(self.normal3, (200, 350))
            else:
                if self.number4 == 0:
                    self.thirdrow_1 = self.display.blit(self.normal0, (200, 350))
                elif self.number4 == 1:
                    self.thirdrow_1 = self.display.blit(self.normal1, (200, 350))
                elif self.number4 == 2:
                    self.thirdrow_1 = self.display.blit(self.normal2, (200, 350))
                elif self.number4 == 3:
                    self.thirdrow_1 = self.display.blit(self.normal3, (200, 350))

        self.thirdrow_2_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.thirdrow_2_on_cube_y = 350 >= self.y-self.ball_on_cube.get_height() and 350 <= self.y+self.ball_on_cube.get_height()

        if self.thirdrow_2_on_cube_x and self.thirdrow_2_on_cube_y:
            if 5 in self.right_path:
                if self.sound_lock5 == False:
                    self.creak.play()
                    self.sound_lock5 = True
                text = fontt.render(f"{self.chosen_calculations[5]}", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.thirdrow_2 = self.display.blit(self.normal_cube_down2, (300, 350))
            else:
                if self.sound_lock5 == False:
                    self.fall.play()
                    self.sound_lock5 = True
                self.x = 313
                self.y = 563
        else:
            self.sound_lock5 = False
            if 5 in self.right_path:
                if self.chosen_answers[5] == 0:
                    self.thirdrow_2 = self.display.blit(self.normal0, (300, 350))
                elif self.chosen_answers[5] == 1:
                    self.thirdrow_2 = self.display.blit(self.normal1, (300, 350))
                elif self.chosen_answers[5] == 2:
                    self.thirdrow_2 = self.display.blit(self.normal2, (300, 350))
                elif self.chosen_answers[5] == 3:
                    self.thirdrow_2 = self.display.blit(self.normal3, (300, 350))
            else:
                if self.number5 == 0:
                    self.thirdrow_2 = self.display.blit(self.normal0, (300, 350))
                elif self.number5 == 1:
                    self.thirdrow_2 = self.display.blit(self.normal1, (300, 350))
                elif self.number5 == 2:
                    self.thirdrow_2 = self.display.blit(self.normal2, (300, 350))
                elif self.number5 == 3:
                    self.thirdrow_2 = self.display.blit(self.normal3, (300, 350))

        self.thirdrow_3_on_cube_x = 400 >= self.x-self.ball_on_cube.get_width() and 400 <= self.x+self.ball_on_cube.get_width()
        self.thirdrow_3_on_cube_y = 350 >= self.y-self.ball_on_cube.get_height() and 350 <= self.y+self.ball_on_cube.get_height()

        if self.thirdrow_3_on_cube_x and self.thirdrow_3_on_cube_y:
            if 6 in self.right_path:
                if self.sound_lock6 == False:
                    self.creak.play()
                    self.sound_lock6 = True
                text = fontt.render(f"{self.chosen_calculations[6]}", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.thirdrow_3 = self.display.blit(self.normal_cube_down2, (400, 350))
            else:
                if self.sound_lock6 == False:
                    self.fall.play()
                    self.sound_lock6 = True
                self.x = 313
                self.y = 563
        else:
            self.sound_lock6 = False
            if 6 in self.right_path:
                if self.chosen_answers[6] == 0:
                    self.thirdrow_3 = self.display.blit(self.normal0, (400, 350))
                elif self.chosen_answers[6] == 1:
                    self.thirdrow_3 = self.display.blit(self.normal1, (400, 350))
                elif self.chosen_answers[6] == 2:
                    self.thirdrow_3 = self.display.blit(self.normal2, (400, 350))
                elif self.chosen_answers[6] == 3:
                    self.thirdrow_3 = self.display.blit(self.normal3, (400, 350))
            else:
                if self.number6 == 0:
                    self.thirdrow_3 = self.display.blit(self.normal0, (400, 350))
                elif self.number6 == 1:
                    self.thirdrow_3 = self.display.blit(self.normal1, (400, 350))
                elif self.number6 == 2:
                    self.thirdrow_3 = self.display.blit(self.normal2, (400, 350))
                elif self.number6 == 3:
                    self.thirdrow_3 = self.display.blit(self.normal3, (400, 350))

        #Adding the third row to a dictionary called self.cube_info
        self.cube_info["thirdrow_1"] = (self.thirdrow_1.y, self.thirdrow_1.x)
        self.cube_info["thirdrow_2"] = (self.thirdrow_2.y, self.thirdrow_2.x)
        self.cube_info["thirdrow_3"] = (self.thirdrow_3.y, self.thirdrow_3.x)

        #Fourth row
        self.fourthrow_1_on_cube_x = 200 >= self.x-self.ball_on_cube.get_width() and 200 <= self.x+self.ball_on_cube.get_width()
        self.fourthrow_1_on_cube_y = 450 >= self.y-self.ball_on_cube.get_height() and 450 <= self.y+self.ball_on_cube.get_height()

        if self.fourthrow_1_on_cube_x and self.fourthrow_1_on_cube_y:
            if 7 in self.right_path:
                if self.sound_lock7 == False:
                    self.creak.play()
                    self.sound_lock7 = True
                text = fontt.render(f"{self.chosen_calculations[7]}", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.fourthrow_1 = self.display.blit(self.normal_cube_down2, (200, 450))
            else:
                if self.sound_lock7 == False:
                    self.fall.play()
                    self.sound_lock7 = True
                self.x = 313
                self.y = 563
        else:
            #Second lowest
            self.sound_lock7 = False
            if 7 in self.right_path:
                if self.chosen_answers[7] == 0:
                    self.fourthrow_1 = self.display.blit(self.normal0, (200, 450))
                elif self.chosen_answers[7] == 1:
                    self.fourthrow_1 = self.display.blit(self.normal1, (200, 450))
                elif self.chosen_answers[7] == 2:
                    self.fourthrow_1 = self.display.blit(self.normal2, (200, 450))
                elif self.chosen_answers[7] == 3:
                    self.fourthrow_1 = self.display.blit(self.normal3, (200, 450))
            else:
                if self.number7 == 0:
                    self.fourthrow_1 = self.display.blit(self.normal0, (200, 450))
                elif self.number7 == 1:
                    self.fourthrow_1 = self.display.blit(self.normal1, (200, 450))
                elif self.number7 == 2:
                    self.fourthrow_1 = self.display.blit(self.normal2, (200, 450))
                elif self.number7 == 3:
                    self.fourthrow_1 = self.display.blit(self.normal3, (200, 450))

        self.fourthrow_2_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.fourthrow_2_on_cube_y = 450 >= self.y-self.ball_on_cube.get_height() and 450 <= self.y+self.ball_on_cube.get_height()

        if self.fourthrow_2_on_cube_x and self.fourthrow_2_on_cube_y:
            if 8 in self.right_path:
                if self.sound_lock8 == False:
                    self.creak.play()
                    self.sound_lock8 = True
                text = fontt.render(f"{self.chosen_calculations[8]}", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.fourthrow_2 = self.display.blit(self.normal_cube_down2, (300, 450))
            else:
                if self.sound_lock8 == False:
                    self.fall.play()
                    self.sound_lock8 = True
                self.x = 313
                self.y = 563

        else:
            self.sound_lock8 = False
            if 8 in self.right_path:
                if self.chosen_answers[8] == 0:
                    self.fourthrow_2 = self.display.blit(self.normal0, (300, 450))
                elif self.chosen_answers[8] == 1:
                    self.fourthrow_2 = self.display.blit(self.normal1, (300, 450))
                elif self.chosen_answers[8] == 2:
                    self.fourthrow_2 = self.display.blit(self.normal2, (300, 450))
                elif self.chosen_answers[8] == 3:
                    self.fourthrow_2 = self.display.blit(self.normal3, (300, 450))
            else:
                if self.number8 == 0:
                    self.fourthrow_2 = self.display.blit(self.normal0, (300, 450))
                elif self.number8 == 1:
                    self.fourthrow_2 = self.display.blit(self.normal1, (300, 450))
                elif self.number8 == 2:
                    self.fourthrow_2 = self.display.blit(self.normal2, (300, 450))
                elif self.number8 == 3:
                    self.fourthrow_2 = self.display.blit(self.normal3, (300, 450))
        self.fourthrow_3_on_cube_x = 400 >= self.x-self.ball_on_cube.get_width() and 400 <= self.x+self.ball_on_cube.get_width()
        self.fourthrow_3_on_cube_y = 450 >= self.y-self.ball_on_cube.get_height() and 450 <= self.y+self.ball_on_cube.get_height()

        if self.fourthrow_3_on_cube_x and self.fourthrow_3_on_cube_y:
            
            if 9 in self.right_path:
                text = fontt.render(f"{self.chosen_calculations[9]}", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.fourthrow_3 = self.display.blit(self.normal_cube_down2, (400, 450))
                if self.sound_lock9 == False:
                    self.creak.play()
                    self.sound_lock9 = True
            else:
                if self.sound_lock9 == False:
                    self.fall.play()
                    self.sound_lock9 = True
                self.x = 313
                self.y = 563
        else:
            self.sound_lock9 = False
            if 9 in self.right_path:
                if self.chosen_answers[9] == 0:
                    self.fourthrow_3 = self.display.blit(self.normal0, (400, 450))
                elif self.chosen_answers[9] == 1:
                    self.fourthrow_3 = self.display.blit(self.normal1, (400, 450))
                elif self.chosen_answers[9] == 2:
                    self.fourthrow_3 = self.display.blit(self.normal2, (400, 450))
                elif self.chosen_answers[9] == 3:
                    self.fourthrow_3 = self.display.blit(self.normal3, (400, 450))
            else:
                if self.number9 == 0:
                    self.fourthrow_3 = self.display.blit(self.normal0, (400, 450))
                elif self.number9 == 1:
                    self.fourthrow_3 = self.display.blit(self.normal1, (400, 450))
                elif self.number9 == 2:
                    self.fourthrow_3 = self.display.blit(self.normal2, (400, 450))
                elif self.number9 == 3:
                    self.fourthrow_3 = self.display.blit(self.normal3, (400, 450))
        #Adding the fourth row to a dictionary called self.cube_info
        self.cube_info["fourthrow_1"] = (self.fourthrow_1.y, self.fourthrow_1.x)
        self.cube_info["fourthrow_2"] = (self.fourthrow_2.y, self.fourthrow_2.x)
        self.cube_info["fourthrow_3"] = (self.fourthrow_3.y, self.fourthrow_3.x)

        #Fifth row
        self.fifthrow_1_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.fifthrow_1_on_cube_y = 550 >= self.y-self.ball_on_cube.get_height() and 550 <= self.y+self.ball_on_cube.get_height()

        # ok make necessary adjustments in the init funktion
        # random doesnt work here
        if self.fifthrow_1_on_cube_x and self.fifthrow_1_on_cube_y:

            #delete unnecessary
            #print(self.chosen_answers[self.right_path[self.chosen_answers[10]]])
            #text2 = fontt.render(f"{self.chosen_calculations[10]}", True, (100, 40, 0))
            if self.sound_lock10 == False:
                    self.creak.play()
                    self.sound_lock10 = True

            text = fontt.render(f"{self.chosen_calculations[10]}", True, (255, 255, 255))
            self.display.blit(text, (50, 100))

            self.fifthrow_1 = self.display.blit(self.normal_cube_down2, (300, 550))
        else:
            #Lowest
            self.sound_lock10 = False
            if self.chosen_answers[10] == 0:
                self.fifthrow_1 = self.display.blit(self.normal0, (300, 550))
            elif self.chosen_answers[10] == 1:
                self.fifthrow_1 = self.display.blit(self.normal1, (300, 550))
            elif self.chosen_answers[10] == 2:
                self.fifthrow_1 = self.display.blit(self.normal2, (300, 550))
            elif self.chosen_answers[10] == 3:
                self.fifthrow_1 = self.display.blit(self.normal3, (300, 550))

        #Adding the fifth row to a dictionary called self.cube_info
        self.cube_info["fifthrow_1"] = (self.fifthrow_1.y, self.fifthrow_1.x)

    #Function that in the future will help with the movement of the character
    #def character(self):

    #Function that loops over and over
    #Thus making the game flow
    def loop(self):
        #Initializing attribute called clock with a new clock object that can be used to track an amount of time as it's value
        clock = pygame.time.Clock()

        #While loop that continues to iterate until the game has been won
        while True:
            #Accessing a function that basically draws the game
            self.draw_the_game()

            #Accessing a function that is mostly responsible for the way the character is moving
            self.analyse_events()

            #Used to help limit the runtime speed of a game
            #The program will never run at more than 60 frames per second
            clock.tick(60)

            #If sentence that will be chosen if the boolean attribute called self.done is True
            if self.done:

                #Accessing a function that prints text when a player has won the game
                self.won_the_game()

                #Ends the loop thus ending the game
                break

    #Function that is mostly responsible for the way the character is moving
    def analyse_events(self):
        #Accessing a funktion that in the future will help with the movement of the character
        #self.character()

        #For loop that iterates over event queue
        for event in pygame.event.get():
            #If sentence that will be chosen if a keyboard key is pressed down
            if event.type == pygame.KEYDOWN:
                #Several if sentences that will be chosen depending on the pressed key
                #Options are left, right, up, and down arrow keys
                #Attributes inside the if sentences are booleans that turn True when the if sentence is chosen
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_DOWN:
                    self.down = True
 
            #If sentence that will be chosen if a computer key is lifted
            if event.type == pygame.KEYUP:
                #Several if sentences that will be chosen depending on the lifted key
                #Options are left, right, up, and down arrow keys
                #Attributes inside the if sentences are booleans that turn False when the if sentence is chosen
                if event.key == pygame.K_LEFT:
                    self.left = False
                    self.locked = False
                if event.key == pygame.K_RIGHT:
                    self.right = False
                    self.locked = False
                if event.key == pygame.K_UP:
                    self.up = False
                    self.locked = False
                if event.key == pygame.K_DOWN:
                    self.down = False
                    self.locked = False
            #If sentence that is chosen if the game is quit either by clicking the windows X button or by completing the game
            if event.type == pygame.QUIT:
                #Ends the game
                exit()

        #Here we make game's playable character move as intended
        #Once again in a slightly lazy way the same code will be repeated several times
        #This too will be fixed in the future but for now the idea is to just make the game work as intended
        #Since the code will be repeated just the first lines of code will be documented

        #If sentence that will be chosen if attribute called self.locked returns False
        if self.locked == False:
            #Ok works but looks horrid
            #Here is just simply too much code and too much repetition

            #If sentence that will be chosen if self.y is over 463
            if self.y > 463:
                #If sentence that will be chosen if self.y is over 250
                if self.y > 250:
                    #If sentence that will be chosen if attribute called self.up return True
                    if self.up:
                        #self.y will be subtracked by 100 causing the playable character to move upwards
                        self.y -= 100
                        #Causes the player's movement to be locked thus making the player only move 1 block with one key press
                        self.locked = True
            #Here are still some problems
            elif self.y == 263:
                if self.x < 313:
                    if self.right:
                        self.x += 100
                        self.locked = True
                if self.x > 350:
                    if self.left:
                        self.x -= 100
                        self.locked = True
                #Edit this part
                if self.x == 213:
                    if self.y < 563:
                        if self.down:
                            self.y += 100
                            self.locked = True
                    if self.y > 350:
                        if self.up:
                            self.y -= 100
                            self.locked = True
                elif self.x == 413:
                    if self.y < 563:
                        if self.down:
                            self.y += 100
                            self.locked = True
                    if self.y > 350:
                        if self.up:
                            self.y -= 100
                            self.locked = True
                #Why does this throw from side to side?
                elif self.x == 313:
                    #if self.x < 413:
                        #if self.right:
                            #self.x += 100
                            #self.locked = True
                    #if self.x > 213:
                        #if self.left:
                            #self.x -= 100
                            #self.locked = True
                    if self.y < 563:
                        if self.down:
                            self.y += 100
                            self.locked = True
                    if self.y > 250:
                        if self.up:
                            self.y -= 100
                            self.locked = True
            elif self.y == 463:
                if self.x < 413:
                    if self.right:
                        self.x += 100
                        self.locked = True
                if self.x > 213:
                    if self.left:
                        self.x -= 100
                        self.locked = True
                if self.x == 213:
                    if self.y < 463:
                        if self.down:
                            self.y += 100
                            self.locked = True
                    if self.y > 250:
                        if self.up:
                            self.y -= 100
                            self.locked = True
                elif self.x == 413:
                    if self.y < 463:
                        if self.down:
                            self.y += 100
                            self.locked = True
                    if self.y > 250:
                        if self.up:
                            self.y -= 100
                            self.locked = True
                else:
                    if self.y < 563:
                        if self.down:
                            self.y += 100
                            self.locked = True
                    if self.y > 250:
                        if self.up:
                            self.y -= 100
                            self.locked = True
            elif self.y == 163:
                self.done = True
            else:
                if self.x < 413:
                    if self.right:
                        self.x += 100
                        self.locked = True
                if self.x > 213:
                    if self.left:
                        self.x -= 100
                        self.locked = True
                if self.y < 563:
                    if self.down:
                        self.y += 100
                        self.locked = True
                if self.y > 250:
                    if self.up:
                        self.y -= 100
                        self.locked = True

    #Function that basically draws the game
    def draw_the_game(self):
 
        #Filling the display with the wanted color
        self.display.fill((0,100,100))

        #Filling the display with a picture of stars
        self.display.blit(self.background7, (0, 0))

        #Accessing function that is responsible for making the squares work as intended
        self.cubes()

        #Accessing a function that in the future will help with the display of the games calculations 
        self.showing_calculations()

        #Accessing a function that helps in the selection of the right cubes
        self.right_cubes()

        #Draws a picture to the surface of the game
        #The coordinations of the shape are whatever self.x and self.y happen to be
        self.display.blit(self.ball_on_cube, (self.x, self.y))
 
        #Allows only a portion of the screen to updated, instead of the entire area
        #If no argument is passed it updates the entire surface area
        pygame.display.flip()

#Used to execute code if the file is run directly
if __name__ == "__main__":
    #Calling a class called DontFall
    DontFall()