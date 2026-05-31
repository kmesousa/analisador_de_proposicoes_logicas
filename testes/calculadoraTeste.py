#titulo
print(f' calculadora '.upper().center(60,'='))

operadores_aceitos = ['+', '-', '*', '/', '**']
aux = ['(', ')']

dic_precedencia = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '**': 3
}

print(f'operadores aceitos: {operadores_aceitos}')

#entrada da expressão a ser resolvida
def entrada():
    expressao = input('>> ')

#removendo espaços da expressão
def preparar_expr(expressao):
    expressao = expressao.split()
    expressao = ''.join(expressao)

def panic():
    pass
    #parar caso encontre um erro

#TOKENIZADOR / LEXER

#lexer
def tokenizar(expressao):
    tokens = []
    pilha = []
    # operadores_aceitos = ['+', '-', '*', '/', '**']
    # aux = ['(', ')']

    i = 0
    #pilha.append(expressao[0])
    while i < len(expressao):

        if expressao[i].isdigit():
            while i<len(expressao) and expressao[i].isdigit():
                pilha.append(expressao[i])
                # print('2',pilha, i, expressao[i])
                if i <= len(expressao)-1:
                    i += 1
            i -=1
        # print('2',pilha, i, expressao[i])
        # #checar por simbolos compostos: ** ou // ou sla
        elif expressao[i]=='*':
            if expressao[i+1]=='*': #lookahead
                pilha.append(expressao[i:i+2])
                i +=1
            else:
                pilha.append(expressao[i])

        else:
            pilha.append(expressao[i])

        #print('3',pilha, i, expressao[i])

        tokens.append(''.join(pilha))
        pilha=[]
        i += 1

    return tokens

print(tokenizar('90**90+2/720**80'))

#PARSER

'''
operadores_aceitos = ['+', '-', '*', '/', '**']
aux = ['(', ')']

dic_precedencia = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '**': 3
}
'''
def rpn (tokens:list) -> list: #sem considerar parenteses e sem validar expressão

    rpn = []
    pilha = []

    for i in range(len(tokens)):
        if tokens[i] not in operadores_aceitos:
            rpn.append(tokens[i])
        elif tokens[i] in operadores_aceitos:
            #print(dic_precedencia[tokens[i]])
            if pilha==[]:
                pilha.append(tokens[i])
            else: #pilha!=[]
                if dic_precedencia[tokens[i]] > dic_precedencia[pilha[len(pilha)-1]]:
                    pilha.append(tokens[i])
                elif dic_precedencia[tokens[i]] <= dic_precedencia[pilha[len(pilha)-1]]: #pq tirando esse elif e deixando só o while não dá certo?
                    while pilha!=[] and dic_precedencia[tokens[i]] <= dic_precedencia[pilha[len(pilha)-1]]:
                        rpn.append(pilha.pop())
                    pilha.append(tokens[i])

        while i == len(tokens)-1 and pilha!=[]:
            rpn.append(pilha.pop())
        #print(rpn, pilha)

    return rpn

print(rpn(['90', '**', '90', '+', '2', '/', '720', '**', '80']))
print(rpn(tokenizar('90**90+2/720**80')))

'''notacao infixa
90 + 90
p ^ q

notacao posfixa
90 90 +
p q ^

90 + 90 * 2
90 90 2 * +
'''

def rpn2 (tokens:list, aux=['(',')']) -> list: #considerando parenteses e não sei se vai ter validação ou não

    rpn = []
    pilha = []

    for i in range(len(tokens)):
        if tokens[i] not in operadores_aceitos:
            rpn.append(tokens[i])
        elif tokens[i] in operadores_aceitos:
            #print(dic_precedencia[tokens[i]])
            if pilha==[]:
                pilha.append(tokens[i])
            else: #pilha!=[]
                if dic_precedencia[tokens[i]] > dic_precedencia[pilha[len(pilha)-1]]:
                    pilha.append(tokens[i])
                elif dic_precedencia[tokens[i]] <= dic_precedencia[pilha[len(pilha)-1]]: #pq tirando esse elif e deixando só o while não dá certo?
                    while pilha!=[] and dic_precedencia[tokens[i]] <= dic_precedencia[pilha[len(pilha)-1]]:
                        rpn.append(pilha.pop())
                    pilha.append(tokens[i])
        elif tokens[i]=='(':
            pilha.append(tokens[i])
        elif tokens[i]==')':
            while pilha[-1]!='(':
                rpn.append(pilha.pop())
        while i == len(tokens)-1 and pilha!=[]:
            rpn.append(pilha.pop())
        #print(rpn, pilha)

    return rpn

print(rpn2(tokenizar('(9+9)*20+20/2')))

'''
'(9+9)*20+20/2'

e se
)
)(
90 (90)
(90+)30
30(+90)
muitos casos
'''

def resolver_rpn(rpn):
    for i in rpn:
        pass
    return