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
        self.rect.y=ALTO - 70
        self.velx=0
        self.vely=0
        self.bloques=pygame.sprite.Group()
        self.puntos=0
        self.salud=100
        

    def update(self):
        self.rect.x += self.velx
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            self.velx=0

        if self.rect.left <= 0:
            self.rect.left = 0
            self.velx=0

        ls_col=pygame.sprite.spritecollide(self, self.bloques, False) 
        for b in ls_col:

            if self.velx >0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    self.velx= 0

            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    self.velx=0
        
        self.rect.y += self.vely
        if self.rect.bottom > ALTO:
            self.rect.top = 0
            self.vely=0

        if self.rect.top < 0:
            self.rect.bottom = ALTO
            self.vely=0

        ls_col=pygame.sprite.spritecollide(self, self.bloques, False) 
        for b in ls_col:

            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.vely=0
                    
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    self.vely=0

class Bloque(pygame.sprite.Sprite):
    def __init__(self,dim,pos,cl=AMARILLO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(dim)
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
          
if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    fondo=pygame.image.load('fondo2.jpg')
    info= fondo.get_rect()
    f_ancho=info[2]

    lim_ventana=ANCHO - f_ancho
    print ('ancho: ', info[2], 'alto: ', info[3])


    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    j1=Jugador()
    jugadores.add(j1)

   

    j1.bloques=bloques

    f_posx=0
    f_velx= -5
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                j1.velx=0
                j1.vely=0
                if event.key == pygame.K_d:
                    j1.velx = 5
                if event.key == pygame.K_a:
                    j1.velx = -5
                if event.key == pygame.K_w:
                    j1.vely = -5
                if event.key == pygame.K_s:
                    j1.vely= 5
            if event.type == pygame.KEYUP:
                j1.velx=0
                j1.vely=0          

        jugadores.update()

        pantalla.fill(NEGRO)
        pantalla.blit(fondo, [f_posx,-200])

        jugadores.draw(pantalla)    
        bloques.draw(pantalla) 

        pygame.display.flip()
        reloj.tick(40)
        if f_posx > lim_ventana:
            f_posx += f_velx

     
    pygame.quit()
            
