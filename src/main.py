# versão 1.0
from initial import gerar_dados_consulta
from app import consultar
from copy import deepcopy

if __name__=='__main__':
    base_dados = input('Qual a base dados?: ')

    dados_consulta = gerar_dados_consulta(base_dados)
    
    centroides = deepcopy(dados_consulta['centroides'])
    conjunto = deepcopy(dados_consulta['conjunto'])
    base = deepcopy(dados_consulta['base'])

    for linha in conjunto:
        print(linha)
    
    ponto = {}
    ponto['x'] = float(input('Valor X: '))
    ponto['y'] = float(input('Valor Y: '))

    print(consultar(ponto, centroides))


