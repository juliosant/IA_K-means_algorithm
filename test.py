
'''
from copy import deepcopy
import random
from matplotlib import pyplot as plt
import random


r = random.random()
g = random.random()
b = random.random()
color = (r,g,b)

fig = plt.figure()
ax1 = fig.add_subplot(111)

x = [1,2,3,4]
y = [4,1,3,6]

ax1.scatter(x, y, c=color)



r = random.random()
g = random.random()
b = random.random()
color = (r,g,b)

x = [5,6,7,8]
y = [1,3,5,2]

ax1.scatter(x, y, c=color)

plt.show()

'''

'''
base = [
    {'ponto': {'x': 1.0, 'y': 1.0}, 'centroide': 1}, 
    {'ponto': {'x': 9.4, 'y': 6.4}, 'centroide': 0}, 
    {'ponto': {'x': 2.5, 'y': 2.1}, 'centroide': 1}, 
    {'ponto': {'x': 8.0, 'y': 7.7}, 'centroide': 0}, 
    {'ponto': {'x': 0.5, 'y': 2.2}, 'centroide': 1}, 
    {'ponto': {'x': 7.9, 'y': 8.4}, 'centroide': 0}, 
    {'ponto': {'x': 7.0, 'y': 7.0}, 'centroide': 0}, 
    {'ponto': {'x': 2.8, 'y': 0.8}, 'centroide': 1}, 
    {'ponto': {'x': 1.2, 'y': 3.0}, 'centroide': 1}, 
    {'ponto': {'x': 7.8, 'y': 6.8}, 'centroide': 0}
]
x = []
y = []
centroide = []

for linha in base:
    x.append(deepcopy(linha['ponto']['x']))
    y.append(deepcopy(linha['ponto']['y']))
    centroide.append(deepcopy(linha['centroide']))
dados  = {}

dados['x'] = x
dados['y'] = y
dados['centroide'] = centroide

plt.plot(x, y, 'o')
plt.show()

lista = ['gato', 'cachorro', 'macaco', 'cachorro']
#conjunto = set(lista)
centroides = [{'x':0, 'y':7}, {'x':0, 'y':5}, {'x':0, 'y':2}, {'x':4, 'y':4}]
print(centroides.count({'x': 0, 'y': 5}))


from random import uniform

lista = [1,2,3,4,5,6,7,8,3]
print(min(lista))
print(max(lista))
print(round(uniform(min(lista), max(lista)),2))

op = 10
if op in [1,2,3]:
    print(1)
else:
    print(0)


lista0 = [{'x':5, 'y':3}, {'x':9, 'y':6}, {'x':5, 'y': 7}]
lista1 = [{'x':9, 'y':6}, {'x':5, 'y': 7}, {'x':5, 'y':3}]

contador = 0
for linha0 in lista0:
    for linha1 in lista1:
        if linha0 == linha1:
            contador +=1

if contador == len(lista0):
    print("Igual")
else: 
    print("Diferente")



def comparar(val0, val1):
    if val0 == val1:
        return True
    else:
        return False

val0 = None
val1 = 2

print(comparar(val0, val1))

base = [{'ana': 0, 'raquel':5}]
a = base[0].keys()
x, y = a
print(x, " ", y)
'''

lista = [1,3,4,5,6,7]
contador = 0

'''
if contador:
    print('a')
else:
    print('b')
'''


while True:
    for i in lista:
        print(i)
        break
    break