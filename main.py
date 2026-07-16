import funcoes
import dicsOperadores
import interface

def main():
    erro = None
    opcao = None

    while True:
        interface.limpar_tela()
        interface.exibir_menu_inicial()
        if erro:
            interface.mostrar_erro(tokens)
        if not opcao:
            opcao = interface.pedir_proposição().strip().lower()

        match opcao:
            case 'sair':
                break
            case 'trocar':
                dicsOperadores.mudar_simbolos()
            case _:
                proposicao = opcao
                tokens = funcoes.tokenizar(proposicao)
                if not funcoes.validar(tokens)[0]:
                    erro = True
                    continue

                funcoes.tabela(funcoes.posfixar(tokens), proposicao)
                opcao = interface.perguntar_continuar().strip().lower()

    interface.limpar_tela()
    interface.exibir_menu_final()

if __name__ == '__main__':
    main()
