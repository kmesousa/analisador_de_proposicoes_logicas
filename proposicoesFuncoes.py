#tokenizador
'''a diferença entre o tokenizador de expressoes matematicas e proposiçoes lógicas é que
'pao com ovo' é aceito como um token, mas '90 10 3' nao pode ser um token
além disso, o da calculadora também só deveria aceitar digitos como operandos
mas não é mt difícil fazer as alterações de um pro outro
'''

operadores = ['-', '^', '+', '-->', '<-->']
def tokenizar(proposicao:str, operadores=['-', '^', '+', '-->', '<-->'], aux=['(',')']) -> list:
    #tokenizador genérico, funciona para proposições lógicas e expressões matemáticas!
    #operadores deve ser uma lista simples dos simbolos, não um dicionário!
    tokens = []
    char_operadores = ''.join(operadores)

    i = 0
    while i < (len(proposicao)):
        pilha = []
        if proposicao[i] not in char_operadores and proposicao[i] not in aux: #construir átomos
            while i<len(proposicao) and proposicao[i] not in char_operadores and proposicao[i] not in aux:
                pilha.append(proposicao[i])
                i += 1
            i -= 1

        elif proposicao[i] in aux:
            pilha.append(proposicao[i])

        elif proposicao[i] in char_operadores: #construir operadores compostos [- v ^ == --> ==> =] sla
            #checar se i é o primeiro elemento de um dos operadores compostos, se nao, adicionar a pilha e prosseguir se sim, checar o próximo elemnto i+1, ver se ele é o segundo elemento de m dos operadores compostos, se não, adicionar apenas i na pilha, se sim, checar o próximo (apenas nos operadores que possuem 3 ou mais), se nao, adicionar i e i+1 a pilha, se sim...
            ''' coisas para se considerar
            print('>' in '[- v ^ == --> ==> = ===> ---> -->]') #true
            print('>' in ['-', 'v', '^', '==', '-->', '==>', '=', '===>', '--->', '-->']) #false
            print('>' in ''.join(['-', 'v', '^', '==', '-->', '==>', '=', '===>', '--->', '-->'])) #true
            '''
            k = 0
            posiveis = operadores[:]
            while len(posiveis)!=1:
                #print('posiveis', k, posiveis) #porra isso daqui tá tudo errado não tô entendendo (que ódio achei q tava pronto)
                if i >= len(proposicao) or proposicao[i] not in char_operadores:
                    i -= 1
                    break
                for j in posiveis[:]:
                    if k >= len(j):
                        posiveis.remove(j)
                    elif proposicao[i] != j[k]:
                        posiveis.remove(j)
            '''
            [- v ^ == --> ==> = ===> ---> -->]

            '''
            #e se tipo, ele usar simbolos q nao são operadores como se fosse? ex pao ==> banana, sendo que ==> era pra ser -->?
            #= ==> é diferente de ==> ? ou se ele usar >==? sendo que o caractere '>' faz parte dos caracteres dos operadores, mas não no começo
        else: #mulher se tu colocar p # q isso vai ser interpretado como um só token, pq # não é operador
            return f'bad token: {proposicao[i]} at index {i}'

        i += 1
        if pilha!=[' ']:
            tokens.append(''.join(pilha).strip())
        pilha = []

    return tokens

print(tokenizar('não chove ^ tenho vontade de sair --> vou sair', ['-', '^', '+', '-->', '<-->']))
print(tokenizar('-chove ^ tenho vontade de sair --> vou sair', ['-', '^', '+', '-->', '<-->']))
print(tokenizar('-(p ^ q) ^ -q'))
print(tokenizar('p ^ q'))
print(tokenizar('p <-- q')) #operador errado ops não idenficica, mas ahco q tá tudo bem né, posso resolver isso na validação
print(tokenizar('p <--> q')) #oxi esse era pra da certo mas não tá, não entendi o pq aff
print(tokenizar('p <> q'))
print(tokenizar('p ^ -%--> q'))
print(tokenizar('p 0 q'))

#______________________________________________________________________#

