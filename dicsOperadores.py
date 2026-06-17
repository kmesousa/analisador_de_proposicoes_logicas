#DICIONARIOS DOS OPERADORES

dic_simbolos = {
    'não': '-',
    'e': '^',
    'ou': '\/',
    'se, então': '-->',
    'se, e somente se': '<-->',
    'ou exclusivo': '<>',
}

operadores = list(dic_simbolos.values())

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
    dic_simbolos['ou']: 2,
    dic_simbolos['se, então']:2,
    dic_simbolos['se, e somente se']:2
}

dic_funcoes = {
    dic_simbolos['não']: lambda rhs : not rhs,
    dic_simbolos['e']: lambda lhs, rhs: lhs and rhs,
    dic_simbolos['ou']: lambda lhs, rhs: lhs or rhs,
    dic_simbolos['se, então']: lambda lhs, rhs: lhs and rhs or not lhs,
    dic_simbolos['se, e somente se']: lambda lhs, rhs: lhs and rhs or not lhs and not rhs
}