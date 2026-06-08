# ------------------- transformando a string em tokens ------------------------------
operadores = ['-', '^', '/', '-->', '<-->']

def tokenizar(proposicao:str) -> list:

    aux=['(',')']
    char_operadores = ''.join(operadores) #operadores deve ser uma lista simples, não um dicionário
    tokens = []
    i = 0

    while i < (len(proposicao)):
        pilha = []

        #construir variáveis (só podem ser formados por letras e números)
        if proposicao[i] not in char_operadores and proposicao[i] not in aux and (proposicao[i].isalnum() or proposicao[i].isspace()):
            while i<len(proposicao) and proposicao[i] not in char_operadores and proposicao[i] not in aux and (proposicao[i].isalnum() or proposicao[i].isspace()):
                pilha.append(proposicao[i])
                i += 1
            i -= 1

        #identificar parenteses
        elif proposicao[i] in aux:
            pilha.append(proposicao[i])

        #construir operadores compostos
        elif proposicao[i] in char_operadores:
            k = 0
            posiveis = operadores[:]
            while len(posiveis)!=1:
                if i >= len(proposicao) or proposicao[i] not in char_operadores:
                    i -= 1
                    break
                for j in posiveis: #tem alguns erros nessa parte, mas melhor fazer o resto primeiro
                    if k >= len(j):
                        posiveis.remove(j)
                    elif proposicao[i]!=j[k]:
                        posiveis.remove(j)
                    elif proposicao[i]==j[k]:
                        pass
                    if proposicao[i] in char_operadores:
                        pilha.append(proposicao[i])
                        i+=1
                        k+=1
        else: #identificar tokens que não são proposições, operadores nem auxiliadores
            return False, f'bad token: {proposicao[i]} at index {i}'

        i += 1
        if pilha!=[' ']:
            tokens.append(''.join(pilha).strip())
        pilha = []
    return tokens

# ------------------- validando os tokens ------------------------------
'''validador geral, menos sobre pareamento de parenteses eu acho
primeiro pode ser -, parenteses abrindo ou proposição
nao pode ter um parenteses abrindo e logo apos um fechando () par vazio
((p ^ q)) acho que isso eu vou ter que permitir, seria como se fosse, eh tecnicamente o parenteses nao tá vazio, entao deixa
pode parenteses com só um operando? tipo p ^ (q) ? acho que sim né
se for parenteses abrindo, o proximo nao pode ser operador, deve ser proposição ou - ou parenteses abrindo
se for parenteses fechando, o proximo'''
def validar(tokens:list, operadores=['-', '^', '+', '-->', '<-->']) -> bool:

    aux=['(',')']
    char_operadores = ''.join(operadores)

    for i in range(len(tokens)):
        if tokens[i][0] in char_operadores and tokens[i] not in operadores:
            return False
        if tokens[i] not in operadores:
            pass
        elif tokens[i] in operadores:
            pass
        elif tokens[i] in aux:
            pass

# ------------------- transformando tokens válidos em notação pos-fixa --------------------
dic_precedencia = {
    '-': 5,
    '^': 4,
    '/': 3,
    '-->':2,
    '<-->':1,
}

def posfixar(tokens:list) -> list:
    aux = ['(',')']
    npf = []
    pilha = []
    for i in range(len(tokens)):

        if tokens[i] not in operadores and tokens[i] not in aux:
            npf.append(tokens[i])

        elif tokens[i] in operadores:
                    if pilha==[]:
                        pilha.append(tokens[i])
                    else: #pilha!=[]
                        if pilha[-1]=='(': #nunca vai ser )
                            pilha.append(tokens[i])
                        elif dic_precedencia[tokens[i]] > dic_precedencia[pilha[-1]]:
                            pilha.append(tokens[i])
                        elif dic_precedencia[tokens[i]] <= dic_precedencia[pilha[-1]]:
                            while pilha!=[] and dic_precedencia[tokens[i]] <= dic_precedencia[pilha[-1]]:
                                npf.append(pilha.pop())
                            pilha.append(tokens[i])

        elif tokens[i]=='(':
            pilha.append(tokens[i])

        elif tokens[i]==')':
            while pilha[-1]!='(':
                npf.append(pilha.pop())
            if pilha[-1]=='(':
                pilha.pop()

        while i == len(tokens)-1 and pilha!=[]:
            npf.append(pilha.pop())

    return npf


# ------------------- gerando combinações para as variáveis --------------------
def extrair_variaveis(posfixos) -> list:
    variaveis = {}
    for i in posfixos:
        if i not in operadores:
            variaveis[i] = ''
    return list(variaveis.keys())