#validador geral, menos sobre pareamento de parenteses
#primeiro pode ser -, parenteses abrindo ou proposição
#nao pode ter um parenteses abrindo e logo apos um fechando () par vazio
#((p ^ q)) acho que isso eu vou ter que permitir, seria como se fosse, eh tecnicamente o parenteses nao tá vazio, entao deixa
#pode parenteses com só um operando? tipo p ^ (q) ? acho que sim né
#se for parenteses abrindo, o proximo nao pode ser operador, deve ser proposição ou - ou parenteses abrindo
#se for parenteses fechando, o proximo
def validar(tokens: list, operadores=['^', '+', '-->', '<-->'], negacao='-') -> bool:
    if not tokens:
        return False

    # 1. Regras de borda (início e fim da expressão)
    # Não pode começar com ')' ou operador binário
    if tokens[0] == ')' or tokens[0] in operadores:
        return False
        
    # Não pode terminar com '(', '-', ou operador binário
    if tokens[-1] == '(' or tokens[-1] in operadores or tokens[-1] == negacao:
        return False

    # 2. Varredura dos tokens para verificar a ordem
    for i in range(len(tokens) - 1):
        atual = tokens[i]
        proximo = tokens[i + 1]

        # Verifica se o token atual é do grupo que "pede operando"
        atual_pede_operando = (atual == '(' or atual in operadores or atual == negacao)

        # Verifica se o PRÓXIMO token é do grupo "operando" (proposição, '(' ou '-')
        prox_eh_operando = (
            proximo == '(' or 
            proximo == negacao or 
            (proximo not in operadores and proximo not in ['(', ')', negacao]) # é proposição
        )

        # Se o token atual pede um operando, o próximo tem que ser um operando.
        if atual_pede_operando:
            if not prox_eh_operando:
                return False
                
        # Se o token atual não pede operando (ou seja, é proposição ou ')'), 
        # o próximo tem que ser um operador binário ou ')'
        else:
            # Operador ou parêntese fechando
            prox_eh_operador = (proximo == ')' or proximo in operadores)
            if not prox_eh_operador:
                return False

    return True
#______________________________________________________________#


#rpn (com parenteses e tudo + validação do pareamento de parenteses)
dic_precedencia = {
    '-': 5,
    '^': 4,
    '/': 3,
    '-->':2,
    '<-->':1,
    # '(':0,
    # ')':0
}


def posfixar(tokens:list, operadores=['-', '^', '/', '-->', '<-->']):
    aux = ['(',')']
    rpn = []
    pilha = []
    for i in range(len(tokens)):

        if tokens[i] not in operadores and tokens[i] not in aux:
            rpn.append(tokens[i])

        elif tokens[i] in operadores:
                    if pilha==[]:
                        pilha.append(tokens[i])
                    else: #pilha!=[]
                        if pilha[-1]==')' or pilha[-1]=='(':
                            pilha.append(tokens[i])
                        elif dic_precedencia[tokens[i]] > dic_precedencia[pilha[-1]]:
                            pilha.append(tokens[i])
                        elif dic_precedencia[tokens[i]] <= dic_precedencia[pilha[-1]]:
                            while pilha!=[] and dic_precedencia[tokens[i]] <= dic_precedencia[pilha[-1]]:
                                rpn.append(pilha.pop())
                            pilha.append(tokens[i])

        elif tokens[i]=='(':
            pilha.append(tokens[i])

        elif tokens[i]==')':
            while pilha[-1]!='(':
                rpn.append(pilha.pop())
            if pilha[-1]=='(':
                pilha.pop()

        while i == len(tokens)-1 and pilha!=[]:
            rpn.append(pilha.pop())

    return rpn

print(posfixar(tokenizar('- p ^ q --> q')))
print(posfixar(tokenizar('- (p ^ q) --> q')))
'''
4 + (40 + 50 * 20)
4 40 50 20 * + +
+ ( + *)

4 +(40*50 + 20)
4 40 50 * 20 + +
+ ( + )
'''
#resoluçaõ (ainda não sei bem como)



