import pygame
from random import randint

class DontFall:
    def __init__(self):
        pygame.init()

        self.download_pictures()

        self.calculations = ["0 + 1", "0 + 2", "0 + 3", "1 + 0", "1 + 1", "1 + 2", "2 + 0", "2 + 1", "3 + 0"]

        self.height = 700
        self.width = 640

        self.right = False
        self.left = False
        self.down = False
        self.up = False
        self.locked = False

        #tää vaihtaa scenen tai lisää tekstin et on voittanut pelin
        self.done = False

        self.x = 313
        self.y = 563
 
        self.display = pygame.display.set_mode((self.width, self.height))
 
        pygame.display.set_caption("Don't Fall")
 
        self.loop()

    def download_pictures(self):
        self.ball_on_cube = pygame.image.load("ball on cube.png")
        self.normal_cube = pygame.image.load("normal cube.png")
        self.normal_cube2 = pygame.image.load("normal cube2.png")
        self.normal_cube_down = pygame.image.load("normal cube down.png")
        self.normal_cube_down2 = pygame.image.load("normal cube down2.png")

    def won_the_game(self):
        print("you won")

    #tee kuva laskuista?
    #tai sit tee display kirjoitusta
    #vähänniinku rahasateessa
    # ja vaihtuu vasta, kun on ratkaistu
    def showing_calculations(self):
        #print(self.calculations[randint(0,8)])
        self.display.blit(self.normal_cube_down, (100, 75))

    #selvitä miks tää laittaa ruutuja uusiin kohtiin
    #pitäis kans jättää ratkaistut ruudut alas
    def cubes(self):

        for cube in self.cube_info:
            #print(self.x)
            #print(self.y)
            on_cube_x =  self.cube_info[cube][0] >= self.x-self.ball_on_cube.get_width() and self.cube_info[cube][0] <= self.x+self.ball_on_cube.get_width()
            on_cube_y = self.cube_info[cube][1] >= self.y-self.ball_on_cube.get_height() and self.cube_info[cube][1] <= self.y+self.ball_on_cube.get_height()

            if on_cube_x and on_cube_y:
                self.display.blit(self.normal_cube_down2, (self.cube_info[cube][0], self.cube_info[cube][1]))
                #self.display.blit(self.normal_cube_down2, (0, 0))

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
                else:
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

        self.cube_info = {}
 
        self.display.fill((0,100,100))

        #ylin
        self.firstrow_1 = self.display.blit(self.normal_cube2, (300, 150))
        self.cube_info["firstrow_1"] = (self.firstrow_1.y, self.firstrow_1.x)

        #4alin
        self.secondrow_1 = self.display.blit(self.normal_cube2, (400, 250))
        self.secondrow_2 = self.display.blit(self.normal_cube2, (200, 250))
        self.secondrow_3 = self.display.blit(self.normal_cube2, (300, 250))
        self.cube_info["secondrow_1"] = (self.secondrow_1.y, self.secondrow_1.x)
        self.cube_info["secondrow_2"] = (self.secondrow_2.y, self.secondrow_2.x)
        self.cube_info["secondrow_3"] = (self.secondrow_3.y, self.secondrow_3.x)

        #3alin
        self.thirdrow_1 = self.display.blit(self.normal_cube2, (400, 350))
        self.thirdrow_2 = self.display.blit(self.normal_cube2, (200, 350))
        self.thirdrow_3 = self.display.blit(self.normal_cube2, (300, 350))
        self.cube_info["thirdrow_1"] = (self.thirdrow_1.y, self.thirdrow_1.x)
        self.cube_info["thirdrow_2"] = (self.thirdrow_2.y, self.thirdrow_2.x)
        self.cube_info["thirdrow_3"] = (self.thirdrow_3.y, self.thirdrow_3.x)
        #2alin
        self.fourthrow_1 = self.display.blit(self.normal_cube2, (400, 450))
        self.fourthrow_2 = self.display.blit(self.normal_cube2, (200, 450))
        self.fourthrow_3 = self.display.blit(self.normal_cube2, (300, 450))
        self.cube_info["fourthrow_1"] = (self.fourthrow_1.y, self.fourthrow_1.x)
        self.cube_info["fourthrow_2"] = (self.fourthrow_2.y, self.fourthrow_2.x)
        self.cube_info["fourthrow_3"] = (self.fourthrow_3.y, self.fourthrow_3.x)
        #alin
        self.fifthrow_1 = self.display.blit(self.normal_cube2, (300, 550))
        self.cube_info["fifthrow_1"] = (self.fifthrow_1.y, self.fifthrow_1.x)

        #vielä testaamassa
        self.cubes()

        #tääkin alussa
        self.showing_calculations()

        #testi
        self.display.blit(self.ball_on_cube, (self.x, self.y))
 
        pygame.display.flip()

if __name__ == "__main__":
    DontFall()