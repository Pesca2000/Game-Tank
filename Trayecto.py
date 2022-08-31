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
        self.rect.y= 170
        self.velx=0
        self.vely=0
        self.puntos=0
        self.salud=100
        self.piso=False
        

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
            self.vely += cte

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
        

        
class Bala(pygame.sprite.Sprite):

    def __init__(self, pi, pf, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pi[0]
        self.rect.y=pi[1]       
        self.velx= 10
        self.ctes(pi,pf)

    def ctes(self,pi,pf):
        self.a = (pf[1]-pi[1])/(pf[0]-pi[0])
        x = pi[0]
        y = pi[1]
        self.b = y - (self.a * x)


    def update(self):
        self.rect.x += self.velx
        self.rect.y = (self.a * self.rect.x) + self.b

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
    Fuente=pygame.font.Font(None,32)

    lim_der=1100

    jugadores=pygame.sprite.Group()   
    balas=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()

    j1=Jugador()
    jugadores.add(j1)

    p=Plataforma([600,650],[80,30])
    plataformas.add(p)
    
    pl=Plataforma([700,550],[80,30])
    plataformas.add(pl)
    
    po=Plataforma([1400,550],[80,30])
    plataformas.add(po)
 
    texto='Fin del juego'
    ubicacion_mesaje=[500,300]
    reloj=pygame.time.Clock()
    fin=False
    fin_juego=False

    while (not fin) and (not fin_juego):
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
                    j1.vely = -15
                if event.key == pygame.K_s:
                    j1.vely = 5
                
            if event.type == pygame.KEYUP:
                j1.velx=0
                j1.vely=0    
            if event.type == pygame.MOUSEBUTTONDOWN: 
               if event.button == 1:
                   pi=j1.rect.center
                   pf= event.pos
                   b=Bala(pi,pf)

                   if pi[0] < pf[0]:
                       b.velx=10
                   else:
                       b.velx=-10
                   balas.add(b)

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


        for b in balas:
            if b.rect.y < - 40:
                balas.remove(b)


        if len(jugadores)==0:
            fin_juego=True
            texto='FIN DEL JUEGO: HAS PERDIDDO'


        jugadores.update()
        balas.update()
        plataformas.update()

        pantalla.fill(NEGRO)

        info='Salud: ' +str(j1.salud)
        cl_salud=VERDE
        if j1.salud <= 60:
            cl_salud = AMARILLO
        if j1.salud <= 20:
            cl_salud=ROJO
        txt_info=Fuente.render(info, True , cl_salud)

        pantalla.blit(txt_info, [10,10])

        jugadores.draw(pantalla)
        balas.draw(pantalla)
        plataformas.draw(pantalla)

        pygame.display.flip()
        reloj.tick(40)

   #Ciclo mensaje de finalizacion         
    Fuente=pygame.font.Font(None,32)

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        pantalla.fill(NEGRO)
        img_texto=Fuente.render(texto, True, BLANCO)
        pantalla.blit(img_texto,[500,400])
        pygame.display.flip()
        


    pygame.quit()
            
