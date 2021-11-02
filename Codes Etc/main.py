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

        #Here are the needed calculations inside a list in ascending order
        self.calculations = ["0 + 0", "0 + 1", "1 + 0", "0 + 2", "2 + 0", "1 + 1", "0 + 3", "1 + 2", "2 + 1", "3 + 0"]

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
        self.ball_on_cube = pygame.image.load("ball on cube.png")
        self.normal_cube = pygame.image.load("normal cube.png")
        self.normal_cube2 = pygame.image.load("normal cube2.png")
        self.normal_cube_down = pygame.image.load("normal cube down.png")
        self.normal_cube_down2 = pygame.image.load("normal cube down2.png")
        self.normal0 = pygame.image.load("0.png")
        self.normal1 = pygame.image.load("11.png")
        self.normal2 = pygame.image.load("2.png")
        self.normal3 = pygame.image.load("3.png")

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
        #And the size of the shape is 280 X 230
        pygame.draw.rect(self.display, (0, 0, 0), (10, 10, 280, 230))

        #Initializing a dictionary called self.cube_info
        self.cube_info = {}

        #First row
        self.firstrow_1_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.firstrow_1_on_cube_y = 150 >= self.y-self.ball_on_cube.get_height() and 150 <= self.y+self.ball_on_cube.get_height()

        if self.firstrow_1_on_cube_x and self.firstrow_1_on_cube_y:
            if 0 in self.cube_choices:
                self.firstrow_1 = self.display.blit(self.normal_cube_down2, (300, 150))
            else:
                self.x = 313
                self.y = 563
        else:
            #Top
            self.firstrow_1 = self.display.blit(self.normal0, (300, 150))
        #Adding the firsth row to a dictionary called self.cube_info
        self.cube_info["firstrow_1"] = (self.firstrow_1.y, self.firstrow_1.x)

        #Second row
        self.secondrow_1_on_cube_x = 200 >= self.x-self.ball_on_cube.get_width() and 200 <= self.x+self.ball_on_cube.get_width()
        self.secondrow_1_on_cube_y = 250 >= self.y-self.ball_on_cube.get_height() and 250 <= self.y+self.ball_on_cube.get_height()

        if self.secondrow_1_on_cube_x and self.secondrow_1_on_cube_y:
            if 1 in self.cube_choices:
                text = fontt.render(f"1 + 1 = ?", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.secondrow_1 = self.display.blit(self.normal_cube_down2, (200, 250))
            else:
                self.x = 313
                self.y = 563
        else:
            #Fourth lowest
            self.secondrow_1 = self.display.blit(self.normal1, (200, 250))

        self.secondrow_2_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.secondrow_2_on_cube_y = 250 >= self.y-self.ball_on_cube.get_height() and 250 <= self.y+self.ball_on_cube.get_height()

        if self.secondrow_2_on_cube_x and self.secondrow_2_on_cube_y:
            if 2 in self.cube_choices:
                text = fontt.render(f"0 + 0 = ?", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.secondrow_2 = self.display.blit(self.normal_cube_down2, (300, 250))
            else:
                self.x = 313
                self.y = 563
        else:
            self.secondrow_2 = self.display.blit(self.normal2, (300, 250))

        self.secondrow_3_on_cube_x = 400 >= self.x-self.ball_on_cube.get_width() and 400 <= self.x+self.ball_on_cube.get_width()
        self.secondrow_3_on_cube_y = 250 >= self.y-self.ball_on_cube.get_height() and 250 <= self.y+self.ball_on_cube.get_height()

        if self.secondrow_3_on_cube_x and self.secondrow_3_on_cube_y:
            if 3 in self.cube_choices:
                text = fontt.render(f"1 + 1 = ?", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.secondrow_3 = self.display.blit(self.normal_cube_down2, (400, 250))
            else:
                self.x = 313
                self.y = 563
        else:
            self.secondrow_3 = self.display.blit(self.normal1, (400, 250))
        #Adding the second row to a dictionary called self.cube_info
        self.cube_info["secondrow_1"] = (self.secondrow_1.y, self.secondrow_1.x)
        self.cube_info["secondrow_2"] = (self.secondrow_2.y, self.secondrow_2.x)
        self.cube_info["secondrow_3"] = (self.secondrow_3.y, self.secondrow_3.x)

        #Third row
        self.thirdrow_1_on_cube_x = 200 >= self.x-self.ball_on_cube.get_width() and 200 <= self.x+self.ball_on_cube.get_width()
        self.thirdrow_1_on_cube_y = 350 >= self.y-self.ball_on_cube.get_height() and 350 <= self.y+self.ball_on_cube.get_height()

        if self.thirdrow_1_on_cube_x and self.thirdrow_1_on_cube_y:
            if 4 in self.cube_choices:
                text = fontt.render(f"1 + 0 = ?", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.thirdrow_1 = self.display.blit(self.normal_cube_down2, (200, 350))
            else:
                self.x = 313
                self.y = 563
        else:
            #Third lowest
            self.thirdrow_1 = self.display.blit(self.normal1, (200, 350))

        self.thirdrow_2_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.thirdrow_2_on_cube_y = 350 >= self.y-self.ball_on_cube.get_height() and 350 <= self.y+self.ball_on_cube.get_height()

        if self.thirdrow_2_on_cube_x and self.thirdrow_2_on_cube_y:
            if 5 in self.cube_choices:
                text = fontt.render(f"1 + 0 = ?", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.thirdrow_2 = self.display.blit(self.normal_cube_down2, (300, 350))
            else:
                self.x = 313
                self.y = 563
        else:
            self.thirdrow_2 = self.display.blit(self.normal3, (300, 350))

        self.thirdrow_3_on_cube_x = 400 >= self.x-self.ball_on_cube.get_width() and 400 <= self.x+self.ball_on_cube.get_width()
        self.thirdrow_3_on_cube_y = 350 >= self.y-self.ball_on_cube.get_height() and 350 <= self.y+self.ball_on_cube.get_height()

        if self.thirdrow_3_on_cube_x and self.thirdrow_3_on_cube_y:
            if 6 in self.cube_choices:
                text = fontt.render(f"2 + 1 = ?", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.thirdrow_3 = self.display.blit(self.normal_cube_down2, (400, 350))
            else:
                self.x = 313
                self.y = 563
        else:
            self.thirdrow_3 = self.display.blit(self.normal2, (400, 350))
        ##Adding the third row to a dictionary called self.cube_info
        self.cube_info["thirdrow_1"] = (self.thirdrow_1.y, self.thirdrow_1.x)
        self.cube_info["thirdrow_2"] = (self.thirdrow_2.y, self.thirdrow_2.x)
        self.cube_info["thirdrow_3"] = (self.thirdrow_3.y, self.thirdrow_3.x)

        #Fourth row
        self.fourthrow_1_on_cube_x = 200 >= self.x-self.ball_on_cube.get_width() and 200 <= self.x+self.ball_on_cube.get_width()
        self.fourthrow_1_on_cube_y = 450 >= self.y-self.ball_on_cube.get_height() and 450 <= self.y+self.ball_on_cube.get_height()

        if self.fourthrow_1_on_cube_x and self.fourthrow_1_on_cube_y:
            if 7 in self.cube_choices:
                text = fontt.render(f"1 + 0 = ?", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.fourthrow_1 = self.display.blit(self.normal_cube_down2, (200, 450))
            else:
                self.x = 313
                self.y = 563
        else:
            #Second lowest
            self.fourthrow_1 = self.display.blit(self.normal0, (200, 450))

        self.fourthrow_2_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.fourthrow_2_on_cube_y = 450 >= self.y-self.ball_on_cube.get_height() and 450 <= self.y+self.ball_on_cube.get_height()

        if self.fourthrow_2_on_cube_x and self.fourthrow_2_on_cube_y:
            if 8 in self.cube_choices:
                text = fontt.render(f"0 + 0 = ?", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.fourthrow_2 = self.display.blit(self.normal_cube_down2, (300, 450))
            else:
                self.x = 313
                self.y = 563
        else:
            self.fourthrow_2 = self.display.blit(self.normal2, (300, 450))

        self.fourthrow_3_on_cube_x = 400 >= self.x-self.ball_on_cube.get_width() and 400 <= self.x+self.ball_on_cube.get_width()
        self.fourthrow_3_on_cube_y = 450 >= self.y-self.ball_on_cube.get_height() and 450 <= self.y+self.ball_on_cube.get_height()

        if self.fourthrow_3_on_cube_x and self.fourthrow_3_on_cube_y:
            if 9 in self.cube_choices:
                text = fontt.render(f"1 + 1 = ?", True, (255, 255, 255))
                self.display.blit(text, (50, 100))
                self.fourthrow_3 = self.display.blit(self.normal_cube_down2, (400, 450))
            else:
                self.x = 313
                self.y = 563
        else:
            self.fourthrow_3 = self.display.blit(self.normal1, (400, 450))
        #Adding the fourth row to a dictionary called self.cube_info
        self.cube_info["fourthrow_1"] = (self.fourthrow_1.y, self.fourthrow_1.x)
        self.cube_info["fourthrow_2"] = (self.fourthrow_2.y, self.fourthrow_2.x)
        self.cube_info["fourthrow_3"] = (self.fourthrow_3.y, self.fourthrow_3.x)

        #Fifth row
        self.fifthrow_1_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.fifthrow_1_on_cube_y = 550 >= self.y-self.ball_on_cube.get_height() and 550 <= self.y+self.ball_on_cube.get_height()

        if self.fifthrow_1_on_cube_x and self.fifthrow_1_on_cube_y:
            teksti = fontt.render(f"1 + 1 = ?", True, (255, 255, 255))
            self.display.blit(teksti, (50, 100))
            self.fifthrow_1 = self.display.blit(self.normal_cube_down2, (300, 550))
        else:
            #Lowest
            self.fifthrow_1 = self.display.blit(self.normal0, (300, 550))
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

        if self.locked == False:
            #Ok works but looks horrid
            #Here is just simply too much code and too much repetition
            if self.y > 463:
                if self.y > 250:
                    if self.up:
                        self.y -= 100
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