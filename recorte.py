import pygame
import random
import configparser


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

    def __init__(self,img,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    bloques=pygame.sprite.Group()

    fondo_p=pygame.image.load('mapa02.png')

    fnt_mapa=configparser.ConfigParser()
    fnt_mapa.read('mapa.map')

    nom_archivo=fnt_mapa.get('general','archivo')

    fondos=pygame.image.load(nom_archivo)
    info=fondos.get_rect()

    ancho_img=info[2]
    alto_img=info[3]

    filas=[]
    sp_ancho= 32
    sp_alto=12
    desp_x=32
    desp_y=32
    m=[]
    
    for i in range (sp_alto): 
        for j in range(sp_ancho): 
            cuadro = fondos.subsurface(desp_x*j ,desp_y*i,32,32)
            filas.append(cuadro)
        m.append(filas)
        

    mapa=fnt_mapa.get('general','mapa')
    print ('Mapa')
    print (mapa)
    filas=mapa.split('\n')

    
    j=0
    for fila in filas:
        i=0
        for col in fila:
            if col != '.':
                inf=fnt_mapa.get(col,'info')
                fl=int (fnt_mapa.get(col,'fil'))
                cl=int (fnt_mapa.get(col,'col'))
                print(col, inf,fl,cl)
                #bloque (imagen,posicion)
                b=Bloque(m[fl][cl],[desp_x*i,desp_y*j])
                bloques.add(b)
                #pantalla.blit(m[fl][cl], [desp_x*i,desp_y*j])
            i+=1
        j+=1

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True  

        pantalla.blit(fondo_p,[0,0])
        bloques.draw(pantalla)

        pygame.display.flip()     

    pygame.quit()
            
