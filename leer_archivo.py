import configparser

fnt_mapa=configparser.ConfigParser()
fnt_mapa.read('mapa.map')
print(fnt_mapa.sections())
print(fnt_mapa.items('general'))
print(fnt_mapa.get('.','info'))

mapa=fnt_mapa.get('general','mapa')
print ('Mapa')
print (mapa)
filas=mapa.split('\n')

print(filas)


for col in filas[0]:
    inf=fnt_mapa.get(col,'info')
    fl=fnt_mapa.get(col,'fil')
    cl=fnt_mapa.get(col,'col')
    print(col, inf,fl,cl)
