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

class Cuadro(pygame.sprite.Sprite):

    def __init__(self, pos=[100,100], cl=BLANCO):
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

    def __init__(self, pos=[100,500], cl=ROJO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([80,80])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        

class Raton(pygame.sprite.Sprite):

    def __init__(self, pos=[400,400], cl=VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        

if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    generadores=pygame.sprite.Group()
    generadores2=pygame.sprite.Group()
    cuadros=pygame.sprite.Group()
    ratones=pygame.sprite.Group()

    c=Cuadro()
    cuadros.add(c)

    g=Generador()
    generadores.add(g)

    g2=Generador2()
    generadores2.add(g2)

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for g in generadores2:
                    if g.rect.collidepoint(event.pos):
                        c=Cuadro(event.pos)
                        c.click=True
                        cuadros.add(c)

                for c in cuadros:
                    if c.rect.collidepoint(event.pos):
                        c.click=True

            if event.type == pygame.MOUSEBUTTONUP:
                for c in cuadros:
                    c.click = False



        for g in generadores:
            if g.temp < 0:
                r=Raton(g.rect.center)
                r.velx=-5
                ratones.add(r)
                dado=random.randrange(100)
                if dado > 50:
                    r.velx=-5
                else:
                    r.velx=5
                g.temp=random.randrange(30,60)

        for r in ratones:
            if (r.rect.x < 0) or (r.rect.right > ANCHO) :
                ratones.remove(r)


        cuadros.update()
        generadores.update()
        ratones.update()

        pantalla.fill(NEGRO)

        
        generadores.draw(pantalla)
        generadores2.draw(pantalla)
        cuadros.draw(pantalla)
        ratones.draw(pantalla)

        pygame.display.flip()
        reloj.tick(40)
        
            
    pygame.quit()