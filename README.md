# Gerador e classificador de tabelas verdade

- UFMA 2026.1
- Trabalho final da disciplina de Matemática Discreta e Lógica
- Professor: Francisco Glaubos
- Discentes: Kamily Vitória e Mileena Costa

## Como o programa está estruturado
O programa está estruturado em 3 arquivos principais:
#### 1. dicsOperadores.py
- Onde estão armazenados todos os dicionários contendo as informações dos operadores lógicos, como: símbolos, precedência, aridade, entre outros

#### 2. funcoes.py
- As funções base do programa, que realizam a análise da fórmula dada passo a passo

#### 3. main.py
- Oferece a interface para o usuário final, utilizando das funções e dicionários criados anteriormente

## Como usar o programa
- Resquisitos: Python 3.9

**Passo a passo**
1. Rode o arquivo **main.py**
2. Digite uma fórmula proposicional utilizando dos símbolos listados
3. Veja a tabela verdade
4. Digite "sair" caso queira sair, ou uma nova proposição para ser analisada

## funcionalidades
- A fórmula lógica pode ser escrita tanto da forma **"p ^ -q"**, com variáveis unitárias, como da forma **"pão ^ -queijo"**, com palavras como variáveis
- O programa suporta os cinco operadores principais, levando em conta sua precedência
- O progama possui suporte ao parênteses na análise de precedência

## Limitações e possivéis atualizações
- O programa não suporta fórmulas do tipo **"pão e não queijo"**
- O programa não verifica ou oferece equivalência entre fórmulas
- O programa não permite a troca dos símbolos usados como operadores
- O programa não suporta mais de cinco operadores

**Observação:**
A implementação dos dois últimos items demanada atualizações mínimas e foi pensada na escalabilidade do programa.

## FIM
Obrigada pela atenção!!