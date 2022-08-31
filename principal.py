import pygame
import random


VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
BLANCO=[255,255,255]
NEGRO=[0,0,0]
AMARILLO=[255, 140, 0]
NARANJA=[255, 69, 0]
PURPURA=[128, 0, 128]
ROSADO=[255, 192, 203]
ANCHO=1200
ALTO=600

class Jugador(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.rect.y=200
        self.velx=0
        self.vely=0
        self.puntos=0
        self.salud=100
        

    def update(self):
        self.rect.x += self.velx
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

        if self.rect.left <= 0:
            self.rect.left = 0

        self.rect.y += self.vely
        if self.rect.bottom > ALTO:
            self.rect.top = 0

        if self.rect.top < 0:
            self.rect.bottom = ALTO

class Punto(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]        
        
if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    jugadores=pygame.sprite.Group()
    punto=pygame.sprite.Group()

    j1=Jugador()
    jugadores.add(j1)

    n=10
    for i in range(n):
        x=random.randrange(10,ANCHO-50)
        y=random.randrange(10,ALTO-50)
        pos=[x,y]
        p=Punto(pos)
        punto.add(p)


    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                j1.velx=0
                j1.vely=0
                if event.key == pygame.K_RIGHT:
                    j1.velx = 5
                if event.key == pygame.K_LEFT:
                    j1.velx = -5
                if event.key == pygame.K_UP:
                    j1.vely = -5
                if event.key == pygame.K_DOWN:
                    j1.vely = 5
            if event.type == pygame.KEYUP:
                j1.velx=0
                j1.vely=0

        ls_col=pygame.sprite.spritecollide(j1,punto,False)
        for p in ls_col:
            #j1.puntos += 1
            #print ('Puntos del jugador', j1.puntos)
            j1.salud -= 10
            p.rect.x +=10
            p.rect.y +=5
            print ('Salud del jugador', j1.salud)
                 
                


        jugadores.update()
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        punto.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
            


    pygame.quit()
            
