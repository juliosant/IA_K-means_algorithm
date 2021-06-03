import random
import csv
from app import k_means
from copy import deepcopy

def gerar_dados_consulta(base):
    with open(f'base_dados/{base}', 'r') as arquivo_csv:
        dicionario_csv = csv.DictReader(arquivo_csv)
        base = []
        
        for linha in dicionario_csv:
            base.append(linha)
        
        for linha in base:
            linha['x'] = float(linha['x'])
            linha['y'] = float(linha['y'])
        
        '''base = [
            {'x': 1.0, 'y': 1.0},
            {'x': 9.4, 'y': 6.4},
            {'x': 2.5, 'y': 2.1},
            {'x': 8.0, 'y': 7.7},
            {'x': 0.5, 'y': 2.2},
            {'x': 7.9, 'y': 8.4},
            {'x': 7.0, 'y': 7.0},
            {'x': 2.8, 'y': 0.8},
            {'x': 1.2, 'y': 3.0},
            {'x': 7.8, 'y': 6.1}
        ]'''
        #for linha in base:
        #    print(linha)

        conjunto = []
        centroides = []

        while True:
            centroides.append(random.choice(deepcopy(base)))
            centroides.append(random.choice(deepcopy(base)))
            #centroides.append({'x': 2.5, 'y': 2.1})
            #centroides.append({'x': 2.8, 'y': 0.8})

            if centroides[0] != centroides[1]:
                break
        
        dados_consulta = k_means(base, centroides, conjunto)

        dados_consulta['base'] = deepcopy(base)
        
        return dados_consulta
        #centroides = deepcopy(dados_consulta['centroides'])
        #conjunto = deepcopy(dados_consulta['conjunto'])

        #print(centroides)
        #for linha in conjunto:
        #    print(linha)
