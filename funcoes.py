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
            return False, f'bad token: {proposicao[i]} at index {i}'

        i += 1
        if pilha!=[' ']: #não adicionar espaços entre tokens a lista
            tokens.append(''.join(pilha).strip()) #adicionar tokens removendo os espaços das extremidades
        pilha = []
    return tokens

# ------------------- validando os tokens ------------------------------
def validar(tokens: list) -> bool:

    from dicsOperadores import dic_aridade, dic_simbolos

    #tipos de tokens
    operando = "operando"
    operador_bi = []
    operador_uni = []

    #operadores separados por aridade
    for i in dic_simbolos:
        if dic_aridade[i]==2:
            operador_bi.append(dic_simbolos[i])
        elif dic_aridade[i]==1:
            operador_uni.append(dic_simbolos[i])
    operador_bi = tuple(operador_bi)
    operador_uni = tuple(operador_uni)

    tipos_tokens = ["(", ")", operador_uni, operador_bi, operando]

    proximos_possiveis = {
        "(": ["(", ")", operador_uni, operando],
        ")": [")", operador_bi],
        operador_uni: ["(", operador_uni, operando],
        operador_bi: ["(", operador_uni, operando],
        operando: [")", operador_bi]
    }

    counter_parentesis = 0 #verificar paridade dos parenteses

    def definir_tipo(elemento):
        for j in tipos_tokens:
            if type(j)==tuple:
                for k in j:
                    if elemento==k:
                        tipo = j
                        return tipo
            elif j==elemento:
                tipo = j
                return tipo
        tipo = operando
        return tipo

    for i in range(len(tokens)):

        atual_tipo = definir_tipo(tokens[i]) #definir o tipo do token atual

        if i + 1 < len(tokens): #se tem proximo token
            prox_tipo = definir_tipo(tokens[i+1]) #definir o tipo do proximo token
            #print(f'atual: {tokens[i]} {atual_tipo} \nprox: {tokens[i+1]} {prox_tipo}')

            if prox_tipo not in proximos_possiveis[atual_tipo]: #verificar se o token atual aceita o tipo do proximo token
                return False, f'{tokens[i]} não pode preceder {tokens[i+1]}' #lindo

        #paridade dos parenteses
        if tokens[i]=="(":
            counter_parentesis += 1
        elif tokens[i]==")":
            counter_parentesis -= 1

        if counter_parentesis < 0: #parenteses fechando sem parenteses abrindo anteriormente
            return False, "uso incorreto de parenteses"

    if counter_parentesis !=0: #parenteses abrindo que nao foi fechado
        return False, "uso incorreto de parenteses"

    return True, "válido"

# ------------------- 2 CONVERTENDO EM NOTAÇÃO POS FIXA --------------------
def posfixar(tokens:list) -> list:
    from dicsOperadores import dic_precedencia, dic_id, operadores
    aux = ['(',')']
    npf = [] #receber notação pos fixa
    pilha = []

    for i in range(len(tokens)): #percorrer os tokens
        if tokens[i] not in operadores and tokens[i] not in aux: #operandos coloca na lista posfixa
            npf.append(tokens[i])

        elif tokens[i] in operadores: #operadores deve checar
            if pilha==[]: #se a pilha está vazia, adiciona
                pilha.append(tokens[i])
            else: #pilha!=[]
                if pilha[-1]=='(': #nunca vai ser ), só adiciona a pilha normalmente
                    pilha.append(tokens[i])
                elif dic_precedencia[dic_id[tokens[i]]] > dic_precedencia[dic_id[pilha[-1]]]: #se a pilha tiver um operador, deve comparar a precedencia deles
                    pilha.append(tokens[i]) #se o atual tiver maior precedencia, adiciona

                elif dic_precedencia[dic_id[tokens[i]]] == dic_precedencia[dic_id[pilha[-1]]]: #se tiverem a mesma precedencia, adiciona
                    pilha.append(tokens[i])

                elif dic_precedencia[dic_id[tokens[i]]] < dic_precedencia[dic_id[pilha[-1]]]: #se a precedencia do atual for menor
                    while pilha!=[] and pilha[-1]!='(' and dic_precedencia[dic_id[tokens[i]]] <= dic_precedencia[dic_id[pilha[-1]]]: #enquanto a pilha nao esta vazia e a precedencia do atual for menor doq a do ultimo da pilha
                        npf.append(pilha.pop()) #remove o operador da pilha e adiciona na lista posfixa
                    pilha.append(tokens[i]) #adiciona o operador atual a pilha

        elif tokens[i]=='(':
            pilha.append(tokens[i])

        elif tokens[i]==')': #quando encontrar um fecha parenteses, adiciona tudo que estava na pilha a lista posfixa
            while pilha[-1]!='(':
                npf.append(pilha.pop())
            if pilha[-1]=='(': #quando encontra o abre parenteses, remove da pilha e continua
                pilha.pop()

        while i == len(tokens)-1 and pilha!=[]:
            npf.append(pilha.pop())

    return npf

