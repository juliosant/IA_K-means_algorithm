# import random
from math import sqrt
# from copy import deepcopy

def retornar_centroide(ponto, centroides):
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
    return centroides.index(centroide_atual)

def k_means(base, centroides, conjunto):

    novo_conjunto = []

    for ponto in base:
        novo_conjunto.append({'ponto': ponto, 'centroide': retornar_centroide(ponto, centroides)})

    #for x in novo_conjunto:
    #    print(x)
    
    # Mudança no conjunto? 
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
            # novo
            if qtde == 0:
                return None

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
        #print("É igual")
        return {'centroides': centroides, 'conjunto':novo_conjunto}
