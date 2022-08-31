import pygame
import random
import configparser
import json

nom_archivo='mapa.json'
with open(nom_archivo) as archivo:
    datos=json.load(archivo)


capas=datos['layers']

tierra = capas[1]['data']
obstaculos = capas[3]['data']
fondopos = [1300,700]

Portal1 = True
Portal2= True
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

def obstaclechecker(px,py):
    x = px//32
    y = py//32
    i = y *120 + x
    #print(x,',',y,'-',obstaculos[i])
    if obstaculos[i] != 0 or tierra[i] == 0:
        return False
    return True

def random_gen(px,py):
    if px < 960:
        x = random.randint(320, 960)
        y = random.randint(640,1280)
        while not obstaclechecker(x,y):
            x = random.randint(320, 960)
            y = random.randint(640,1280)
        return x,y
    if py < 480:
        x = random.randint(1376, 2400)
        y = random.randint(96,480)
        while not obstaclechecker(x,y):
            x = random.randint(1376, 2400)
            y = random.randint(96,480)
        return x,y
    if px > 2880 :
        x = random.randint(2880, 3520)
        y = random.randint(640,1280)
        while not obstaclechecker(x,y):
            x = random.randint(1920, 2560)
            y = random.randint(640,1280)
        return x,y
    if py > 1440:
        x = random.randint(1376, 2400)
        y = random.randint(1440,1824)
        while not obstaclechecker(x,y):
            x = random.randint(1376, 2400)
            y = random.randint(1440,1824)
        return x,y

