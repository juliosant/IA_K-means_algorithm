# import random
from math import sqrt
from copy import deepcopy

def retornar_centroide(ponto, centroides, colX, colY):
    # 2 - **** Calcular a distância geométrica do ponto p/ Centróide****
    distancia = 0
    centroide_atual = None
    for centroide in centroides:
        d1 = pow(centroide[colY] - ponto[colY], 2)
        d2 = pow(centroide[colX] - ponto[colX], 2)
        d = sqrt(d1 + d2)

        if centroides.index(centroide) == 0:
            distancia = d
            centroide_atual = deepcopy(centroide)
        elif distancia > d:
            distancia = d
            centroide_atual = deepcopy(centroide)
    return centroides.index(centroide_atual)

def k_means(base, centroides, conjunto, colX, colY):

    novo_conjunto = []

    for ponto in base:
        # 3 - **** Associa a cada ponto o centróide mais próximo
        centroide = retornar_centroide(ponto, centroides, colX, colY)
        novo_conjunto.append({'ponto': ponto, 'centroide': centroide})

    #for x in novo_conjunto:
    #    print(x)
    # input()
    
    # Mudança no conjunto? 
    # 5 - **** Houve mudanças no conjunto **** 
    if novo_conjunto != conjunto:
        for centroide in centroides:
            x = 0
            y = 0
            qtde = 0

            for linha in novo_conjunto:
                if linha['centroide'] == centroides.index(centroide):
                    x += linha['ponto'][colX]
                    y += linha['ponto'][colY]
                    qtde += 1
            # novo
            if qtde == 0:
                return None

            mediaX = x/qtde
            mediaY = y/qtde
            centroide[colX] = mediaX
            centroide[colY] = mediaY
            
        #print(centroides)
        #input()

        #print('Não é igual')    
        info = k_means(base, centroides, novo_conjunto, colX, colY)
        return info
    # 4 - **** Não houve mudanças no conjunto **** 
    else:
        #print("É igual")
        return {'centroides': centroides, 'conjunto':novo_conjunto}
