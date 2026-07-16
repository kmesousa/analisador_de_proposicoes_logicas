#DICIONARIOS DOS OPERADORES

dic_simbolos = {
    'não': '-',
    'e': '^',
    'ou': '/',
    'se, então': '-->',
    'se, e somente se': '<-->',
}

dic_id = {simbolo: nome for nome, simbolo in dic_simbolos.items()}

# dic_id = {
#     dic_simbolos['não']: 'não',
#     dic_simbolos['e']: 'e',
#     dic_simbolos['ou']: 'ou',
#     dic_simbolos['se, então']: 'se, então',
#     dic_simbolos['se, e somente se']: 'se, e somente se'
# }

operadores = list(dic_simbolos.values())

dic_precedencia = {
    'não': 5,
    'e': 4,
    'ou': 3,
    'se, então':2,
    'se, e somente se':1
}

dic_aridade = {
    'não': 1,
    'e': 2,
    'ou': 2,
    'se, então':2,
    'se, e somente se':2
}

dic_funcoes = {
    'não': lambda rhs : not rhs,
    'e': lambda lhs, rhs: lhs and rhs,
    'ou': lambda lhs, rhs: lhs or rhs,
    'se, então': lambda lhs, rhs: lhs and rhs or not lhs,
    'se, e somente se': lambda lhs, rhs: lhs and rhs or not lhs and not rhs
}

#https://claude.ai/chat/3617d369-013c-471a-ac78-c977f145301f
'''ai q preguiça da porra parece que eu vou ter q reestruturar tudo dnv aa'''

def mudar_simbolos():
    from interface import TAMANHO, sep
    novos_simbolos = {}
    trocou = False

    print("digite o novo símbolo para cada operador \n(ENTER para manter o atual).")
    sep()
    for nome, simbolo_atual in dic_simbolos.items():
        novo = input(f"{nome} [{simbolo_atual}]: ").strip()
        if novo!='':
            trocou = True
        novos_simbolos[nome] = novo if novo else simbolo_atual
    sep()

    if trocou:
        if len(set(novos_simbolos.values())) != len(novos_simbolos):
            print("\nErro: dois operadores não podem usar o mesmo símbolo. \nNada foi alterado.")
            sep()
            return

        dic_simbolos.clear()
        dic_simbolos.update(novos_simbolos)

        dic_id.clear()
        dic_id.update({simbolo: nome for nome, simbolo in dic_simbolos.items()})

        operadores.clear()
        operadores.extend(dic_simbolos.values())

        print("símbolos atualizados com sucesso!")
        sep()
        return
    print("nada foi alterado.")
    sep()
    #print(dic_simbolos)