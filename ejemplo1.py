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


if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])


    fondos=pygame.image.load('terrenogen.png')
    info=fondos.get_rect()

    ancho_img=info[2]
    alto_img=info[3]

    filas=[]
    sp_ancho=32
    sp_alto=12
    desp_x=32
    desp_y=32
    m=[]
    
    for i in range (sp_alto): 
        filas=[]
        for j in range(sp_ancho): 
            cuadro = fondos.subsurface(desp_x*j ,desp_y*i,32,32)
            filas.append(cuadro)
        m.append(filas)


    pantalla.blit(m[1][1], [0,0])
    pygame.display.flip()


    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True       

    pygame.quit()
            
