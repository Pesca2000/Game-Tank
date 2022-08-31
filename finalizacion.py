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
        self.puntos=0
        self.salud=100
        

    def update(self):
        self.rect.x += self.velx
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

        if self.rect.left <= 0:
            self.rect.left = 0

class Rival(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]       
        self.liminf=50
        self.limsup=1100
        self.velx= 5
        self.disparar=False
        self.temp=random.randrange(30,60)

    def update(self):
        if self.temp>0:
            self.temp-=1

        self.rect.x += self.velx
        if self.rect.right > self.limsup:
            self.velx = -5

        if self.rect.left < self.liminf:
            self.velx = 5
        
class Bala(pygame.sprite.Sprite):

    def __init__(self, pos, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,20])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]       
        self.vely= -10

    def update(self):
        self.rect.y += self.vely

def Crear_oleada(n):
        grupo=pygame.sprite.Group()
        for i in range(n):
            x=random.randrange(50,1000)
            y=random.randrange(50,500)
            pos=[-1*x,y]
            r=Rival(pos)
            rivales.add(r)
        return rivales    

if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    Fuente=pygame.font.Font(None,32)

    jugadores=pygame.sprite.Group()
    rivales=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balas_rival=pygame.sprite.Group()

    j1=Jugador()
    jugadores.add(j1)

    rivales= Crear_oleada(5)
    oleada=1
 
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
            if event.type == pygame.KEYUP:
                j1.velx=0
                j1.vely=0    
            if event.type == pygame.MOUSEBUTTONDOWN:
               
               if event.button == 1:
                   pos=[j1.rect.x + 20 , j1.rect.y]
                   b=Bala(pos)
                   balas.add(b)

        for r in rivales:
            if r.temp ==0:
                r.disparar=True

            if r.disparar:
                pos=[r.rect.x + 20 , r.rect.bottom]
                b=Bala(pos, ROJO)
                b.vely=10
                balas_rival.add(b)
                r.disparar=False
                r.temp=random.randrange(30,60)

        for b in balas:
            if b.rect.y < - 40:
                balas.remove(b)

            ls_col=pygame.sprite.spritecollide(b, rivales, True)
                         
            if len(ls_col)>0:
                balas.remove(b) 

        for b in balas_rival:
            if b.rect.y > (ALTO + 5 ):
                balas_rival.remove(b)

            ls_col=pygame.sprite.spritecollide(j1, balas_rival, True) 
            for b in ls_col:
                j1.salud -= 20
                if j1.salud <= 0:
                    jugadores.remove(j1)

        if len(rivales)==0:
            if oleada == 2:
                fin_juego=True
                texto='FIN DEL JUEGO: HAS VENCIDO'
            else:
                rivales=Crear_oleada(8)
                oleada += 1
            

        if len(jugadores)==0:
            fin_juego=True
            texto='FIN DEL JUEGO: HAS PERDIDDO'

        jugadores.update()
        rivales.update()
        balas.update()
        balas_rival.update()

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
        rivales.draw(pantalla)
        balas.draw(pantalla)
        balas_rival.draw(pantalla)
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
            