# ----------------------------------------- 3 RESOLVENDO  --------------------
# ------------------- gerando combinações para as variáveis --------------------
def extrair_variaveis(posfixos) -> list: #extrair as variaveis dos posfixos
    from dicsOperadores import operadores
    variaveis = {}
    tamanho = 0
    for i in posfixos:
        if i not in operadores: #o que nao for token, obrigatoriamente é variável, pois não há pareteses nos posfixos
            variaveis[i] = ''
            tamanho += len(i) #controlar o tamanho para futuramente adicionar função de abreviar variáveis não unitárias

    lista_variaveis = list(variaveis.keys())
    return lista_variaveis

def gerar_combinacoes(variaveis):

    qte_combinacoes = 2 ** len(variaveis) #quantidade das combinações é 2**n, pois cada variável pode ter 2 estados (TRUE/ FALSE)
    combinacoes = [0]*qte_combinacoes #lista com a quantidade de combinaçãoes
    for i in range(qte_combinacoes):
        combinacoes[i]={} #cada item da lista de combinações vira um dicionário vazio para receber a combinação

    valores = (True, False) #valores que a variável pode receber

    #qte e tamanho de blocos por variável
    for v in range(len(variaveis)):
        blocos = 2**(v+1) #quantas repartições a variável faz entre TRUE e FALSE (blocos = seção de combinações de 1 variável)
        inicio_bloco = 0
        fim_bloco = inicio_bloco + qte_combinacoes//blocos #tamanho do bloco é a quantidade de combinações // qte de blocos

        #atribuindo valores aos blocos
        for i in range(blocos):
            valor = valores[i%2] #alternar entre TRUE e FALSE para cada bloco

            #colocando o valor na variável e no dicionário
            for j in range(inicio_bloco, fim_bloco): #para o bloco inteiro de combinações a variavel recebe o mesmo valor
                combinacoes[j][variaveis[v]] = valor #coloca a variável na combição
            inicio_bloco = fim_bloco #começa um novo bloco a partir do fim do anterior
            fim_bloco += qte_combinacoes//blocos #define o fim do bloco a partir de seu tamanho
    #tipo de return: [{'p': True, 'q': True}, {'p': True, 'q': False}, {'p': False, 'q': True}, {'p': False, 'q': False}]
    return combinacoes

#--------------- resolução da expressão com os valores dados nas combinações ------------------

def resolver(posfixas):
    from dicsOperadores import operadores, dic_aridade, dic_funcoes, dic_id

    variaveis = extrair_variaveis(posfixas) #execulta a função de extrair variáveis
    combinacoes = gerar_combinacoes(variaveis) #gera a combinação das variáveis

    #descobrir a classificação
    tautologia = True
    contradicao = True

    pilha = [] #armazenar operandos aguardando operador (não precisava ter sido iniciada aq ops)
    tabela = {} #recebe a tabela final com as variáveis, subexpressões, resultado final e subexpressoes
    tamanho = 0 #tamanho do cabeçario (variáveis + susbexpressões + final) para verificar se pode imprimir corretamente

    for c in range(len(combinacoes)): #para cada combinação
        pilha = [] #reiniciar a pilha (não precisava ter sido iniciada antes, opa)
        for i in range(len(posfixas)): #percorrer posfixas
            if posfixas[i] in variaveis:
                expressao = posfixas[i] #armazena a variável
                valor = combinacoes[c][posfixas[i]] #armazena o valor da variável na combinação atual
            elif posfixas[i] in operadores: #se encontar um operador, deve verificar a arridade
                if dic_aridade[dic_id[posfixas[i]]]==1: #se for operador unitário (arridade 1, infere sobre apenas 1 operando)
                    op = pilha.pop() #o operando é o ultimo da pilha de operandos
                    expressao = f'{posfixas[i]} {op[0]}' #a subexpressão é o operador a esquerda e o operando a direita
                    valor = dic_funcoes[dic_id[posfixas[i]]](op[1]) #o valor é a função do operando sobre o operador
                else: #se for operador binário (infere sobre 2 operandos, não suporta operadores com arridade > 2)
                    rhs = pilha.pop() #o operando da direita é o ultimo da pilha
                    lhs = pilha.pop() #o operando da esquerda é o penultimo da pilha (agora o ulitmo, depois da remoção do rhs)
                    expressao = f'{lhs[0]} {posfixas[i]} {rhs[0]}' #a expressão é o operando da esquerda, operador, opr da direita
                    valor = dic_funcoes[dic_id[posfixas[i]]](lhs[1],rhs[1]) #o valor a função do operado sobre os operandos da esqueda e direita
            pilha.append((expressao, valor)) #armazena expressão(variável, subexpressão ou expressao final reconstruida) e valor

            if expressao not in tabela: #tabela irá armazenar um dicionário
                tabela[expressao] = [] #chaves são as expressões e valores são listas que armazenam o valor da expressão para cada linha da tabela/ cada combinação das variáveis iniciais
                tamanho += len(expressao)
            if c+1 > len(tabela[expressao]): #adicionar apenas 1 valor por combinanação a cada variável ou subexpressao (no caso de encontar a mesma variável ou subexpressão mais de uma vez, ex (p ^ p) só armazena 1 p
                tabela[expressao].append(valor)

        #ao fim do for, expressao armazena resultado final para a linha da tabela
        if tabela[expressao][-1]==False: #se for falso em qualquer combinção
            tautologia=False #não pode ser tautologia
            classificacao = 'contradição' #assumir que é contradição
        if tabela[expressao][-1]==True: #se for verdadeiro em qualquer combinaçaõ
            contradicao=False #não pode ser contradiçao
            classificacao = 'tautologia' #assumir que é tautologia
    if not (contradicao or tautologia): #se não for nem tautologia nem contradição
        classificacao = 'contingência' #só pode ser contingência

    return tabela, classificacao, tamanho

