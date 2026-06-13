# --------------- limpar tela -------------------------------------------
import os

#---------------- funcoes e dicionários ----------------------------------
from dicsOperadores import dic_simbolos
from funcoes import tokenizar, validar, posfixar, extrair_variaveis, gerar_combinacoes, resolver, tabela

#---------------- menu principal -----------------------------------------

continuar = True
valido = False
msg = False
tam = 50
sep = lambda: print('-'*tam)

while continuar:
    while not valido:
        print(f' gerador de tabelas verdade '.upper().center(tam, '='))
        print(f'informações que eu nem sei se vou colocar ou não')
        sep()

        print('simbolos'.center(tam))
        sep()

        #imprimindo os simbolos dividos em duas colunas, uma ao lado da outra
        chaves = list(dic_simbolos.keys())
        par = len(chaves)//2 + 1
        i = 0
        while i < len(chaves)//2+1:
            if i + par < len(chaves):
                primeiro = f'[{dic_simbolos[chaves[i]]}] {chaves[i]}'
                segundo = f'[{dic_simbolos[chaves[i+par]]}] {chaves[i+par]}'
                print(primeiro, ' '*(10-len(primeiro)), segundo )
            else:
                print(f'[{dic_simbolos[chaves[i]]}] {chaves[i]}')
            i +=1

        sep()

        print('digite a proposição OU digite: ')
        print('[sair] para sair')
        sep()

        if not valido and msg:
            print(f'inválido: {erro}')

        proposicao = input('>>>>>>> ')

        if proposicao=='sair':
            continuar = False
            valido = True
            break

        #--------------------- validar ---------------------------------------------
        #se não passar na validação, deve repetir até passar (ou [sair]) e mostrar a msg de erro
        tokens = tokenizar(proposicao)
        if tokens[0]==False:
            valido = False
            msg = True
            erro = tokens[1]
            break

        if validar(tokens)[0]==False:
            valido = False
            msg = True
            erro = validar(tokens)[1]
            break 

        valido = True

    #-------------------------  resolver e tabela -------------------------------------------
    sep()

    posfixos = posfixar(tokens)

    print(posfixos)
    
    print('continuar? (digite [sair] para sair)')
    sair = input('>>>>> ')
    if sair=='sair':
        continuar = False
