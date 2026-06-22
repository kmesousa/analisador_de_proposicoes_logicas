# ------------------- 1 TRANSFORMANDO A LISTA EM TOKENS ------------------------------
def operadores_decrescentes(operadores): #colocar os operadores em ordem descrescente de quantidade de caracteres, para usar para descobrir os operadores na função tokenizar
    ordenados = [] #lista para receber com a ordem correta
    i = 0 #ERRO isso seria o intinerador caso fosse usar o while, mas não é o caso, linha é ignorada no programa
    maior = len(operadores[0]) #maior operador recebe o tamanho do primeiro operador
    #------ descobrir o maior operador ------------------------------------------------------------------------
    for i in range(1, len(operadores)): #itinerar pelos operadores, começando pelo segundo, para descobrir o maior
        if len(operadores[i-1])<len(operadores[i]): #verificar se o atual é maior que o anterior
            maior = len(operadores[i]) #recebe o tamanho de caracteres do maior operador ao final do for
    #---- ordenar os operadores --------------------------------------------------------------------------------
    while len(ordenados)!=len(operadores): #enquanto a lista de ordenados não conter todos os elementos da lista de operadores
        for i in range(len(operadores)): #itinerar cada operador
            if len(operadores[i])==maior: #se o operador tiver a mesma quantidade de caracteres do maior operador encontrado
                ordenados.append(operadores[i])
        maior -= 1 #diminuir o tamanho do maior para encontrar os proximos operadores menores que ele
    return ordenados

def tokenizar(proposicao:str) -> list: #recebe a formula proposicional lógica e retorna uma lista com os tokens

    from dicsOperadores import operadores #pegar a lista de operadores
    operadores = operadores_decrescentes(operadores) #colocar a lista em ordem decrescente pelo número de caracteres
    aux=['(',')']
    char_operadores = ''.join(operadores) #identificar todos caracteres presentes dos operadores
    tokens = [] #lista que receberá os tokens

    i = 0 #inicialização do while
    while i < (len(proposicao)): #percorrer os caracteres da proposição
        pilha = [] #pilha para a construção dos tokens

        # ---------------------- construir variáveis ----------------------------------------------------------------------
        if proposicao[i] not in char_operadores and proposicao[i] not in aux and (proposicao[i].isalnum() or proposicao[i].isspace()): # não pode ser formada por caracteres usados nos operadores e só pode conter letrar, números e espaços)
            while i<len(proposicao) and proposicao[i] not in char_operadores and proposicao[i] not in aux and (proposicao[i].isalnum() or proposicao[i].isspace()): #percorrer a proposição enquanto estiver em seu escopo e atender as condições de caractere para variável
                pilha.append(proposicao[i])
                i += 1 #ir para o próximo caracterere da proposição
            i -= 1 #quando encontrar um caractere que não atende aos requesitos da variável, encerra o while das variáveis e incrementa -1 para avaliar esse caractere no próximo while maior para encontrar em qual elif ele se encaixa

        #------------------------ identificar parenteses ------------------------------------------------------------------
        elif proposicao[i] in aux:
            pilha.append(proposicao[i]) #adicionados individualmente na pilha, cada parentese é um token por si só

        #---------------------- descobrir operadores compostos --------------------------------------------------------
        elif proposicao[i] in char_operadores: #caso o caractere atual seja um dos usados para formar operadores
            #procurar pelo mais longo primeiro
            for o in range(len(operadores)):
                w = i #simular os proximos caracteres para verificar se forma operadores longo
                valido = True
                for j in range(len(operadores[o])):
                    if operadores[o][j]==proposicao[w]: #verificar se os proximos caracteres condizem com os do operador
                        w+=1
                    else:
                        valido = False
                        break
                if valido:
                    pilha.extend(operadores[o])
                    i = w #atualizar com a posição do proximo caractere após o ultimo do operador
                    break
            if not valido:
                return False, f'bad token: {proposicao[i]} at index {i}'
            i -=1 #voltar para o ultimo caractere do operador

        else: #identificar tokens que não são proposições, operadores nem auxiliadores
            print(f"Proposição: {repr(proposicao)}")
            print(f"Caractere inválido: {repr(proposicao[i])}")
            print(f"Índice: {i}")
            return False, f'bad token: {proposicao[i]} at index {i}'

        i += 1
        if pilha!=[' ']: #não adicionar espaços entre tokens a lista
            tokens.append(''.join(pilha).strip()) #adicionar tokens removendo os espaços das extremidades
        pilha = []
    return tokens

# ------------------- validando os tokens ------------------------------
def parenteseses_certos(lista:list) -> bool:
    #só verifica se eles estão pareados corretamente (não diz nada a respeito do posicionamento parenteses, operandos e operadores)

    pilha1 = [] #( não pode conter elementos no final
    pilha2 =[] #) não pode conter elementos caso a pilha 2 esteja vazia a qualquer momento

    for i in range (0, len(lista)):
        #1: direcionamento
        if lista[i] == '(':
            pilha1.append(lista[i])
        elif lista[i] == ')':
            pilha2.append(lista[i])

        #2: pareamento
        while len(pilha2)!=0 and len(pilha1)!=0:
            del pilha1[0]
            del pilha2[0]

        #3: validadação
        if len(pilha2)!=0:
            return False
    if pilha1!=[]:
        return False
    return True

