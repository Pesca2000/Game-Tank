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

    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.col=0
        self.fil=0
        self.image = self.m[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.rect.y=ALTO - 70
        self.velx=0
        self.vely=0
        self.puntos=0
        self.salud=100
        

    def update(self):
        if self.velx != self.vely:
            self.image = self.m[self.fil][self.col]
            if self.col <2:
                self.col+=1
            else:
                self.col=0

        self.rect.x += self.velx
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            self.velx=0

        if self.rect.left <= 0:
            self.rect.left = 0
            self.velx=0

        self.rect.y += self.vely
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
            self.vely=0

        if self.rect.top < 0:
            self.rect.top = 0
            self.vely=0
            



if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])


    jugadores=pygame.sprite.Group()
    fondos=pygame.image.load('animales.png')
    info=fondos.get_rect()

    ancho_img=info[2]
    alto_img=info[3]

    filas=[]
    sp_ancho=12
    sp_alto=8
    desp_x=32
    desp_y=32
    m=[]
    
    for i in range (sp_alto): 
        filas=[]
        for j in range(sp_ancho): 
            cuadro = fondos.subsurface(desp_x*j ,desp_y*i,32,32)
            filas.append(cuadro)
        m.append(filas)
   

    j1=Jugador(m)
    jugadores.add(j1)

    con=0
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
                    j1.fil=2
                    j1.velx = 5
                if event.key == pygame.K_a:
                    j1.fil=1
                    j1.velx = -5
                if event.key == pygame.K_w:
                    j1.fil=3
                    j1.vely = -5
                if event.key == pygame.K_s:
                    j1.fil=0
                    j1.vely = 5
            if event.type == pygame.KEYUP:
                j1.velx=0
                j1.vely=0
                


        jugadores.update()
        pantalla.fill(NEGRO)

        pantalla.blit(m[3][con], [400,100])
        jugadores.draw(pantalla)

        pygame.display.flip()
        reloj.tick(20)
        
            
    pygame.quit()
            