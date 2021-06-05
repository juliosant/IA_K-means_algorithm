
from app import k_means
from copy import deepcopy
from matplotlib import pyplot as plt
from platform import system
import random
import csv

#class Posicoes:
#    def __init__(self, posicoes):
#        self.x, self.y = posicoes


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
        
        colX, colY = base[0].keys()

        for linha in base:
            linha[colX] = float(linha[colX])
            linha[colY] = float(linha[colY])
        
        #for linha in base:
        #    print(linha)
        # input()

        conjunto = []
        centroides = []

        # 1 - **** Escolher centróides ****
        
        # centroides.append({'x': 2.5, 'y': 2.1})
        # centroides.append({'x': 2.8, 'y': 0.8})
        
        # 1.1 - **** Escolher pontos aleatórios dentro da base de dados ****
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
        # 1.2 - **** Escolher valores aleatórios entre o maio e menor valores das colunas ****
        x = []
        y = []
        for linha in base:
            x.append(deepcopy(linha[colX]))
            y.append(deepcopy(linha[colY]))

        while True:
            # 1.2.1 - **** Gerar valores randômicos por coluna ****
            for centroide in range(0, grupos):
                posX = round(random.uniform(min(x), max(x)), 2)
                posY = round(random.uniform(min(y), max(y)), 2)
                centroides.append({colX: posX, colY: posY})

            # 1.2.2 - **** Centróides repetidos? ****
            contador = 0
            for centroide in centroides:
                contagem_atual = centroides.count(centroide)
                if contagem_atual > 1:
                    contador = contagem_atual
                    break
                elif contagem_atual > contador:
                    contador = contagem_atual
            
            if contador > 1:
                pass
            else:
                break
        
        #for linha in centroides:
        #    print(linha)
        # input()

        # **** Chamar Kmeans ****
        dados_consulta = k_means(base, centroides, conjunto, colX, colY)

        if dados_consulta == None:
            return None
        
        dados_consulta['base'] = deepcopy(base)
        
        return dados_consulta

# **** Gráficos ****
def mostrar_grupos(conjunto, centroides, colX, colY):

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
                x.append(deepcopy(linha['ponto'][colX]))
                y.append(deepcopy(linha['ponto'][colY]))
            ax.scatter(x, y, color=cor)
    plt.show()


def plotar_ponto(ponto, conjunto, centroides, centroide_ponto, colX, colY):
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
                x.append(deepcopy(linha['ponto'][colX]))
                y.append(deepcopy(linha['ponto'][colY]))   
                ax.scatter(x, y, color=cor)
        
    ax.scatter(ponto[colX], ponto[colY], color=cor_ponto, s=100, edgecolors='black')
    plt.show()

