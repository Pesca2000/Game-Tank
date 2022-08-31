import pygame
import random 
import json


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

    bloques=pygame.sprite.Group()

    fondo=pygame.image.load('fondocreado.png')
    info= fondo.get_rect()
    f_ancho=info[2]

    nom_archivo='fondo.json'
    with open(nom_archivo) as archivo:
        datos=json.load(archivo)

    
    capas=datos['layers']

    
    mapa=capas[1]['data']
    limite=capas[1]['width']

    con=0
    ls=[]
    posx=0
    posy=0
    for e in mapa:
        if e !=0:
            b=Bloque([64,64],[posx*64,posy*64])
            bloques.add(b)
        con+=1
        posx+=1
        if con >= limite:
            print(ls)
            ls=[]
            con=0
            posx=0
            posy+=1

    print('ancho: ', info[2], 'alto: ', info[3])
    f_posx=0
    f_velx=-5
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

    

        pantalla.fill(NEGRO)
        pantalla.blit(fondo, [f_posx,-200])

        
        bloques.draw(pantalla) 


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()