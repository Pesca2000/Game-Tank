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
        self.rect.x=200
        self.rect.y=ALTO - 300
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

    fondo=pygame.image.load('mapa02.png')
    info= fondo.get_rect()
    f_ancho=info[2]
    f_alto=info[3]

    lim_ventana=ANCHO - f_ancho
    lim_ventanaAlto=ALTO - f_alto


    print ('ancho: ', info[2], 'alto: ', info[3])

    lim_movDer =1100
    lim_movIzq =10
    lim_movAba =550
    lim_movArr = 10


    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    j1=Jugador()
    jugadores.add(j1)

    b1=Bloque ([50,80], [1400,300])
    bloques.add(b1)
    j1.bloques=bloques

    f_posx= 0
    f_velx= -5
    f_posy= 0
    f_vely= -5

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
        pantalla.blit(fondo, [f_posx,f_posy])

        jugadores.draw(pantalla)    
        bloques.draw(pantalla) 

        pygame.display.flip()
        reloj.tick(40)
        if j1.rect.right > lim_movDer:
            #j1.velx = 0
            j1.rect.right = lim_movDer

            if f_posx > lim_ventana:
                f_posx +=f_velx

                for b in bloques:
                    b.rect.x += f_velx

        if j1.rect.left <= lim_movIzq:
            j1.rect.left = lim_movIzq

            if f_posx <= 0:
                f_posx -= f_velx

                for b in bloques:
                    b.rect.x += f_velx

        if j1.rect.bottom >= lim_movAba:
            j1.rect.bottom = lim_movAba

            if f_posy >= lim_ventanaAlto:
                f_posy += f_vely

                for b in bloques:
                    b.rect.y += f_vely

        if j1.rect.top < lim_movArr:
            j1.rect.top = lim_movArr

            if f_posy <= 0:
                f_posy -= f_vely

                for b in bloques:
                    b.rect.y += f_vely

     
    pygame.quit()
            