class Jugador(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.limite=[4,4,4,4]
        self.col=0
        self.fil=2
        self.image = self.m[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.rect.x=556
        self.rect.y= 228
        self.velx=0
        self.vely=0
        self.puntos=0
        self.salud= 400
        self.puntaje=0
        self.bloques=pygame.sprite.Group()
        self.px = 1888
        self.py = 960
        

    def update(self):
        
        if obstaclechecker(self.px+self.velx, self.py + self.vely):
            if self.velx != self.vely:
                self.image = self.m[self.fil][self.col]
            if self.col <0:
                self.col
            else:
                self.col=0
                   
            ls_colm=pygame.sprite.spritecollide(j1, vidas, True) 
            if len (ls_colm)>0:
                if (j1.rect.left > v.limizq) or (j1.rect.top > v.limarr) or (j1.rect.right < v.limder) or (j1.rect.bottom < v.limaba):
                    j1.salud = min(1000,j1.salud + 100)
                    v.vida.play()

            ls_colm=pygame.sprite.spritecollide(j1, extras, True) 
            if len (ls_colm)>0:
                if (j1.rect.left > bon.limizq) or (j1.rect.top > bon.limarr) or (j1.rect.right < bon.limder) or (j1.rect.bottom < bon.limaba):
                    j1.puntos+=100
                    bon.estrella.play()

            ls_colm=pygame.sprite.spritecollide(j1, monedas, True) 
            if len (ls_colm)>0:
                if (j1.rect.left > p.limizq) or (j1.rect.top > p.limarr) or (j1.rect.right < p.limder) or (j1.rect.bottom < p.limaba):
                    j1.puntaje+=100
                    p.moneda.play()

            ls_col=pygame.sprite.spritecollide(j1, balasrivales, True) 
            for br in ls_col:
                j1.salud -= 20

            

            

            '''ls_colm=pygame.sprite.spritecollide(j1, generadores, True) 
            if len (ls_colm)>0:
                if (j1.rect.left > p.limizq) or (j1.rect.top > p.limarr) or (j1.rect.right < p.limder) or (j1.rect.bottom < p.limaba):
                    j1.salud-=10'''

            self.rect.x += self.velx
            self.px += self.velx
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
                self.velx=0

            if self.rect.left <= 0:
                self.rect.left = 0
                self.velx=0

            self.rect.y += self.vely
            self.py += self.vely
            if self.rect.bottom > ALTO:
                self.rect.bottom = ALTO
                self.vely=0

            if self.rect.top < 0:
                self.rect.top = 0
                self.vely=0


class Bala (pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.m2=m2
        self.limite=[3,3,3,3]
        self.col=0
        self.fil=0
        self.image = self.m2[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.balas=pygame.mixer.Sound('shot.ogg')
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

class Vida(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.mcor=mcor
        self.limite=[1,1,1,1,1,1,1]
        self.col=0
        self.fil=0
        self.image = self.mcor[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.vida=pygame.mixer.Sound('health.ogg')
        self.rect.x= 800
        self.rect.y= 400     
        self.vely= 0
        self.activo=True
        self.limizq=self.rect.left 
        self.limder=self.rect.right 
        self.limarr=self.rect.top 
        self.limaba=self.rect.bottom 

    def update(self):
        if self.activo == True:
            self.image = self.mcor[self.fil][self.col]
            if self.col < 6:
                self.col+=1
            else:
                self.col=0

        self.rect.y += self.vely

class Extra(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.mest=mest
        self.limite=[1,1,1,1,1,1,1]
        self.col=0
        self.fil=0
        self.image = self.mest[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.estrella=pygame.mixer.Sound('star.ogg')
        self.rect.x= 400
        self.rect.y= 200    
        self.velx= 0 
        self.vely= 0
        self.activo=True
        self.limizq=self.rect.left 
        self.limder=self.rect.right 
        self.limarr=self.rect.top 
        self.limaba=self.rect.bottom 

    def update(self):
        if self.activo == True:
            self.image = self.mest[self.fil][self.col]
            if self.col < 6:
                self.col+=1
            else:
                self.col=0      

        self.rect.y += self.vely

class Moneda(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.mp=mp
        self.limite=[1,1,1,1,1,1,1]
        self.col=0
        self.fil=0
        self.image = self.mp[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.moneda=pygame.mixer.Sound('coin.ogg')
        self.rect.x= 900
        self.rect.y= 200    
        self.velx= 0 
        self.vely= 0
        self.activo=True
        self.limizq=self.rect.left 
        self.limder=self.rect.right 
        self.limarr=self.rect.top 
        self.limaba=self.rect.bottom 

    def update(self):
        if self.activo == True:
            self.image = self.mp[self.fil][self.col]
            if self.col < 6:
                self.col+=1
            else:
                self.col=0    

class Generador(pygame.sprite.Sprite):

    def __init__(self,col, mcueva, pos):
        pygame.sprite.Sprite.__init__(self)
        self.mc=mcueva
        self.limite=[4]
        self.col=col
        self.fil=0
        self.image = self.mc[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.limizq=self.rect.left 
        self.limder=self.rect.right 
        self.limarr=self.rect.top 
        self.limaba=self.rect.bottom

    def update(self):
        if self.velx == self.vely:
            self.image = self.mc[self.fil][self.col]
        if self.col < 3:
            self.col +=1
        else:
            self.col=0

class Generador2(pygame.sprite.Sprite):

    def __init__(self,col, mcueva2, pos):
        pygame.sprite.Sprite.__init__(self)
        self.mc2=mcueva2
        self.limite=[4]
        self.col=col
        self.fil=0
        self.image = self.mc2[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.vida = 1000
        self.limizq=self.rect.left 
        self.limder=self.rect.right 
        self.limarr=self.rect.top 
        self.limaba=self.rect.bottom

    def update(self):
        if self.velx == self.vely:
            self.image = self.mc2[self.fil][self.col]
        if self.col < 3:
            self.col +=1
        else:
            self.col=0

        ls_colm=pygame.sprite.spritecollide(g3, balas, True) 
        if len (ls_colm)>0:
            if (b1.rect.left> g3.limizq ) or (b1.rect.top > g3.limarr ) or (b1.rect.right < g3.limder ) or (b1.rect.bottom < g3.limaba ):
                g3.vida -= 50
        ls_colm=pygame.sprite.spritecollide(g4, balas, True)
        if len (ls_colm)>0:
            if (b1.rect.left> g4.limizq ) or (b1.rect.top > g4.limarr ) or (b1.rect.right < g4.limder ) or (b1.rect.bottom < g4.limaba ):
                g4.vida -= 50


        

class TanqueEnemigo(pygame.sprite.Sprite):

    def __init__(self, col, fil, m_tanq, pos=[100,500]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.mtanq=m_tanq
        self.limite=[4,4,4,4]
        self.col=col
        self.fil=fil
        self.image = self.mtanq[self.fil][self.col] 
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.disparar=False
        self.temp=random.randrange(30,60)
        self.limizq=self.rect.left 
        self.limder=self.rect.right 
        self.limarr=self.rect.top 
        self.limaba=self.rect.bottom 

    def update(self):

        
        if self.velx != self.vely:
            self.image = self.mtanq[self.fil][self.col]
        if self.col <3:
            self.col+=1
        else:
            self.col=0

        if self.temp ==0:
            pos=[self.rect.x + 20 , self.rect.bottom] * 1

            if fil == 0:
                br=BalasRival(pos, ROJO)
                br.vely -=5
                balasrivales.add(br)
                self.temp=random.randrange(20,40)                

            if fil == 1:
                br=BalasRival(pos, ROJO)
                br.velx=5
                balasrivales.add(br)
                self.temp=random.randrange(20,40)

            if fil == 2:
                br=BalasRival(pos, ROJO)
                br.velx -=5
                balasrivales.add(br)
                self.temp=random.randrange(20,40)

            if fil == 3:
                br=BalasRival(pos, ROJO)
                br.vely =5
                balasrivales.add(br)
                self.temp=random.randrange(20,40)
    
        if self.temp>0:
            self.temp-=1

        ls_colm=pygame.sprite.spritecollide(r, balas, True) 
        if len (ls_colm)>0:
            if (b1.rect.left + 40 > r.limizq ) or (b1.rect.top + 40 > r.limarr ) or (b1.rect.right -40 < r.limder ) or (b1.rect.bottom - 40 < r.limaba ):
                TanquesEnemigos.remove(r)
                j1.puntaje+=40       
        
        self.rect.x += self.velx
        self.rect.y += self.vely

class BalasRival (pygame.sprite.Sprite):
    def __init__(self, pos, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,20])
        self.image.fill(cl)     
        self.m2=m2
        self.limite=[3,3,3,3]
        self.col=0
        self.fil=0
        self.image = self.m2[self.fil][self.col]
        self.rect = self.image.get_rect()
        #self.balas=pygame.mixer.Sound('shot.ogg')
        self.rect.x=pos[0]
        self.rect.y=pos[1]       
        self.velx=0
        self.vely=0
        

    def update(self):

        if self.velx != self.vely:
            self.image = self.m2[self.fil][self.col]
        if self.col <0:
            self.col
        else:
            self.col
        self.rect.x += self.velx
        self.rect.y += self.vely


class Fenomeno(pygame.sprite.Sprite):

    def __init__(self, col, fil, mfen, pos=[400,300]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.mfen=mfen
        self.limite=[4,4,4,4]
        self.col=col
        self.fil=fil
        self.image = self.mfen[self.fil][self.col] 
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.vida = 500
        self.disparar=True
        self.temp=random.randrange(10,100)
        self.limizq=self.rect.left 
        self.limder=self.rect.right 
        self.limarr=self.rect.top 
        self.limaba=self.rect.bottom

    def update(self):

        
        if self.velx != self.vely:
            self.image = self.mfen[self.fil][self.col]
        if self.col <3:
            self.col+=1
        else:
            self.col=0

        self.rect.x += self.velx
        self.rect.y += self.vely

        

if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    Fuente=pygame.font.Font(None,32)
    Fuente1 = pygame.font.Font('fuente1.ttf', 25)
    inicio = pygame.image.load('inicio.png')
    g1pos = [556,900] # abajo
    g2pos = [-724,260] # izq
    g3pos = [2090,228] # der
    g4pos = [492,-540] # arriba
    

    bloques=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    vidas=pygame.sprite.Group()
    extras=pygame.sprite.Group()
    monedas=pygame.sprite.Group()
    generadores=pygame.sprite.Group()
    generadores2=pygame.sprite.Group()
    TanquesEnemigos=pygame.sprite.Group()
    balasrivales=pygame.sprite.Group()
    fenomenos=pygame.sprite.Group()

    



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
   
    cor=pygame.image.load('corazones.png')
    info_cor=cor.get_rect()

    ancho_cor=info_bala[2]
    alto_cor=info_bala[3]

    filasCor=[]
    sp_anchoCor= 7
    sp_altoCor= 1
    desp_xCor= 50
    desp_yCor= 56
    mcor=[]
    
    for i in range (sp_altoCor): 
        filasCor=[]
        for j in range(sp_anchoCor): 
            cuadroCor = cor.subsurface(desp_xCor*j ,desp_yCor*i,50,56)
            filasCor.append(cuadroCor)
        mcor.append(filasCor)

    v=Vida()
    vidas.add(v)

    estr=pygame.image.load('estrellasmovimiento.png')
    info_estr=estr.get_rect()

    ancho_estr=info_estr[2]
    alto_estr=info_estr[3]

    filasEst=[]
    sp_anchoEst= 7
    sp_altoEst= 1
    desp_xEst= 50
    desp_yEst= 56
    mest=[]
    
    for i in range (sp_altoEst): 
        filasEst=[]
        for j in range(sp_anchoEst): 
            cuadroEst = estr.subsurface(desp_xEst*j ,desp_yEst*i,50,56)
            filasEst.append(cuadroEst)
        mest.append(filasEst)

    bon=Extra()
    extras.add(bon)


    mon=pygame.image.load('monedas.png')
    info_mon=mon.get_rect()

    ancho_mon=info_mon[2]
    alto_mon=info_mon[3]

    filasMon=[]
    sp_anchoMon= 7
    sp_altoMon= 1
    desp_xMon= 50
    desp_yMon= 56
    mp=[]
    
    for i in range (sp_altoMon): 
        filasMon=[]
        for j in range(sp_anchoMon): 
            cuadroMon = mon.subsurface(desp_xMon*j ,desp_yMon*i,50,56)
            filasMon.append(cuadroMon)
        mp.append(filasMon)

    p=Moneda()
    monedas.add(p)

    tanq=pygame.image.load('enemigos2.png')
    info_tanq=tanq.get_rect()

    ancho_img=info_tanq[2]
    alto_img=info_tanq[3]

    filas_tanq=[]
    sp_ancho_tanq=4
    sp_alto_tanq=4
    desp_x_tanq= 80
    desp_y_tanq= 80
    m_tanq=[]
    
    for i in range (sp_alto_tanq): 
        filas_tanq=[]
        for j in range(sp_ancho_tanq): 
            cuadro_tanq = tanq.subsurface(desp_x_tanq*j ,desp_y_tanq*i,80,80)
            filas_tanq.append(cuadro_tanq)
        m_tanq.append(filas_tanq)


    fen=pygame.image.load('fenomeno.png')
    info_fen=fen.get_rect()

    ancho_img=info_fen[2]
    alto_img=info_fen[3]

    filas_fen=[]
    sp_ancho_fen=4
    sp_alto_fen=4
    desp_x_fen= 100
    desp_y_fen= 100
    mfen=[]
    
    for i in range (sp_alto_fen): 
        filas_fen=[]
        for j in range(sp_ancho_fen): 
            cuadro_fen = fen.subsurface(desp_x_fen*j ,desp_y_fen*i,100,100)
            filas_fen.append(cuadro_fen)
        mfen.append(filas_fen)

    

    cueva=pygame.image.load('portal.png')
    info_cueva=cueva.get_rect()

    ancho_img=info_cueva[2]
    alto_img=info_cueva[3]

    filas_cueva=[]
    sp_ancho_cueva=4
    sp_alto_cueva=1
    desp_x_cueva= 58
    desp_y_cueva= 120
    mcueva=[]
    
    for i in range (sp_alto_cueva): 
        filas_cueva=[]
        for j in range(sp_ancho_cueva): 
            cuadro_cueva = cueva.subsurface(desp_x_cueva*j ,desp_y_cueva*i,58,120)
            filas_cueva.append(cuadro_cueva)
        mcueva.append(filas_cueva)

    g1=Generador(0,mcueva,[550,880])
    generadores.add(g1)
    g2=Generador(0,mcueva,[-750,240])
    generadores.add(g2)


    cueva2=pygame.image.load('portal2.png')
    info_cueva2=cueva2.get_rect()

    ancho_img=info_cueva2[2]
    alto_img=info_cueva2[3]

    filas_cueva2=[]
    sp_ancho_cueva2=4
    sp_alto_cueva2=1
    desp_x_cueva2= 85
    desp_y_cueva2= 200
    mcueva2=[]
    
    for i in range (sp_alto_cueva2): 
        filas_cueva2=[]
        for j in range(sp_ancho_cueva2): 
            cuadro_cueva2 = cueva2.subsurface(desp_x_cueva2*j ,desp_y_cueva2*i,85,200)
            filas_cueva2.append(cuadro_cueva2)
        mcueva2.append(filas_cueva2)

    g3=Generador2(0,mcueva2,[2090,215])
    generadores2.add(g3)
    g4=Generador2(0,mcueva2,[470,-550])
    generadores2.add(g4)
    g1=Generador2(0,mcueva2,[2090,215])
    generadores.add(g1)
    g2=Generador2(0,mcueva2,[470,-550])
    generadores.add(g2)

       
    print ('ancho: ', info[2], 'alto: ', info[3])

    lim_movDer =1100
    lim_movIzq =100
    lim_movAba =500
    lim_movArr = 100
    f_posx= -1300
    f_velx= -4
    f_posy= -700
    f_vely= -4

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

    texto='Fin del juego'
    ubicacion_mesaje=[500,300]
    tasa=40
    con=0
    minuto=0
    segundo=0
    px = 1888
    py = 960 
    segundosGenerador= 0
    segundosGenerador2= 0
    reloj=pygame.time.Clock()
    fin=False
    fin_juego=False
    while (not fin) and (not fin_juego):
        segundosGenerador +=reloj.get_time()
        segundosGenerador2 +=reloj.get_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True  
            if event.type == pygame.KEYDOWN:
                j1.velx=0
                j1.vely=0
                if event.key == pygame.K_RIGHT:
                    j1.fil = 2
                    j1.velx = 4
                if event.key == pygame.K_LEFT:
                    j1.fil = 1
                    j1.velx = -4
                if event.key == pygame.K_UP:
                    j1.fil = 3
                    j1.vely = -4
                if event.key == pygame.K_DOWN:
                    j1.fil = 0
                    j1.vely = 4
                if event.key == pygame.K_d:
                    if  (j1.fil == 2) :
                        pos=[j1.rect.x + 30 , j1.rect.y + 5]
                        
                        
                        b1=Bala(pos)
                        balas.add(b1)
                        b1.fil = 2
                        b1.col = 0 
                        b1.velx += 10
                        b1.balas.play()
                        

                    if (j1.fil == 0) :
                        pos=[j1.rect.x - 8 , j1.rect.y + 10]
                        
                        
                        b1=Bala(pos)
                        balas.add(b1)
                        b1.fil = 2
                        b1.col = 2
                        b1.vely += 10
                        b1.balas.play()

                    if (j1.fil == 1) :
                        pos=[j1.rect.x + 10 , j1.rect.y + 5]
                        
                        
                        b1=Bala(pos)

                        balas.add(b1)
                        b1.fil = 2
                        b1.col = 3
                        b1.velx -= 10
                        b1.balas.play()

                    if  (j1.fil == 3) :
                        pos=[j1.rect.x + 7 , j1.rect.y - 20]
                        
                        
                        b1=Bala(pos)
                        balas.add(b1)
                        b1.fil = 2
                        b1.col = 1
                        b1.vely -= 10
                        b1.balas.play()

            #Condicion para disparo de tigre azul
                if j1.puntos >= 100:
                    if event.key == pygame.K_a:

                        if  (j1.fil == 2):
                            pos=[j1.rect.x + 30 , j1.rect.y + 5]
                            
                            
                            b1=Bala(pos)
                            balas.add(b1) 
                            b1.fil=1
                            b1.col = 0
                            b1.velx += 10 
                            

                        if (j1.fil == 0):
                            pos=[j1.rect.x - 8 , j1.rect.y + 10]
                            
                            
                            b1=Bala(pos)
                            balas.add(b1)
                            b1.fil=1
                            b1.col = 2
                            b1.vely += 10

                        if (j1.fil == 1):
                            pos=[j1.rect.x - 20 , j1.rect.y + 10]
                            
                            
                            b1=Bala(pos)
                            balas.add(b1)
                            b1.fil=1
                            b1.col = 3
                            b1.velx -= 10

                        if  (j1.fil == 3):
                            pos=[j1.rect.x + 7 , j1.rect.y - 20]
                            
                            
                            b1=Bala(pos)
                            balas.add(b1)
                            b1.fil=1
                            b1.col = 1
                            b1.vely -= 10

                #Condicion de disparo bola amarilla grande}
                if j1.puntaje >= 500:
                    if event.key == pygame.K_s:
                        if  (j1.fil == 2) :
                            pos=[j1.rect.x + 30 , j1.rect.y + 5]
                            
                            
                            b1=Bala(pos)
                            balas.add(b1)
                            b1.fil = 3
                            b1.col = 0 
                            b1.velx += 10 
                            

                        if (j1.fil == 0) :
                            pos=[j1.rect.x - 8 , j1.rect.y + 10]
                            
                            
                            b1=Bala(pos)
                            balas.add(b1)
                            b1.fil = 3
                            b1.col = 2
                            b1.vely += 10

                        if (j1.fil == 1) :
                            pos=[j1.rect.x - 20 , j1.rect.y + 5]
                            
                            
                            b1=Bala(pos)

                            balas.add(b1)
                            b1.fil = 3
                            b1.col = 3
                            b1.velx -= 10

                        if  (j1.fil == 3) :
                            pos=[j1.rect.x + 3 , j1.rect.y - 20]
                            
                            
                            b1=Bala(pos)
                            balas.add(b1)
                            b1.fil = 3
                            b1.col = 1
                            b1.vely -= 10
            if event.type == pygame.KEYUP:
                j1.velx=0
                j1.vely=0

        direcciones=[ 'Izquierda','Abajo']


        for g in generadores:
            if segundosGenerador >= 5000:
                segundosGenerador = 0
                velx=0
                vely=0
                direccion=random.choice(direcciones)
                gpos = 0
                img=0

                if direccion == 'Izquierda' and Portal1:
                    col = 0
                    fil = 2
                    velx = -2
                    gpos = g3pos
                    img=m_tanq
                    r=TanqueEnemigo(col, fil, img,gpos)
                    r.velx=velx
                    r.vely=vely
                    TanquesEnemigos.add(r)

                if direccion == 'Abajo' and Portal2:
                    col = 0
                    fil = 3
                    vely = 2
                    gpos = g4pos
                    img=m_tanq
                    r=TanqueEnemigo(col, fil, img,gpos)
                    r.velx=velx
                    r.vely=vely
                    TanquesEnemigos.add(r)
                    

        direcciones=['Derecha',  'Arriba' ]

        for f in generadores2:
            if segundosGenerador2 >= 10000 :
                segundosGenerador2 = 0
                velx=0
                vely=0
                direccion=random.choice(direcciones)
                gpos = 0
                img=0
                if direccion == 'Derecha':
                    col = 0
                    fil = 3
                    velx = 2
                    gpos = g2pos
                    img=mfen
                if direccion == 'Arriba':
                    col = 0
                    fil = 1
                    vely = -2
                    gpos = g1pos
                    img=mfen

    
                f=Fenomeno(col, fil, img,gpos)
                f.velx=velx
                f.vely=vely
                fenomenos.add(f)


                ls_colm=pygame.sprite.spritecollide(j1, vidas, True) 
                if len (ls_colm)>0:
                    if (j1.rect.left > v.limizq) or (j1.rect.top > v.limarr) or (j1.rect.right < v.limder) or (j1.rect.bottom < v.limaba):
                        j1.salud+=100
                        v.vida.play()

                ls_colm=pygame.sprite.spritecollide(j1, extras, True) 
                if len (ls_colm)>0:
                    if (j1.rect.left > bon.limizq) or (j1.rect.top > bon.limarr) or (j1.rect.right < bon.limder) or (j1.rect.bottom < bon.limaba):
                        j1.puntos+=100
                        bon.estrella.play()

                ls_colm=pygame.sprite.spritecollide(j1, monedas, True) 
                if len (ls_colm)>0:
                    if (j1.rect.left > p.limizq) or (j1.rect.top > p.limarr) or (j1.rect.right < p.limder) or (j1.rect.bottom < p.limaba):
                        j1.puntaje+=100
                        p.moneda.play()

                ls_col=pygame.sprite.spritecollide(j1, balasrivales, True) 
                for br in ls_col:
                    j1.salud -= 20

                ls_colm=pygame.sprite.spritecollide(f, balas, True) 
                if len (ls_colm)>0:
                    if (b1.rect.left + 40 > f.limizq ) or (b1.rect.top + 40 > f.limarr ) or (b1.rect.right -40 < f.limder ) or (b1.rect.bottom - 40 < f.limaba ):
                        TanquesEnemigos.remove(f)
                        j1.puntaje+=40

                ls_colm=pygame.sprite.spritecollide(g3, balas, True) 
                if len (ls_colm)>0:
                    if (b1.rect.left> g3.limizq ) or (b1.rect.top > g3.limarr ) or (b1.rect.right < g3.limder ) or (b1.rect.bottom < g3.limaba ):
                        g3.vida -= 50

            
        if len(jugadores)==0:
            fin_juego=True
            texto='GAMEEEEEE OVEEEEER: TE HAS MUERTO ...'

        jugadores.update()
        balas.update()
        vidas.update()
        extras.update()
        monedas.update()
        generadores.update()
        generadores2.update()
        TanquesEnemigos.update()
        balasrivales.update()
        fenomenos.update()


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
        if j1.salud <= 0:
            jugadores.remove (j1)
        txt_info=Fuente.render(info, True , cl_salud)
        pantalla.blit(txt_info, [10,10])

        info='PUNTAJE: ' +str(j1.puntaje)
        cl_puntaje=BLANCO
        txt_info=Fuente.render(info, True , cl_puntaje)
        pantalla.blit(txt_info, [1000,10])

        info='E1: ' +str(g3.vida)
        cl_puntaje=BLANCO
        if g3.vida <= 0:
            generadores.remove(g3)
            Portal1 = False
        txt_info=Fuente.render(info, True , cl_puntaje)
        pantalla.blit(txt_info, [300,10])

        info='E2: ' +str(g4.vida)
        cl_puntaje=BLANCO
        if g4.vida <= 0:
            generadores.remove(g4)
            Portal2 = False
        txt_info=Fuente.render(info, True , cl_puntaje)
        pantalla.blit(txt_info, [420,10])

        
        
        #bloques.draw(pantalla)
        balas.draw(pantalla)
        vidas.draw(pantalla)
        jugadores.draw(pantalla)
        extras.draw(pantalla)
        monedas.draw(pantalla)
        generadores.draw(pantalla)
        generadores2.draw(pantalla)
        TanquesEnemigos.draw(pantalla)
        balasrivales.draw(pantalla)
        fenomenos.draw(pantalla)

       #Cronometro
        if (segundo == 0):
            minuto +=1
        segundo=(con//(tasa)) % 60    
               
        textotiempo=str((minuto//30)-1) + ':' + str(segundo)
        img_texto=Fuente.render(textotiempo, True,BLANCO)
        pantalla.blit(img_texto,[600,10])

        pygame.display.flip()
        reloj.tick(tasa)
        con+=1
       
        #Limites y movimiento de la pantalla
        
        #Right
        if j1.rect.right > lim_movDer:
            j1.rect.right = lim_movDer
            fondopos[0] += f_velx
            g1pos[0] += f_velx
            g2pos[0] += f_velx
            g3pos[0] += f_velx
            g4pos[0] += f_velx
            if f_posx > lim_ventana:
                f_posx +=f_velx
                
                for b in bloques:
                    b.rect.x += f_velx
                    
                for generador in generadores:
                    generador.rect.x += f_velx

                for moneda in monedas:
                    moneda.rect.x += f_velx

                for vida in vidas:
                    vida.rect.x += f_velx

                for extra in extras:
                    extra.rect.x += f_velx

                for tanquenemigo in TanquesEnemigos:
                    tanquenemigo.rect.x += f_velx

                for bala in balas:
                    bala.rect.x += f_velx

                for balasrival in balasrivales:
                    balasrival.rect.x += f_velx
                
                for fenomeno in fenomenos:
                    fenomeno.rect.x += f_velx

        #Left
        if j1.rect.left < lim_movIzq:
            j1.rect.left = lim_movIzq
            fondopos[0] += f_velx
            g1pos[0] -= f_velx
            g2pos[0] -= f_velx
            g3pos[0] -= f_velx
            g4pos[0] -= f_velx
            if f_posx <= 0:
                f_posx -= f_velx

                for b in bloques:
                    b.rect.x -= f_velx
                
                for generador in generadores:
                    generador.rect.x -= f_velx

                for moneda in monedas:
                    moneda.rect.x -= f_velx

                for vida in vidas:
                    vida.rect.x -= f_velx

                for extra in extras:
                    extra.rect.x -= f_velx
                    
                for tanquenemigo in TanquesEnemigos:
                    tanquenemigo.rect.x -= f_velx

                for bala in balas:
                    bala.rect.x -= f_velx

                for balasrival in balasrivales:
                    balasrival.rect.x -= f_velx

                for fenomeno in fenomenos:
                    fenomeno.rect.x -= f_velx


        #Down
        if j1.rect.bottom > lim_movAba:
            j1.rect.bottom = lim_movAba
            fondopos[1] += f_vely
            if f_posy >= lim_ventanaAlto:
                f_posy += f_vely
                g1pos[1] += f_vely
                g2pos[1] += f_vely
                g3pos[1] += f_vely
                g4pos[1] += f_vely
                for b in bloques:
                    b.rect.y += f_vely

                for generador in generadores:
                    generador.rect.y += f_vely

                for moneda in monedas:
                    moneda.rect.y += f_vely

                for vida in vidas:
                    vida.rect.y += f_vely

                for extra in extras:
                    extra.rect.y += f_vely

                for tanquenemigo in TanquesEnemigos:
                    tanquenemigo.rect.y += f_vely

                for bala in balas:
                    bala.rect.y += f_vely

                for balasrival in balasrivales:
                    balasrival.rect.y += f_vely
                
                for fenomeno in fenomenos:
                    fenomeno.rect.y += f_vely

        #Up
        if j1.rect.top < lim_movArr:
            j1.rect.top = lim_movArr
            fondopos[1] += f_vely
            g1pos[1] -= f_vely
            g2pos[1] -= f_vely
            g3pos[1] -= f_vely
            g4pos[1] -= f_vely
            if f_posy <= 0:
                f_posy -= f_vely

                for b in bloques:
                    b.rect.y += f_vely 

                for generador in generadores:
                    generador.rect.y -= f_vely

                for moneda in monedas:
                    moneda.rect.y -= f_vely

                for vida in vidas:
                    vida.rect.y -= f_vely

                for extra in extras:
                    extra.rect.y -= f_vely
                    
                for tanquenemigo in TanquesEnemigos:
                    tanquenemigo.rect.y -= f_vely

                for bala in balas:
                    bala.rect.y -= f_vely

                for balasrival in balasrivales:
                    balasrival.rect.y -= f_vely
 
                for fenomeno in fenomenos:
                    fenomeno.rect.y -= f_vely

    Fuente=pygame.font.Font(None,32)

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        pantalla.fill(NEGRO)
        img_texto=Fuente.render(texto, True, BLANCO)
        pantalla.blit(img_texto,[400,400])
        pygame.display.flip()
                    

    pygame.quit()




            
