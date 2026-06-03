def parenteseses_certos(texto:str, com=False) -> bool:
    #só verifica se eles estão pareados corretamente, não diz nada a respeito do posicionamento parenteses, operandos e operadores(ex. invalidade de (90+)40, 90(40), validade de (90)+40, etc), então acho que é melhor usar outro método que cubra tudo de uma vez
    if com!= 0 and com!=False:
        com = True

    lista = list(texto)
    if com:
        print(lista)

    pilha1 = [] #( não pode conter elementos no final
    pilha2 =[] #) não pode conter elementos caso a pilha 2 esteja vazia a qualquer momento

    for i in range (0, len(lista)):
        #1: direcionamento
        if lista[i] == '(':
            pilha1.append(lista[i])
        elif lista[i] == ')':
            pilha2.append(lista[i])
        if com:
            print(pilha1, pilha2)

        #2: pareamento
        while len(pilha2)!=0 and len(pilha1)!=0:
            del pilha1[0]
            del pilha2[0]
            if com:
                print(pilha1, pilha2)

        #3: validadação
        if com:
            print(len(pilha1), len(pilha2))
        if len(pilha2)!=0:
            return False
    if pilha1!=[]:
        return False
    return True