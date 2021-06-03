# versão 1.0

import random
from math import sqrt
from copy import deepcopy

def k_means(base, centroides, conjunto):

    novo_conjunto = []

    for ponto in base:
        distancia = 0
        centroide_atual = None
        for centroide in centroides:
            d1 = pow(centroide['y'] - ponto['y'], 2)
            d2 = pow(centroide['x'] - ponto['x'], 2)
            d = sqrt(d1 + d2)

            if centroides.index(centroide) == 0:
                distancia = d
                centroide_atual = centroide
            elif distancia > d:
                distancia = d
                centroide_atual = centroide

        novo_conjunto.append({'ponto': ponto, 'centroide': centroides.index(centroide_atual)})

    #for x in novo_conjunto:
    #    print(x)

    if novo_conjunto != conjunto:
        for centroide in centroides:
            x = 0
            y = 0
            qtde = 0

            for linha in novo_conjunto:
                if linha['centroide'] == centroides.index(centroide):
                    x += linha['ponto']['x']
                    y += linha['ponto']['y']
                    qtde += 1

            mediaX = x/qtde
            mediaY = y/qtde
            centroide['x'] = mediaX
            centroide['y'] = mediaY

            #print(mediaX, ' ', mediaY)
        #print(centroides)

        #print('Não é igual')    
        info = k_means(base, centroides, novo_conjunto)
        return info
    else:
        print("É igual")
        print(novo_conjunto)
        return {'centroides': centroides, 'conjunto':novo_conjunto}


if __name__ == '__main__':
    base = [
        {'x': 1.0, 'y': 1.0},
        {'x': 9.4, 'y': 6.4},
        {'x': 2.5, 'y': 2.1},
        {'x': 8.0, 'y': 7.7},
        {'x': 0.5, 'y': 2.2},
        {'x': 7.9, 'y': 8.4},
        {'x': 7.0, 'y': 7.0},
        {'x': 2.8, 'y': 0.8},
        {'x': 1.2, 'y': 3.0},
        {'x': 7.8, 'y': 6.8}
    ]
    conjunto = []
    centroides = []

    while True:
        centroides.append(random.choice(deepcopy(base)))
        centroides.append(random.choice(deepcopy(base)))
        #centroides.append({'x': 2.5, 'y': 2.1})
        #centroides.append({'x': 2.8, 'y': 0.8})

        if centroides[0] != centroides[1]:
            break
    # print(f'{centroide1} - {centroide2}')
    print(centroides)
    dados_consulta = k_means(base, centroides, conjunto)

    centroides = deepcopy(dados_consulta['centroides'])
    conjunto = deepcopy(dados_consulta['conjunto'])

    #print(centroides)
    
    #for linha in conjunto:
    #    print(linha)

    # Consulta:
