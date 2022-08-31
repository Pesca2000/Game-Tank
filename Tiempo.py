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
    Fuente=pygame.font.Font(None,32)

    tasa=40
    con=0

    reloj=pygame.time.Clock()
    fin=False
    fin_juego=False
    while not fin :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


        segundo=con//(tasa-20)
        minuto=segundo//60
        if (segundo & 60) == 0 :
            segundo = 0
            

        texto=str(minuto) + ':' + str(segundo)
        pantalla.fill(NEGRO)
        img_texto=Fuente.render(texto, True, BLANCO)
        pantalla.blit(img_texto,[500,400])

        pygame.display.flip()
        reloj.tick(tasa)
        con+=1

    pygame.quit()