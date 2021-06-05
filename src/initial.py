
from app import k_means
from copy import deepcopy
from matplotlib import pyplot as plt
from platform import system
import random
import csv

def retornar_caminho(base):
    sistema = system()
    if sistema == "Linux":
        return f'base_dados/{base}'
    elif sistema == "Windows":
        return f'..\\base_dados\\{base}'


def gerar_dados_consulta(base,grupos):
    with open(retornar_caminho(base), 'r') as arquivo_csv:
        dicionario_csv = csv.DictReader(arquivo_csv)
        base = []
        
        for linha in dicionario_csv:
            base.append(linha)
        
        for linha in base:
            linha['x'] = float(linha['x'])
            linha['y'] = float(linha['y'])
        
        #for linha in base:
        #    print(linha)

        conjunto = []
        centroides = []

        #centroides.append({'x': 2.5, 'y': 2.1})
        #centroides.append({'x': 2.8, 'y': 0.8})

        '''
        while True:
            for centroide in range(0, grupos):
                centroides.append(random.choice(deepcopy(base)))

            repete = []

            for centroide in centroides:
                repete.append(centroides.count(centroide))
            if 2 in repete:
                centroides.clear()
                pass
            else:
                break
            print(repete)
            #centroides.append(random.choice(deepcopy(base)))
        '''
        x = []
        y = []
        for linha in base:
            x.append(deepcopy(linha['x']))
            y.append(deepcopy(linha['y']))

        while True:
            for centroide in range(0, grupos):
                posX = round(random.uniform(min(x), max(x)), 5)
                posY = round(random.uniform(min(y), max(y)), 5)
                centroides.append({'x': posX, 'y': posY})

            repete = []
            for centroide in centroides:
                repete.append(centroides.count(centroide))
            if 2 in repete:
                centroides.clear()
                pass
            else:
                break

        dados_consulta = k_means(base, centroides, conjunto)

        if dados_consulta == None:
            return None
        
        dados_consulta['base'] = deepcopy(base)
        
        return dados_consulta

# Gráfico
def mostrar_grupos(conjunto, centroides):

    for centroide in centroides:
        x = []
        y = []
        print(f'Centroide {centroides.index(centroide)}')
        for linha in conjunto:
            if centroides.index(centroide) == linha['centroide']:
                print(linha)

    grafico = plt.figure()
    ax = grafico.add_subplot(111)

    for centroide in centroides:
        x = []
        y = []
        r = random.random()
        g = random.random()
        b = random.random()
        cor = (r,g,b)      
        for linha in conjunto:
            if centroides.index(centroide) == linha['centroide']:
                x.append(deepcopy(linha['ponto']['x']))
                y.append(deepcopy(linha['ponto']['y']))
            ax.scatter(x, y, color=cor)
    plt.show()


def plotar_ponto(ponto, conjunto, centroides, centroide_ponto):
    grafico = plt.figure()
    ax = grafico.add_subplot(111)
    cor_ponto = None
    for centroide in centroides:
        x = []
        y = []
        r = random.random()
        g = random.random()
        b = random.random()
        cor = (r,g,b)

        if centroide_ponto == centroides.index(centroide):
            cor_ponto = cor

        for linha in conjunto:
            if centroides.index(centroide) == linha['centroide']:
                x.append(deepcopy(linha['ponto']['x']))
                y.append(deepcopy(linha['ponto']['y']))   
                ax.scatter(x, y, color=cor)
        
    ax.scatter(ponto['x'], ponto['y'], color=cor_ponto, s=100, edgecolors='black')
    plt.show()

