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

if __name__=='__main__':
    base_dados = input('Qual a base dados?: ')
    grupos = int(input('Quantos grupos são necessários? '))

    dados_consulta = None
    while dados_consulta == None:
        dados_consulta = gerar_dados_consulta(base_dados, grupos)
    
    centroides = deepcopy(dados_consulta['centroides'])
    conjunto = deepcopy(dados_consulta['conjunto'])
    base = deepcopy(dados_consulta['base'])

    #for linha in conjunto:
    #    print(linha)

    #for linha in base:
    #    print(linha)
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
                ponto['x'] = float(input('Valor X: '))
                ponto['y'] = float(input('Valor Y: '))
                #print(f'Centróide {retornar_centroide(ponto, centroides)}')
                centroide_ponto = retornar_centroide(ponto, centroides)
                plotar_ponto(ponto, conjunto, centroides, centroide_ponto)

            elif op == 2:
                mostrar_grupos(conjunto, centroides)
            
            elif op == 0:
                break
        
            limpar_janela()
        
        else:
            limpar_janela()
            print('Digite um valor válido')