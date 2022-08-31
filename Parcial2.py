import pygame
import random
import configparser


VERDE=[0,255,0]
ROJO=[250,3,3]
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
        self.m=m
        self.limite=[4,4,4,4]
        self.col=0
        self.fil=2
        self.image = self.m[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.rect.y= 170
        self.velx=0
        self.vely=0
        self.puntos=0
        self.salud=1000
        self.puntaje=0
        self.bloques=pygame.sprite.Group()
        

    def update(self):

        print (self.col)
        print (self.fil)
        if self.velx != self.vely:
            self.image = self.m[self.fil][self.col]
        if self.col <0:
            self.col
        else:
            self.col=0

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

'''class Bloque(pygame.sprite.Sprite):

    def __init__(self,img,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]'''

class Balas (pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.m2=m2
        self.limite=[3,3,3,3]
        self.col=0
        self.fil=0
        self.image = self.m2[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]       
        self.velx= 0
        self.vely= 0

    def update(self):

        if self.velx != self.vely:
            self.image = self.m2[self.fil][self.col]
        if self.col <0:
            self.col
        else:
            self.col

        self.rect.x += self.velx
        self.rect.y += self.vely


if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    Fuente=pygame.font.Font(None,32)
    

    bloques=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    balas=pygame.sprite.Group()


    fondo=pygame.image.load('fondojuego.png')
    info= fondo.get_rect()
    f_ancho=info[2]
    f_alto=info[3]

    lim_ventana=ANCHO - f_ancho
    lim_ventanaAlto=ALTO - f_alto

    


    fondos=pygame.image.load('pruebatanque.png')
    info=fondos.get_rect()

    ancho_img=info[2]
    alto_img=info[3]

    filas=[]
    sp_ancho=3
    sp_alto=4
    desp_x= 64
    desp_y= 64
    m=[]
    
    for i in range (sp_alto): 
        filas=[]
        for j in range(sp_ancho): 
            cuadro = fondos.subsurface(desp_x*j ,desp_y*i,64,64)
            filas.append(cuadro)
        m.append(filas)

    j1=Jugador()
    jugadores.add(j1)

    #Recorte de balas

    bal=pygame.image.load('balas.png')
    info_bala=bal.get_rect()

    ancho_img2=info_bala[2]
    alto_img2=info_bala[3]

    filas2=[]
    sp_ancho2 = 4
    sp_alto2 = 4
    desp_x2= 65
    desp_y2= 40
    m2=[]
    
    for i in range (sp_alto2): 
        filas2=[]
        for j in range(sp_ancho2): 
            cuadro2 = bal.subsurface(desp_x2*j ,desp_y2*i,65,40)
            filas2.append(cuadro2)
        m2.append(filas2)
   

    

    
    print ('ancho: ', info[2], 'alto: ', info[3])

    lim_movDer =1100
    lim_movIzq =10
    lim_movAba =550
    lim_movArr = 10
    f_posx= 0
    f_velx= -5
    f_posy= 0
    f_vely= -5

    fnt_mapa=configparser.ConfigParser()
    fnt_mapa.read('mapa.map')

    nom_archivo=fnt_mapa.get('general','archivo')

    fondos=pygame.image.load(nom_archivo)
    info=fondos.get_rect()

    ancho_img=info[2]
    alto_img=info[3]
     
    mapa=fnt_mapa.get('general','mapa')
    print ('Mapa')
    print (mapa)
    filas=mapa.split('\n')

    

    
    '''j=0
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
                pantalla.blit(m[fl][cl], [desp_x*i,desp_y*j])
            i+=1
        j+=1'''

    tasa=40
    con=0
    minuto=0
    segundo=0

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True  
            if event.type == pygame.KEYDOWN:
                j1.velx=0
                j1.vely=0
                if event.key == pygame.K_RIGHT:
                    j1.fil = 2
                    j1.velx = 5
                if event.key == pygame.K_LEFT:
                    j1.fil = 1
                    j1.velx = -5
                if event.key == pygame.K_UP:
                    j1.fil = 3
                    j1.vely = -5
                if event.key == pygame.K_DOWN:
                    j1.fil = 0
                    j1.vely = 5
                if event.key == pygame.K_j:
                    if  (j1.fil == 2) :
                        pos=[j1.rect.x + 30 , j1.rect.y + 5]
                        
                        
                        b1=Balas(pos)
                        balas.add(b1)
                        b1.fil = 2
                        b1.col = 0 
                        b1.velx += 10 
                        

                    if (j1.fil == 0) :
                        pos=[j1.rect.x - 8 , j1.rect.y + 10]
                        
                        
                        b1=Balas(pos)
                        balas.add(b1)
                        b1.fil = 2
                        b1.col = 2
                        b1.vely += 10

                    if (j1.fil == 1) :
                        pos=[j1.rect.x + 10 , j1.rect.y + 5]
                        
                        
                        b1=Balas(pos)

                        balas.add(b1)
                        b1.fil = 2
                        b1.col = 3
                        b1.velx -= 10

                    if  (j1.fil == 3) :
                        pos=[j1.rect.x + 7 , j1.rect.y - 20]
                        
                        
                        b1=Balas(pos)
                        balas.add(b1)
                        b1.fil = 2
                        b1.col = 1
                        b1.vely -= 10



            #Condicion para disparo de tigre azul

                if event.key == pygame.K_k:

                    if  (j1.fil == 2):
                        pos=[j1.rect.x + 30 , j1.rect.y + 5]
                        
                        
                        b1=Balas(pos)
                        balas.add(b1) 
                        b1.fil=1
                        b1.col = 0
                        b1.velx += 10 
                        

                    if (j1.fil == 0):
                        pos=[j1.rect.x - 8 , j1.rect.y + 10]
                        
                        
                        b1=Balas(pos)
                        balas.add(b1)
                        b1.fil=1
                        b1.col = 2
                        b1.vely += 10

                    if (j1.fil == 1):
                        pos=[j1.rect.x - 20 , j1.rect.y + 10]
                        
                        
                        b1=Balas(pos)
                        balas.add(b1)
                        b1.fil=1
                        b1.col = 3
                        b1.velx -= 10

                    if  (j1.fil == 3):
                        pos=[j1.rect.x + 7 , j1.rect.y - 20]
                        
                        
                        b1=Balas(pos)
                        balas.add(b1)
                        b1.fil=1
                        b1.col = 1
                        b1.vely -= 10

                #Condicion de disparo bola amarilla grande
                if event.key == pygame.K_s:
                    if  (j1.fil == 2) :
                        pos=[j1.rect.x + 30 , j1.rect.y + 5]
                        
                        
                        b1=Balas(pos)
                        balas.add(b1)
                        b1.fil = 3
                        b1.col = 0 
                        b1.velx += 10 
                        

                    if (j1.fil == 0) :
                        pos=[j1.rect.x - 8 , j1.rect.y + 10]
                        
                        
                        b1=Balas(pos)
                        balas.add(b1)
                        b1.fil = 3
                        b1.col = 2
                        b1.vely += 10

                    if (j1.fil == 1) :
                        pos=[j1.rect.x - 20 , j1.rect.y + 5]
                        
                        
                        b1=Balas(pos)

                        balas.add(b1)
                        b1.fil = 3
                        b1.col = 3
                        b1.velx -= 10

                    if  (j1.fil == 3) :
                        pos=[j1.rect.x + 3 , j1.rect.y - 20]
                        
                        
                        b1=Balas(pos)
                        balas.add(b1)
                        b1.fil = 3
                        b1.col = 1
                        b1.vely -= 10

            if event.type == pygame.KEYUP:
                j1.velx=0
                j1.vely=0                
                

        jugadores.update()
        balas.update()

        pantalla.fill(NEGRO)

        
        pantalla.blit(fondo,[1000,2000])
        pantalla.blit(fondo, [f_posx,f_posy])

        a=(0,0)
        b=(2000,0)
        c=(0,35)
        d=(2000,35)

        ls=[a,c,d,b]
        pygame.draw.polygon(pantalla,NEGRO,ls)


        info='VIDA DEL TANQUE: ' +str(j1.salud)
        cl_salud=BLANCO
        if j1.salud <= 60:
            cl_salud = AMARILLO
        if j1.salud <= 20:
            cl_salud=ROJO
        txt_info=Fuente.render(info, True , cl_salud)
        pantalla.blit(txt_info, [10,10])

        info='PUNTAJE: ' +str(j1.puntaje)
        cl_puntaje=BLANCO
        txt_info=Fuente.render(info, True , cl_puntaje)
        pantalla.blit(txt_info, [1000,10])

        info='BONUS: ' +str(j1.puntaje)
        cl_puntaje=BLANCO
        txt_info=Fuente.render(info, True , cl_puntaje)
        pantalla.blit(txt_info, [300,10])

        
        
        #bloques.draw(pantalla)
        balas.draw(pantalla)
        jugadores.draw(pantalla)

       #Cronometro
        if (segundo == 0):
            minuto +=1
        segundo=(con//(tasa)) % 60    
               
        texto=str((minuto//10)-1) + ':' + str(segundo)
        img_texto=Fuente.render(texto, True,BLANCO)
        pantalla.blit(img_texto,[600,10])

        pygame.display.flip()
        reloj.tick(tasa)
        con+=1
       
        #Limites y movimiento de la pantalla
        
        if j1.rect.right > lim_movDer:
            j1.rect.right = lim_movDer
            

            if f_posx > lim_ventana:
                f_posx +=f_velx
                
                for b in bloques:
                    b.rect.x += f_velx

        if j1.rect.left < lim_movIzq:
            j1.rect.left = lim_movIzq

            if f_posx <= 0:
                f_posx -= f_velx

                for b in bloques:
                    b.rect.x += f_velx

        if j1.rect.bottom > lim_movAba:
            j1.rect.bottom = lim_movAba

            if f_posy >= lim_ventanaAlto:
                f_posy += f_vely

                for b in bloques:
                    b.rect.y += f_vely

        if j1.rect.top < lim_movArr:
            j1.rect.top = lim_movArr

            if f_posy <= 0:
                f_posy -= f_vely

                for b in bloques:
                    b.rect.y += f_vely 

    pygame.quit()
            
