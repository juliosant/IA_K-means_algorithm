# versão 1.0
from initial import gerar_dados_consulta, mostrar_grupos, plotar_ponto
from app import retornar_centroide
from copy import deepcopy
from platform import system
import os

def limpar_janela():
    sistema = system()
    if sistema == "Linux":
        os.system("clear")
    elif sistema == "Windows":
        os.system("cls")

def comparar_dados(ct0, ct1):
    contador = 0
    for linha0 in ct0:
        for linha1 in ct1:
            if linha0 == linha1:
                contador +=1

    if contador == len(ct0):
        return True
    else: 
        return False

if __name__=='__main__':
    base_dados = input('Qual a base dados?: ')
    grupos = int(input('Quantos grupos são necessários? '))

    dados_consulta = None
    while dados_consulta == None:
        # **** Inicio do Algoritmo ****
        dados_consulta = gerar_dados_consulta(base_dados, grupos)
        comparador = gerar_dados_consulta(base_dados, grupos)

        resultado_comparacao = False
        if dados_consulta != None and comparador != None:
            resultado_comparacao = comparar_dados(dados_consulta['centroides'] , comparador['centroides'])
        if resultado_comparacao == False:
            dados_consulta = None

    centroides = deepcopy(dados_consulta['centroides'])
    conjunto = deepcopy(dados_consulta['conjunto'])
    base = deepcopy(dados_consulta['base'])

    #for linha in conjunto:
    #    print(linha)

    #for linha in base:
    #    print(linha)
    colX, colY = centroides[0].keys()

    print(centroides)
    while True:
        print('''
            [1] Consultar novo ponto
            [2] Consultar grupos
            [0] Sair
        ''')

        op = int(input("Escolha uma opção: "))

        if op in [0,1,2]:
            if op == 1:
                ponto = {}
                ponto[colX] = float(input(f'Valor {colX}: '))
                ponto[colY] = float(input(f'Valor {colY}: '))
                #print(f'Centróide {retornar_centroide(ponto, centroides)}')
                centroide_ponto = retornar_centroide(ponto, centroides, colX, colY)
                plotar_ponto(ponto, conjunto, centroides, centroide_ponto, colX, colY)

            elif op == 2:
                mostrar_grupos(conjunto, centroides, colX, colY)
            
            elif op == 0:
                break
        
            limpar_janela()
        
        else:
            limpar_janela()
            print('Digite um valor válido')