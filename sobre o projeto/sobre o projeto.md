etapas do programa
1. menu e entrada
    ultimo a ser feito
2. tokenização
    falta verificar que só podem ser tokens letrar do alfabeto e números
3. validação inicial
    falta fazer
4. notação pos fixa
    pronta
5. combinacoes
    pronta
5. avaliação, tabelas e classificação
    falta fazer

## como fazer a resolução
-> só rpn ou
ou
-> rpn > ast

partes da resolução
- avaliação e tabelas
- classificação (acho que o mais fácio)

# exemplos de proposições a serem avaliadas

## valido
-(pao ^ banana) --> - comer muito
proposições átomos seriam: pao, banana, comer muito (como se fosse p, q, r)

aluno1 ^ aluno2 --> amizade
sla

2coelhos ^ 3arvores <--> 5 itens


## invalido

## pensamentos sobre a avaliação
avaliação durante outras etapas, posso fazer durente a tokenização ou durante a rpn, mas durente a tokenização deve ser melhor pq na rpn já vou tá fazendo mt coisa
só o da paridade dos parenteses que eu acho difícil fazer aq, talvez possa deixar só ela pra rpn
pq as outras avaliam o token que tá do lado delas, essa dos parenteses pode estar longe
panic()
return 'bad token: x at index y'

90 + + 90

90 90 + 80 #ou pode ser 9090 +80, já que nas proposições pode uma composta contar como só uma

90(+40)
(90+)40
(+)

)90(

# RESOLUÇÂO (ainda não sei bem como)
criar as árvores??

ou

1 achar os operandos difirentes? (acho que com um dicionário é mais fácil)
2 dps atribuir valor a eles / criar as combinações
3 resolver e classificar?
acho q é né

extra: subexpressoes
seria mais difícil