#configurações
WIDHT = 50
sep = lambda: print('-'*WIDHT)

# --------------- limpar tela -------------------------------------------
import os

def clean():
  if os.name == 'nt':
    _ = os.system('cls')

#---------------- menu principal -----------------------------------------
def exibir_menu_inicial():
    #--------------- cabeçário ----------------------------------
    print(' GERADOR E CLASSIFICADOR DE TABELAS VERDADE '.center(WIDHT, '='))
    print('Lógica Proposicional'.center(WIDHT))
    print('Use os símbolos abaixo para montar expressões.'.center(WIDHT))
    sep()

    #------------------ símbolos --------------------------------
    from dicsOperadores import dic_simbolos
    print('simbolos'.center(WIDHT))
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

def pedir_proposição ():
    print('digite a fórmula proposicional OU digite: ')
    print('[sair] para sair')
    sep()
    return input(">>>>>> ")

def mostrar_erro ():
    print('invalido')

def perguntar_continuar ():
    pass

def exibir_menu_final():
    sep = lambda: print('='*WIDHT)
    sep()
    print('FIM DO PROGRAMA'.center(WIDHT))
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