# --------------------------- imprimir tabela verdade ---------------------------------------------------

def organizar_dados(dados, variaveis): #caso as variáveis não sejam as primeiras chaves do dicionário tabela
    #dados recebe o resultado[0] da função resolver, nomeado de tabela
    organizados = {} #novo dicionário
    for i in variaveis: #adicionar primeiro as variáveis
        organizados[i]=dados[i]
    for i in dados:
        if i not in organizados: #adicionar o resto das chaves
            organizados[i]=dados[i]
    return organizados

def tabela(posfixos, proposicao): #imprimi tabela e retorna o tamanho da largura da tabela imprimida
    from interface import TAMANHO

    variaveis = extrair_variaveis(posfixos)
    dados = organizar_dados(resolver(posfixos)[0], variaveis)

    chaves = list(dados.keys()) #variáveis, subexpressões e expressão final
    dados[proposicao] = dados.pop(chaves[-1]) #trocar a ultima subexpressao pela proposição original (a reconstruida não é igual pois não considera parenteses)

    #------------ tamanho da tabela horizontalmente -----------------------------------
    tamanho = resolver(posfixos)[2]
    if tamanho > 40: #se o tamanho da linha de cabeçário for mt grande, remover subsexpressoes
        for i in range(len(dados)-1): #remover chaves que não forem variáveis ou que não forem a ultima(proposição final)
            if chaves[i] not in variaveis:
                dados.pop(chaves[i])
                tamanho -= len(chaves[i])
    if tamanho > 100: #se mesmo removendo as subexpressoes, o cabeçário ainda for mt grande
        print('proposição muito grande para formar tabela')
        return False

    largura = (tamanho+len(dados)*4) #cada chave tem 2 espaços e 2 b | nas extremidades
    if largura <= 50:
        base = 50 #fazer a tabela com 50 mesmo se for menor
    else:
        base = largura #se for maior que 50, usar a largura real

    #------------------- imprimir tabela -------------------------
    print(f' gerador de tabelas verdade '.upper().center(base, '=')) #título alinhado ao centro com a largura da tabela
    print('-'*base) #separador do tamanho da largura da tabela

    resultado = f'classificação: {resolver(posfixos)[1].upper()}' #classificação
    espaco_entre = base - len(resultado)-len(proposicao) #espaço entre o resultado e proposição delimitados pela largura da tabela
    if espaco_entre < 4: #se o espaço for menor que 4
        print(proposicao) #imprimir proposição e resultado em linhas separadas
        print(resultado)
    else: #se for maior que 4
        print(f"{proposicao}{' '*espaco_entre}{resultado}") #imprimir proposiçaõ e resultado na mesma linha, separadas pelo espaço restante da ocupação delas na largura da célula
    print('-'*base) #separador

    for chave in dados:
        print(f'| {chave} |', end='') #cabeçario da tabela
    print('')

    for i in range(len(dados[variaveis[0]])): #para cada combinação
        for j in dados: #para cada chave (variável, subexpressao, proposição original)
            match dados[j][i]: #encontrar valor e atribuir representação
                case True:
                    valor = 'V'
                case False:
                    valor = 'F'
            print(f'| {valor.center(len(j))} |', end='')
        print('')
    print('-'*base)

    return base