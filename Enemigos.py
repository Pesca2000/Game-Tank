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



class Enemigo(pygame.sprite.Sprite):

    def __init__(self, pos=[100,100], cl=AZUL):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.click=False

    def update(self):
        if self.click:
            self.rect.center=pygame.mouse.get_pos()

class Generador(pygame.sprite.Sprite):

    def __init__(self, pos=[400,400], cl=AMARILLO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([80,80])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.temp=random.randrange(30,60)

    def update(self):
        self.temp -= 1

class Generador2(pygame.sprite.Sprite):

    def __init__(self, pos=[400,400], cl=AMARILLO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([80,80])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.temp=random.randrange(30,60)

    def update(self):
        self.temp -= 1
        

class TanqueEnemigo(pygame.sprite.Sprite):

    def __init__(self, pos=[400,400]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.mtanq=m_tanq
        self.limite=[4,4,4,4]
        self.col=1
        self.fil=0
        self.image = self.mtanq[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):

        if self.velx != self.vely:
            self.image = self.mtanq[self.fil][self.col]
        if self.col <4:
            self.col
        else:
            self.col=0
        
        self.rect.x += self.velx
        self.rect.y += self.vely
        

if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    generadores=pygame.sprite.Group()
    generadores=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    TanquesEnemigos=pygame.sprite.Group()

    c=Enemigo()
    enemigos.add(c)

    g=Generador()
    generadores.add(g)

    tanq=pygame.image.load('enemigos1.png')
    info_tanq=tanq.get_rect()

    ancho_img=info_tanq[2]
    alto_img=info_tanq[3]

    filas_tanq=[]
    sp_ancho_tanq=4
    sp_alto_tanq=4
    desp_x_tanq= 85
    desp_y_tanq= 85
    m_tanq=[]
    
    for i in range (sp_alto_tanq): 
        filas=[]
        for j in range(sp_ancho_tanq): 
            cuadro_tanq = tanq.subsurface(desp_x_tanq*j ,desp_y_tanq*i,85,85)
            filas_tanq.append(cuadro_tanq)
        m_tanq.append(filas_tanq)


    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True




        for g in generadores:
            if g.temp < 0:
                r=TanqueEnemigo(g.rect.center )
                r.velx=-4
                TanquesEnemigos.add(r)
                dado=random.randrange(100)
                if dado > 50:
                    r.col = 1
                    r.fil = 2
                    r.velx=-4
                else:
                    r.col = 1
                    r.velx=4
                g.temp=random.randrange(30,60)

        for r in TanquesEnemigos:
            if (r.rect.x < 0) or (r.rect.right > ANCHO) :
                TanquesEnemigos.remove(r)


        enemigos.update()
        generadores.update()
        TanquesEnemigos.update()

        pantalla.fill(NEGRO)

        
        generadores.draw(pantalla)
        enemigos.draw(pantalla)
        TanquesEnemigos.draw(pantalla)

        pygame.display.flip()
        reloj.tick(40)
        
            
    pygame.quit()