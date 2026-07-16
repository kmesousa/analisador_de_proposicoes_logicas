from dicsOperadores import dic_simbolos
import funcoes

#configurações
TAMANHO = 50
sep = lambda: print('-'*TAMANHO)

# --------------- limpar tela -------------------------------------------
import os

def limpar_tela():
  if os.name == 'nt':
    _ = os.system('cls')


def exibir_simbolos():
    print('simbolos'.center(TAMANHO))
    sep()
    #imprimindo os simbolos dividos em duas colunas, uma ao lado da outra
    chaves = list(dic_simbolos.keys())
    if len(chaves)%2==0:
        par = len(chaves)//2
        criterio = lambda i: i < len(chaves)//2
    else:
        par = len(chaves)//2+1
        criterio = lambda i: i < len(chaves)//2+1
    i = 0
    while criterio(i):
        if i + par < len(chaves):
            primeiro = f'[{dic_simbolos[chaves[i]]}] {chaves[i]}'
            segundo = f'[{dic_simbolos[chaves[i+par]]}] {chaves[i+par]}'
            print(primeiro, ' '*(10-len(primeiro)), segundo )
        else:
            print(f'[{dic_simbolos[chaves[i]]}] {chaves[i]}')
        i +=1
    sep()

def exibir_menu_inicial():
    print(' GERADOR E CLASSIFICADOR DE TABELAS VERDADE '.center(TAMANHO, '='))
    print('Lógica Proposicional'.center(TAMANHO))
    print('Use os símbolos abaixo para montar expressões.'.center(TAMANHO))
    sep()
    exibir_simbolos()

def pedir_proposição ():
    print('digite a fórmula proposicional OU digite: ')
    print('[sair] para sair')
    print('[trocar] para trocar simbolos')
    sep()
    return input(">>>>>> ")

def mostrar_erro (tokens):
    print(f'invalido: {funcoes.validar(tokens)[1]}')
    sep()

def perguntar_continuar ():
    print('continuar? (digite [sair] para sair)')
    return input('>>>>> ')

def exibir_menu_final():
    sep = lambda: print('='*TAMANHO)
    sep()
    print('FIM DO PROGRAMA'.center(TAMANHO))
    sep()

    print('\nGerador de Tabelas Verdade')
    print('Projeto desenvolvido para a disciplina de MDL.')

    print('\nDesenvolvido por:')
    print('- Kamily')
    print('- Mileena')

    print('\nObrigado por utilizar o programa.')
    print('\nREFERÊNCIA:')
    print()
    print('link: https://youtu.be/0c8b7YfsBKs?si=KK5-bVCiTEjJ_o7v')
    sep()

