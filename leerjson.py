import json

nom_archivo='fondo.json'
with open(nom_archivo) as archivo:
    datos=json.load(archivo)


print(datos['height'])
capas=datos['layers']

print (capas[0]['name'])
print (capas[1]['name'])
mapa=capas[1]['data']
limite=capas[1]['width']

con=0
ls=[]
for e in mapa:
    if e !=0:
        ls.append(e)
    else:
        ls.append('')
    con+=1
    if con >= limite:
        print(ls)
        ls=[]
        con=0
