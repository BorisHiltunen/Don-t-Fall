import pygame
from random import randint

class DontFall:
    #Initializing necessary attributes
    def __init__(self):
        pygame.init()

        #This downloads pictures
        self.download_pictures()

        #here are calculations in the correct order
        self.calculations = ["0 + 0", "0 + 1", "1 + 0", "0 + 2", "2 + 0", "1 + 1", "0 + 3", "1 + 2", "2 + 1", "3 + 0"]

        #Here we specify how large game window we want
        self.height = 700
        self.width = 640

        #Here are boolians that show which way you're going
        self.right = False
        self.left = False
        self.down = False
        self.up = False

        #This locks movement to just move one block at a time
        self.locked = False

        #This changes the scene or adds a text that shows that you have won the game
        self.done = False

        #Here are the players coordinates
        self.x = 313
        self.y = 563
 
        #Here we initiate the window
        self.display = pygame.display.set_mode((self.width, self.height))
 
        #Here we set the caption
        pygame.display.set_caption("Don't Fall")
 
        #This is a function that loops over and over
        #Thus making the game flow
        self.loop()

    def download_pictures(self):
        self.ball_on_cube = pygame.image.load("ball on cube.png")
        self.normal_cube = pygame.image.load("normal cube.png")
        self.normal_cube2 = pygame.image.load("normal cube2.png")
        self.normal_cube_down = pygame.image.load("normal cube down.png")
        self.normal_cube_down2 = pygame.image.load("normal cube down2.png")
        self.normal0 = pygame.image.load("0.png")
        self.normal1 = pygame.image.load("11.png")
        self.normal2 = pygame.image.load("2.png")
        self.normal3 = pygame.image.load("3.png")

    def won_the_game(self):
        print("you won!")

    #tee kuva laskuista?
    #tai sit tee display kirjoitusta
    #vähänniinku rahasateessa
    # ja vaihtuu vasta, kun on ratkaistu
    def showing_calculations(self):
        pass
        #print(self.calculations[randint(0,8)])
        #self.display.blit(self.normal_cube_down, (100, 75))

    def right_cubes(self):
        self.all_cubes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.all_cubes2 = {}

        self.cube_choices = []
        self.numbers_on_cubes = []
        self.calculation_choices = []

        self.cube_choices2 = {}
        self.numbers_on_cubes2 = []
        self.calculation_choices2 = []

        for cube in self.all_cubes:
            self.all_cubes2[str(cube)] = randint(0,3)

        #self.calculations = ["0 + 0", "0 + 1", "1 + 0", "0 + 2", "2 + 0", "1 + 1", "0 + 3", "1 + 2", "2 + 1", "3 + 0"]

        self.cube_choices = [0, 2, 1, 4, 7, 8, 10]
        #tänki vois tehä randomisti
        #self.numbers_on_cubes = [0, 0, 2, 1, 1, 3, 2, 1, 2, 1, 0]
        for cube in self.all_cubes2:
            if self.all_cubes2[cube] == 0:
                self.calculation_choices.append(self.calculations[0])
            elif self.all_cubes2[cube] == 1:
                self.calculation_choices.append(self.calculations[randint(1,2)])
            elif self.all_cubes2[cube] == 2:
                self.calculation_choices.append(self.calculations[randint(3,5)])
            elif self.all_cubes2[cube] == 3:
                self.calculation_choices.append(self.calculations[randint(6,9)])

        #ja random
        #cube_choices.append(randint(0,2))
        #while True:
            #cube_choices.append()

    def cubes(self):
        #selvennä tätä o.O

        fontt = pygame.font.SysFont("Arial", 50)
        pygame.draw.rect(self.display, (0, 0, 0), (10, 10, 280, 230))

        self.cube_info = {}

        #ensimmäinen rivi
        self.firstrow_1_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.firstrow_1_on_cube_y = 150 >= self.y-self.ball_on_cube.get_height() and 150 <= self.y+self.ball_on_cube.get_height()

        if self.firstrow_1_on_cube_x and self.firstrow_1_on_cube_y:
            #laita tää jokaseen
            #muuta tätä miten tää kattoo
            #kokeile miten joku joka ei oo listassa tekee
            if 0 in self.cube_choices:
                self.firstrow_1 = self.display.blit(self.normal_cube_down2, (300, 150))
            else:
                self.x = 313
                self.y = 563
        else:
            #ylin
            self.firstrow_1 = self.display.blit(self.normal0, (300, 150))
        #sanakirjaan ensimmäisen ruutu rivin lisäys
        self.cube_info["firstrow_1"] = (self.firstrow_1.y, self.firstrow_1.x)

        #toinen rivi
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
            #4alin
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
        #sanakirjaan toisen ruutu rivin lisäys
        self.cube_info["secondrow_1"] = (self.secondrow_1.y, self.secondrow_1.x)
        self.cube_info["secondrow_2"] = (self.secondrow_2.y, self.secondrow_2.x)
        self.cube_info["secondrow_3"] = (self.secondrow_3.y, self.secondrow_3.x)

        #kolmas rivi
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
            #3alin
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
        #sanakirjaan kolmannen ruutu riven lisäys
        self.cube_info["thirdrow_1"] = (self.thirdrow_1.y, self.thirdrow_1.x)
        self.cube_info["thirdrow_2"] = (self.thirdrow_2.y, self.thirdrow_2.x)
        self.cube_info["thirdrow_3"] = (self.thirdrow_3.y, self.thirdrow_3.x)

        #neljäs rivi
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
            #2alin
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
        #sanakirjaan neljännen ruutu riven lisäys
        self.cube_info["fourthrow_1"] = (self.fourthrow_1.y, self.fourthrow_1.x)
        self.cube_info["fourthrow_2"] = (self.fourthrow_2.y, self.fourthrow_2.x)
        self.cube_info["fourthrow_3"] = (self.fourthrow_3.y, self.fourthrow_3.x)

        self.fifthrow_1_on_cube_x = 300 >= self.x-self.ball_on_cube.get_width() and 300 <= self.x+self.ball_on_cube.get_width()
        self.fifthrow_1_on_cube_y = 550 >= self.y-self.ball_on_cube.get_height() and 550 <= self.y+self.ball_on_cube.get_height()

        if self.fifthrow_1_on_cube_x and self.fifthrow_1_on_cube_y:
            #self.all_cubes[10]
            teksti = fontt.render(f"1 + 1 = ?", True, (255, 255, 255))
            self.display.blit(teksti, (50, 100))
            self.fifthrow_1 = self.display.blit(self.normal_cube_down2, (300, 550))
        else:
            #alin
            self.fifthrow_1 = self.display.blit(self.normal0, (300, 550))
        #sanakirjaan viidennen ruutu riven lisäys
        self.cube_info["fifthrow_1"] = (self.fifthrow_1.y, self.fifthrow_1.x)

    #def character(self):

    def loop(self):
        
        kello = pygame.time.Clock()
        while True:
            self.draw_the_game()
            self.analyse_events()
            kello.tick(60)
            if self.done:
                self.won_the_game()
                break
            #print(self.x)

    def analyse_events(self):
        #self.character()

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
 
            if event.type == pygame.KEYUP:
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
 
            if event.type == pygame.QUIT:
                exit()

        if self.locked == False:

            #ok toimii mut joo näyttää järkyttävältä
            # tässä on nyt ylipäätänsä turhan paljon koodia ja paljon toistoa
            if self.y > 463:
                if self.y > 250:
                    if self.up:
                        self.y -= 100
                        self.locked = True
            #tässä vielä ongelmaa
            elif self.y == 263:
                if self.x < 313:
                    if self.right:
                        self.x += 100
                        self.locked = True
                if self.x > 350:
                    if self.left:
                        self.x -= 100
                        self.locked = True
                #muokkaa tätä kohtaa
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
                #miks tää nyt heittää reunast reunaa
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
            #sitten kun on valmiimpi
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

    def draw_the_game(self):
 
        self.display.fill((0,100,100))

        self.cubes()

        #tääkin alussa
        self.showing_calculations()
        self.right_cubes()

        #testi
        self.display.blit(self.ball_on_cube, (self.x, self.y))
 
        pygame.display.flip()

if __name__ == "__main__":
    DontFall()