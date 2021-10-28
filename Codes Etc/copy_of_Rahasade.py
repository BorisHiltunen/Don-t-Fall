import pygame
from random import randint
 
class Rahasade:
    def __init__(self):
        pygame.init()
        
        self.lataa_kuvat()
        
        self.korkeus = 480
        self.leveys = 640
 
        self.oikealle = False
        self.vasemmalle = False
 
        self.x = 0
        self.y = 480-self.robo.get_height()
 
        self.kolikkoja = 0
        self.aika = 0
        self.paras_aika = 0
        self.paras_kolikkomaara = 0
 
        self.maara = 4
        self.hirvioiden_maara = 0
 
        self.kolikot = []
        self.hirviot = []
 
        self.sekunti = 0
        self.sekunnit = 0
        self.minuutit = 0
        self.tunnit = 0
 
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))
 
        pygame.display.set_caption("Rahasade")
 
        self.silmukka()
 
    def lataa_kuvat(self):
        self.robo = pygame.image.load("ball on cube.png")
        self.kolikko = pygame.image.load("normal cube down.png")
        self.hirvio = pygame.image.load("normal cube down2.png")
 
    def kolikkojen_toiminta(self):
        for i in range(self.maara):
            # aiheuttaa että alkupaikka arvotaan heti
            self.kolikot.append([-1000,self.korkeus])
        for i in range(self.maara):
            osuma_x = self.kolikot[i][0] >= self.x-self.robo.get_width()/2 and self.kolikot[i][0] <= self.x+self.robo.get_width()
            osuma_y = self.kolikot[i][1] >= self.y-self.robo.get_height()/2 and self.kolikot[i][1] <= self.y+self.robo.get_height()
            if self.kolikot[i][1]+self.kolikko.get_height() < self.korkeus+200:
                # kolikko putoaa alaspäin
                self.kolikot[i][1] += 2
            if osuma_x and osuma_y:
                    self.kolikkoja += 1
                    self.kolikot[i][0] = randint(0,self.leveys-self.robo.get_width())
                    self.kolikot[i][1] = -randint(100,1000)
            else:
                if self.kolikot[i][0] < -self.robo.get_width() or self.kolikot[i][0] > self.leveys:
                    # arvotaan uusi alkupaikka
                    self.kolikot[i][0] = randint(0,self.leveys-self.robo.get_width())
                    self.kolikot[i][1] = -randint(100,600)
                else:
                    if self.kolikot[i][1]+self.kolikko.get_height()/2 >= self.korkeus+100:
                        self.kolikot[i][0] = randint(0,self.leveys-self.robo.get_width())
                        self.kolikot[i][1] = -randint(100,600)
 
    def hirvioiden_toiminta(self):
        for i in range(self.hirvioiden_maara):
            # aiheuttaa että alkupaikka arvotaan heti
            self.hirviot.append([-1000,self.korkeus])
        for i in range(self.hirvioiden_maara):
            hirvio_osuma_x = self.hirviot[i][0] >= self.x-self.robo.get_width()/2 and self.hirviot[i][0] <= self.x+self.robo.get_width()/2
            hirvio_osuma_y = self.hirviot[i][1] >= self.y-self.hirvio.get_height() and self.hirviot[i][1] <= self.y+self.robo.get_height()
            if self.hirviot[i][1]+self.hirvio.get_height() < self.korkeus+200:
                # hirvio putoaa alaspäin
                self.hirviot[i][1] += 2
            if hirvio_osuma_x and hirvio_osuma_y:
                for i in range(self.maara):
                    self.kolikot[i] =([-1000,self.korkeus])
                for i in range(self.hirvioiden_maara):
                    self.hirviot[i] =([-1000,self.korkeus])
                self.kolikkoja = 0
                self.x = 0
                self.y = 480-self.robo.get_height()
                self.sekunti = 0
                self.sekunnit = 0
                self.minuutit = 0
                self.tunnit = 0
            else:
                if self.hirviot[i][0] < -self.hirvio.get_width() or self.hirviot[i][0] > self.leveys:
                    # arvotaan uusi alkupaikka
                    self.hirviot[i][0] = randint(0,self.leveys-self.hirvio.get_width())
                    self.hirviot[i][1] = -randint(100,600)
                else:
                    if self.hirviot[i][1]+self.hirvio.get_height()/2 >= self.korkeus+100:
                        self.hirviot[i][0] = randint(0,self.leveys-self.hirvio.get_width())
                        self.hirviot[i][1] = -randint(100,1000)
 
    def ajan_toiminta(self):
        if self.sekunti == 60:
            self.sekunnit += 1
            self.sekunti = 0
            if self.sekunnit == 60:
                self.sekunnit = 0
                self.minuutit += 1
                if self.minuutit == 60:
                    self.minuutit = 0
                    self.tunnit += 1
                    if self.tunnit == 24:
                        self.tunnit = 0
 
    def ajan_laskenta(self, luku: int):
        aika = ""
        sekunnit = 0
        minuutit = 0
        tunnit = 0
 
        while luku > 0:
            luku -= 1
            sekunnit += 1
            if sekunnit == 60:
                sekunnit = 0
                minuutit += 1
                if minuutit == 60:
                    minuutit = 0
                    tunnit += 1
                    if tunnit == 24:
                        tunnit = 0
 
        if tunnit < 10:
            if minuutit < 10:
                if sekunnit < 10:
                    aika = f"0{tunnit}:0{minuutit}:0{sekunnit}"
                else:
                    aika = f"0{tunnit}:0{minuutit}:{sekunnit}"
            else:
                if sekunnit < 10:
                    aika = f"0{tunnit}:{minuutit}:0{sekunnit}"
                else:
                    aika = f"0{tunnit}:{minuutit}:{sekunnit}"
        else:
            if minuutit < 10:
                if sekunnit < 10:
                    aika = f"{tunnit}:0{minuutit}:0{sekunnit}"
                else:
                    aika = f"{tunnit}:0{minuutit}:{sekunnit}"
            else:
                if sekunnit < 10:
                    aika = f"{tunnit}:{minuutit}:0{sekunnit}"
                else:
                    aika = f"{tunnit}:{minuutit}:{sekunnit}"
 
        return aika
 
    def silmukka(self):
        kello = pygame.time.Clock()
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto()
            self.sekunti += 1
            self.ajan_toiminta()
            self.hirvioiden_maara = self.aika // 3
            kello.tick(60)
 
    def tutki_tapahtumat(self):
        self.kolikkojen_toiminta()
        self.hirvioiden_toiminta()
 
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = True
 
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = False
 
            if tapahtuma.type == pygame.QUIT:
                exit()
 
        if self.x < 590:
            if self.oikealle:
                self.x += 3
        if self.x > 0:
            if self.vasemmalle:
                self.x -= 3
 
 
    def piirra_naytto(self):
        if self.aika > self.paras_aika:
            self.paras_aika = self.aika
        if self.kolikkoja > self.paras_kolikkomaara:
            self.paras_kolikkomaara = self.kolikkoja
 
        self.aika = self.sekunnit + (self.minuutit*60) + ((self.tunnit*60)*60)
        self.ennatys_aika = f"Paras aika: 0"
        self.ennatys_kolikkomaara  = f"Paras kolikkomäärä: 0"
 
        self.naytto.fill((0, 0, 255))
 
        for i in range(self.maara):
            self.naytto.blit(self.kolikko, (self.kolikot[i][0], self.kolikot[i][1]))
        for i in range(self.hirvioiden_maara):
            self.naytto.blit(self.hirvio, (self.hirviot[i][0], self.hirviot[i][1]))
 
        self.naytto.blit(self.robo, (self.x, self.y))
 
        fontti = pygame.font.SysFont("Arial", 24)
        pygame.draw.rect(self.naytto, (0, 0, 0), (10, 10, 623, 28))
        teksti = fontti.render(f"Kolikot: {self.kolikkoja}   Paras: {self.paras_kolikkomaara}", True, (255, 255, 255))
        teksti2 = fontti.render(f"Aika: {self.ajan_laskenta(self.aika)}   Paras: {self.ajan_laskenta(self.paras_aika)}", True, (255, 255, 255))
        self.naytto.blit(teksti, (10, 10))
        self.naytto.blit(teksti2, (290, 10))
 
        pygame.display.flip()
 
if __name__ == "__main__":
    Rahasade()