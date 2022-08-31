import pygame
import random


VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
BLANCO=[255,255,255]
NEGRO=[0,0,0]
AMARILLO=[250, 200, 0]
NARANJA=[255, 69, 0]
PURPURA=[128, 0, 128]
ROSADO=[255, 192, 203]
ANCHO=1200
ALTO=800

class Jugador(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.rect.y=0
        self.velx=0
        self.vely=0
        self.piso=0
        self.salud=100
        
    def update(self):
            self.rect.x += self.velx
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
                self.velx=0

            if self.rect.left <= 0:
                self.rect.left = 0
                self.velx=0
            if not self.piso:
                cte=0.5
                self.vely+=cte
            
            self.rect.y += self.vely
            
            if self.rect.bottom > ALTO:
                self.rect.bottom = ALTO
                self.vely=0
                self.piso=True
            else:
                self.piso=False
                
            if self.rect.top <= 0:
                self.rect.top = 0
                self.velx=0
                self.piso=False
                
class Plataforma(pygame.sprite.Sprite):

    def __init__(self, pos, dim, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(dim)
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
    
    def update(self):
        self.rect.x+=self.velx       
        
if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    #Ciclo mensaje de finalizacion
    Fuente=pygame.font.Font(None, 32)
    
    lim_der=1100
    
    jugadores=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    
    j1=Jugador()
    jugadores.add(j1)
    
    p=Plataforma([600,650],[80,30])
    plataformas.add(p)
    
    pl=Plataforma([700,550],[80,30])
    plataformas.add(pl)
    
    po=Plataforma([1400,550],[80,30])
    plataformas.add(po)
    
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                '''j1.velx=0
                j1.vely=0'''
                if event.key == pygame.K_d:
                    j1.velx = 5
                if event.key == pygame.K_a:
                    j1.velx = -5
                '''if event.key == pygame.K_s:
                    j1.vely= 5'''
                if event.key == pygame.K_w:
                    j1.vely = -15
                    j1.ppiso=False
            if event.type == pygame.KEYUP:
                if event.key != pygame.K_w:
                    j1.velx=0
                    j1.vely=0    
            
        #Control
        ls_col=pygame.sprite.spritecollide(j1,plataformas,False)
        for p in ls_col:
            if j1.vely < 0:
                if j1.rect.top < p.rect.bottom:
                    j1.rect.top = p.rect.bottom
                    j1.vely=0
            else:
                if j1.rect.bottom > p.rect.top:
                    j1.rect.bottom = p.rect.top
                    j1.vely=0
                    j1.piso=True
            
        if j1.rect.right > lim_der:
            j1.rect.right = lim_der
            #j1.velx=0
            for p in plataformas:
                p.velx=-5  
                
        else:
            for p in plataformas:
                p.velx=0 
    
        jugadores.update()
        plataformas.update()
        
        pantalla.fill(NEGRO)
        
        jugadores.draw(pantalla)
        plataformas.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
    
pygame.quit()