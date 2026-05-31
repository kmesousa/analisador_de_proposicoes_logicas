#DICIONARIOS OPERADORES

dic_simbolos ={
    'não': '-',
    'e': '^',
    'ou': '/',
    'se, então': '->',
    'se, e somente se': '<-->'
}
print(dic_simbolos['não'])
print(list(dic_simbolos.values()))

#como fazer pra se atualizar com os simbolos tbm?
dic_funcoes = {
    dic_simbolos['não']: lambda rhs : not rhs,
    dic_simbolos['e']: lambda lhs, rhs: lhs and rhs
}

# nao = lambda rhs : not rhs
# e = lambda lhs, rhs: lhs and rhs

dic_precedencia = {
    dic_simbolos['não']: 5,
    dic_simbolos['e']: 4,
    dic_simbolos['ou']: 3,
    dic_simbolos['se, então']:2,
    dic_simbolos['se, e somente se']:1
}

dic_aridade = {
    dic_simbolos['não']: 1,
    dic_simbolos['e']: 2,
    dic_simbolos['ou']: 2
}

for i in dic_simbolos:
    print(f'{i}: {dic_simbolos[i]}')

operadores = list(dic_simbolos.values())
print(operadores)

def refazer_dic_simbolos(dic):
    for i in dic:
        v = input(f'{i}:')
        i = v
    print(dic)
    return dic

new = refazer_dic_simbolos(dic_simbolos)

print(new)
'''
p#q
p<>q
p^q
p&q
p/q
'''