def gerar_combinacoes(variaveis):

    #crinando a lista com dicionários vazios para cada combinação
    qte_combinacoes = 2 ** len(variaveis)
    combinacoes = [0]*qte_combinacoes
    for i in range(qte_combinacoes):
        combinacoes[i]={}

    valores = (True, False)

    #colunas por variável
    for v in range(len(variaveis)):
        blocos = 2**(v+1)
        inicio_bloco = 0
        fim_bloco = inicio_bloco + qte_combinacoes//blocos

        #blocos por valor da variável
        for i in range(blocos):
            valor = valores[i%2]

            #colocando o valor na variável
            for j in range(inicio_bloco, fim_bloco):
                combinacoes[j][variaveis[v]] = valor
            inicio_bloco = fim_bloco
            fim_bloco += qte_combinacoes//blocos
    return combinacoes
    #[{'p': True, 'q': True}, {'p': True, 'q': False}, {'p': False, 'q': True}, {'p': False, 'q': False}]

def quadro_combinacoes(combinacoes):
    for c in combinacoes:
        print(c)

#--------------- resolução da expressão com os valores dados nas combinações ------------------

dic_simbolos = {
    'não': '-',
    'e': '^',
    'ou': '/',
    'se, então': '-->',
    'se, e somente se': '<-->'
}

dic_sign = {
    dic_simbolos['não']: 'não',
    dic_simbolos['e']: 'e',
    dic_simbolos['ou']: 'ou',
    dic_simbolos['se, então']: 'se, então',
    dic_simbolos['se, e somente se']: 'se, e somente se'
}

dic_funcoes = {
    dic_simbolos['não']: lambda rhs : not rhs,
    dic_simbolos['e']: lambda lhs, rhs: lhs and rhs,
    dic_simbolos['ou']: lambda lhs, rhs: lhs or rhs,
    dic_simbolos['se, então']: lambda lhs, rhs: (lhs and rhs) or not lhs,
    dic_simbolos['se, e somente se']: lambda lhs, rhs: lhs and rhs or (not lhs and not rhs)
}

dic_aridade = {
    dic_simbolos['não']: 1,
    dic_simbolos['e']: 2,
    dic_simbolos['ou']: 2,
    dic_simbolos['se, então']:2,
    dic_simbolos['se, e somente se']:2
}

def resolver(posfixas):

    variavies = extrair_variaveis(posfixas)
    combinacoes = gerar_combinacoes(variavies)

    tautologia = True
    contradicao = True

    pilha = []
    tabela = {}

    for c in range(len(combinacoes)):
        pilha = []
        for i in range(len(posfixas)):
            if posfixas[i] in variavies:
                expressao = posfixas[i]
                valor = combinacoes[c][posfixas[i]]
            elif posfixas[i] in operadores:
                if dic_aridade[posfixas[i]]==1:
                    op = pilha.pop()
                    expressao = f'{posfixas[i]} {op[0]}'
                    valor = dic_funcoes[posfixas[i]](op[1])
                else:
                    rhs = pilha.pop()
                    lhs = pilha.pop()
                    expressao = f'{lhs[0]} {posfixas[i]} {rhs[0]}'
                    valor = dic_funcoes[posfixas[i]](lhs[1],rhs[1])
            pilha.append((expressao, valor))

            if expressao not in tabela:
                tabela[expressao] = []
            if c+1 > len(tabela[expressao]): #adicionar apenas 1 valor por combinanação a cada variável ou subexpressao
                tabela[expressao].append(valor)

        if tabela[expressao][-1]==False:
            tautologia=False
            classificacao = 'contradição'
        if tabela[expressao][-1]==True:
            contradicao=False
            classificacao = 'tautologia'
    if not (contradicao or tautologia):
        classificacao = 'contingência'

    return tabela, classificacao

print(resolver(posfixar(tokenizar('-p ^ -q'))))
print(resolver(posfixar(tokenizar('p ^ q'))))
print(resolver(posfixar(tokenizar('-p'))))
print(resolver(posfixar(tokenizar('p / -p')))) #p tem mais linhas doq devia
print(resolver(posfixar(tokenizar('p-->q'))))
print(resolver(posfixar(tokenizar('p<--> q'))))
print(resolver(posfixar(tokenizar('p ^ -p')))) #p tem mais linhas doq devia
print(resolver(posfixar(tokenizar('p ^ -p --> -p ^ -p')))) #era pra ter só duas linhas, mas tem mt mais q isso, como corrigir?
print(resolver(posfixar(tokenizar('p ^ -q --> -p ^q')))) #as linhas da tabela estão completamente erradas, aaa #pronto :)


def tabela():
    pass