# ------------------- transformando a string em tokens ------------------------------
operadores = ['-', '^', '+', '-->', '<-->']

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
            return f'bad token: {proposicao[i]} at index {i}'

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
    #provavelmente vai ser bem redundante
    if tokens[0]==')' or (tokens[0] in operadores and tokens[0]!='-'):
        return False
    if tokens[-1]=='(' or tokens[-1] in operadores: #posso fazer isso de outras formas tbm
        return False
    for i in range(len(tokens)):
        if tokens[i]=='(' and i>len(tokens)-1:
            if tokens[i+1] in operadores or tokens[i+1]==')':
                return False
            else:
                pass
        elif tokens[i]==')':
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

print(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q'))))
print(extrair_variaveis(posfixar(tokenizar('-chove ^ tenho vontade de sair --> vou sair'))))
print(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q'))))

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


def quadro_combinacoes(combinacoes):
    for c in combinacoes:
        print(c)

#--------------- resolução da expressão com os valores dados nas combinações ------------------
def resolver_linha(posfixas) -> bool:
    result = 0
    return result


def resolver(posfixas):
    pass
    #- p ^ q >>>>  p - q ^ >>> not p and q
    #-(p ^ q) >>>  p q ^ - >>> not (p and q)
    #acho q isso é mais difícil de fazer, n sei agora ahhhhh

    #p - q ^
    '''
    for c in combinacoes:
        for i in range(posfixas)
            if i in variaveis:
                i = gerar_combinacoes[i]
            elif i in operadores:
    '''

def classificar():
    pass

def tabela():
    pass