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
        self.limite=[3,3,2,4,1,3,4,4,6.0]
        self.col=0
        self.fil=1
        self.image = self.m[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.rect.y= 170
        self.velx=0
        self.vely=0
        self.puntos=0
        self.salud=100
        

    def update(self):
        #Animacion
       # if self.velx != self.vely:
        self.image = self.m[self.fil][self.col]
        if self.col < self.limite[self.fil]:
            self.col+=1
        else:
            self.col=0
            self.fil=1

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
            
class Barril(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,70])
        self.image.fill(VERDE)
        self.grito=pygame.mixer.Sound('grito.ogg')
        self.rect = self.image.get_rect()
        self.rect.x=320
        self.rect.y=170
        self.velx=0
        self.liminf=self.rect.bottom - 20
        self.limsup=self.rect.bottom + 20

    def update(self):
        self.rect.x+=self.velx

        if self.velx > 0:
            self.velx -= 1



if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])


    jugadores=pygame.sprite.Group()
    barriles=pygame.sprite.Group()

    fondos=pygame.image.load('ken.png')
    info=fondos.get_rect()

    ancho_img=info[2]
    alto_img=info[3]

    filas=[]
    sp_ancho=7
    sp_alto=10
    desp_x=70
    desp_y=80
    m=[]
    
    for i in range (sp_alto): 
        filas=[]
        for j in range(sp_ancho): 
            cuadro = fondos.subsurface(desp_x*j ,desp_y*i,70,80)
            filas.append(cuadro)
        m.append(filas)
   

    j1=Jugador(m)
    jugadores.add(j1)

    b=Barril()
    barriles.add(b)

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
                    j1.velx = 5
                if event.key == pygame.K_a:
                    j1.velx = -5
                if event.key == pygame.K_w:
                    j1.vely = -5
                if event.key == pygame.K_s:
                    j1.vely = 5
                #Pu??o
                if event.key == pygame.K_j:
                    j1.fil = 2
                    j1.col = 0
                #Patada
                if event.key == pygame.K_k:
                    j1.fil = 6
                    j1.col = 0                
            if event.type == pygame.KEYUP:
                j1.velx=0
                j1.vely=0
                          

        ls_col=pygame.sprite.spritecollide(j1,barriles,False)

        for b in ls_col:
            if j1.fil==2 and ((j1.rect.bottom > b.liminf) and (j1.rect.bottom < b.limsup)):
                b.velx=10
                b.grito.play()

        for b in ls_col: 
            if j1.fil==6 and ((j1.rect.bottom > b.liminf) and (j1.rect.bottom < b.limsup)):
                b.velx=20

        jugadores.update()
        barriles.update()

        pantalla.fill(NEGRO)

        '''pygame.draw.line(pantalla,BLANCO,[b.rect.left-40,b.rect.bottom],[b.rect.right+40,b.rect.bottom])
        pygame.draw.line(pantalla,ROJO,[b.rect.left-40,b.liminf],[b.rect.right+40,b.liminf])
        pygame.draw.line(pantalla,ROJO,[b.rect.left-40,b.limsup],[b.rect.right+40,b.limsup])'''

        #pantalla.blit(m[0][0], [400,100])
        if j1.rect.bottom < b.rect.bottom:

            jugadores.draw(pantalla)
            barriles.draw(pantalla)
        else:
            barriles.draw(pantalla)
            jugadores.draw(pantalla)

        pygame.display.flip()
        reloj.tick(20)
        
            
    pygame.quit()
            