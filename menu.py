'''
menu inicial

=========== GERADOR DE TABELAS VERDADE =============
UFMA área básica de ingresso em computação e ia
disciplina: Matemática discreta e lógica
discentes: Kamily e Mileena
professor: Francisco Glaubos                  2026.1
-----------------------------------------------------
                    simbolos
-----------------------------------------------------
[-] não      [-->] se, então
[^] e        [<-->] se, e somente se
[/] ou
-----------------------------------------------------
digite a proposição OU digite:
[0] para sair
[1] para trocar simbolos
[2] para ver exemplos
-----------------------------------------------------
>>>>>>

input invalido
(simbolo invalido ou número invalido
ou proposição invalida)

=========== GERADOR DE TABELAS VERDADE =============
-----------------------------------------------------
                    simbolos
-----------------------------------------------------
[-] não      [-->] se, então
[^] e        [<-->] se, e somente se
[/] ou
-----------------------------------------------------
digite a proposição OU digite:
[0] para sair
[1] para trocar simbolos
[2] para ver exemplos
-----------------------------------------------------
inválido: mensagem! (input da pessoa)
>>>>>>



trocar simbolos
=========== GERADOR DE TABELAS VERDADE =============
-----------------------------------------------------
                    simbolos
-----------------------------------------------------
[-] não      [-->] se, então
[^] e        [<-->] se, e somente se
[/] ou
-----------------------------------------------------
                reconfigurar
não:
e:
ou:
se, então:
se, e comente se:
----------------------------------------------------

confirmar

=========== GERADOR DE TABELAS VERDADE =============
-----------------------------------------------------
              novos simbolos
-----------------------------------------------------
[-] não      [-->] se, então
[^] e        [<-->] se, e somente se
[/] ou
----------------------------------------------------
[0] restaurar padrão
[1] confirmar
[2] refazer
----------------------------------------------------
>>>>>>


resultado (propposição valida)

=========== GERADOR DE TABELAS VERDADE =============
----------------------------------------------------
p ^ -p                    classificação: CONTRADIÇÃO
----------------------------------------------------
p | -p | p ^ -p
T |  F |   F
F |  T |   F

=========== GERADOR DE TABELAS VERDADE =============
----------------------------------------------------
(p ^ q) / - q --> p       classificação: CONTRADIÇÃO
----------------------------------------------------
p | -p | p ^ -p
T |  F |   F
F |  T |   F

=========== GERADOR DE TABELAS VERDADE =============
----------------------------------------------------
- chove ^ quero sair <--> vou sair
classificação: CONTINGENCIA
----------------------------------------------------
chove | quero sair | vou sair |-c ^ q |-c ^ q <--> v
  T   |     T      |     T    |   F   |      F
  T   |     T      |     F    |   F   |      T
  T   |     F      |     T    |   F   |      F
  T   |     F      |     F    |   F   |      T
  F   |     T      |     T    |   T   |      T
  F   |     T      |     F    |   T   |      F
  F   |     F      |     T    |   F   |      F
  F   |     F      |     F    |   F   |      T

====================== GERADOR DE TABELAS VERDADE ===============================
---------------------------------------------------------------------------------
amo meus pais ^ tenho dinheiro --> comprar um presente para meus pais
classificação: CONTINGENCIA
---------------------------------------------------------------------------------
amo meus pais | tenho dinheiro | comprar um presente para meus pais | a ^ t --> c
      T       |       T        |               T                    |       F
      T       |       T        |               F                    |       T
      T       |       F        |               T                    |       F
      T       |       F        |               F                    |       T
      F       |       T        |               T                    |       T
      F       |       T        |               F                    |       F
      F       |       F        |               T                    |       F
      F       |       F        |               F                    |       T

ou (acho que é melhor fazer assim, eh(se tiver duas com o msm nome bota a, a1, a2, etc...))
---------------------------------------------------------------------------------
a | t | c | a ^ t --> c
---------------------------------------------------------------------------------

1. se a soma dos tamanhos das variáveis for maior do que 20, susbstituir todas
pos letras

2. soma dos tamanhos das variáveis + | + espaços + proposição final (+ subs, caso fosse ter elas)

3. a primeira linha
(variavel1 + espaço + traço + espaço + variável 2 + espaço + traço + espaço+ proposição)

usar esse o tamanho disso tudo para determinar o tamanho nas linhas -----
e o tamanho das próximas linhas com os valores

4. formar as outras linhas obedecendos os espaços estabelecidos na primeira


'''
#mds

print(len('chove |'))
print(len('      |')) #ebaa
print(f'oi'.center(50))

variaveis = ['p','q']
header = f'| {variaveis[0]} |'
print(header)
dados = {'p': [True, False], 'q': [True, False]}
match dados[variaveis[0]][0]:
    case True:
        valor = 'V'
    case False:
        valor ='F'
  
print('|',valor.center(len(header)-4),'|')
print(f'| {valor.center(len(header)-4)} |')