def validar(tokens: list) -> bool:

    from dicsOperadores import operadores, dic_simbolos

    negacao= dic_simbolos['não']

    operadores_binarios = operadores.copy()
    operadores_binarios.remove(negacao)


    #validar a paridade dos parenteses
    if not parenteseses_certos(tokens):
        return False, 'parenteses não fechados'

    if not tokens:
        return False, 'nenhum token encontrado, expressão vazia'

    # 1. Regras de borda (início e fim da expressão)
    # Não pode começar com ')' ou operador binário
    #if tokens[0] == ')' or (tokens[0] in operadores and tokens[0]!=dic_simbolos['não']):
    if tokens[0] in operadores_binarios:
        return False, 'precedência inválida'

    # Não pode terminar com '(', '-', ou operador binário
    if tokens[-1] == '(' or tokens[-1] in operadores or tokens[-1] == negacao:
        return False, 'precedência inválida'

    if tokens[-1] in operadores:
        return False, f"operador '{tokens[-1]}' sem operando"

    # 2. Varredura dos tokens para verificar a ordem
    for i in range(len(tokens) - 1):
        atual = tokens[i]
        proximo = tokens[i + 1]

        if atual not in operadores and atual != '(' and atual != ')':
            if proximo not in operadores and proximo != ')':
                return False, f"falta operador entre '{atual}' e '{proximo}'"

        # Verifica se o token atual é do grupo que "pede operando"
        atual_pede_operando = (atual == '(' or atual == negacao or atual in operadores_binarios)

        # Verifica se o PRÓXIMO token é do grupo "operando" (proposição, '(' ou '-')
        prox_eh_operando = (
            proximo == '(' or
            proximo == negacao or
            (proximo not in operadores and proximo not in ['(', ')', negacao]) # é proposição
        )

        # Se o token atual pede um operando, o próximo tem que ser um operando.
        if atual_pede_operando:
            if not prox_eh_operando:
                return False, f"esperava uma proposição após '{atual}', mas encontrou '{proximo}'"

        # Se o token atual não pede operando (ou seja, é proposição ou ')'),
        # o próximo tem que ser um operador binário ou ')'
        else:
            # Operador ou parêntese fechando
            prox_eh_operador = (proximo == ')' or proximo in operadores_binarios)
            if not prox_eh_operador:
                return False, f"esperava um operador entre '{atual}' e '{proximo}'"

    return True, 'valido'

# ------------------- transformando tokens válidos em notação pos-fixa --------------------
def posfixar(tokens:list) -> list:
    from dicsOperadores import dic_precedencia, operadores
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

                        elif dic_precedencia[tokens[i]] == dic_precedencia[pilha[-1]]:
                            pilha.append(tokens[i])

                        elif dic_precedencia[tokens[i]] < dic_precedencia[pilha[-1]]:
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
    from dicsOperadores import operadores
    variaveis = {}
    tamanho = 0
    for i in posfixos:
        if i not in operadores:
            variaveis[i] = ''
            tamanho += len(i)

    lista_variaveis = list(variaveis.keys())

    #diminuir variávies caso sejam muito longas(ex. chove vira c, teria que fazer antes do posfixar)
    return lista_variaveis

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
    return combinacoes #[{'p': True, 'q': True}, {'p': True, 'q': False}, {'p': False, 'q': True}, {'p': False, 'q': False}]

#--------------- resolução da expressão com os valores dados nas combinações ------------------

def resolver(posfixas):
    from dicsOperadores import operadores, dic_aridade, dic_funcoes


    variaveis = extrair_variaveis(posfixas)
    combinacoes = gerar_combinacoes(variaveis)

    tautologia = True
    contradicao = True

    pilha = []
    tabela = {}
    tamanho = 0

    for c in range(len(combinacoes)):
        pilha = []
        for i in range(len(posfixas)):
            if posfixas[i] in variaveis:
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
                tamanho += len(expressao)
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

    return tabela, classificacao, tamanho

# --------------------------- imprimir tabela verdade ---------------------------------------------------

def organizar_dados(dados, variaveis):
    organizados = {}
    for i in variaveis:
        organizados[i]=dados[i]
    for i in dados:
        if i not in organizados:
            organizados[i]=dados[i]
    return organizados

def tabela(posfixos, proposicao):
    variaveis = extrair_variaveis(posfixos)
    dados = organizar_dados(resolver(posfixos)[0], variaveis)

    #trocar a ultima subexpressao pela proposição original (a reconstruida não considera parenteses)
    chaves = list(dados.keys())
    dados[proposicao] = dados.pop(chaves[-1])

    tamanho = resolver(posfixos)[2]

    if tamanho > 40: #se o tamanho da linha de cabeçário for mt grande, remover subsexpressoes
        for i in range(len(dados)-1): #remover chaves que não forem variáveis ou que não forem a ultima(proposição final)
            if chaves[i] not in variaveis:
                dados.pop(chaves[i])
                tamanho -= len(chaves[i])

    if tamanho > 100: #se mesmo removendo as subexpressoes, o cabeçário ainda for mt grande
        print('proposição muito grande para formar tabela')
        return False

    largura = (tamanho+len(dados)*4)
    if largura <= 50:
        base = 50
    else:
        base = largura

    print(f' gerador de tabelas verdade '.upper().center(base, '='))
    print('-'*base)

    resultado =f'classificação: {resolver(posfixos)[1].upper()}'
    espaco_entre = base - len(resultado)-len(proposicao)
    if espaco_entre < 4:
        print(proposicao)
        print(resultado)
    else:
        print(f"{proposicao}{' '*espaco_entre}{resultado}")

    print('-'*base)

    for chave in dados:
        print(f'| {chave} |', end='')
    print('')

    for i in range(len(dados[variaveis[0]])):
        for j in dados:
            match dados[j][i]:
                case True:
                    valor = 'V'
                case False:
                    valor = 'F'
            print(f'| {valor.center(len(j))} |', end='')
        print('')
    print('-'*base)

    return base