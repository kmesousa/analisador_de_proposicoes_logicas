entrada/string
-> preparação e avaliação básica
-> tokenização / lexer
-> shunting yard / rpn
-> avaliação e tabelas

ou
-> rpn > ast
-> avaliação e tabelas

-> classificação

-(pao ^ banana) --> - comer muito

aluno1 ^ aluno2 --> aluno3

2coelhos ^ 3arvores --> 5 itens

pao

banana

comer muito

pao

banana

comer muito

remover os espaços do começo e fim após separar os tokens!!!
tokens.append(i.strip()) algo assim!!

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