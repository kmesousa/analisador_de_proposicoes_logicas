from funcoesPrincipais import tokenizar, posfixar, extrair_variaveis, gerar_combinacoes, quadro_combinacoes

#-------------- testes tokenizar --------------------------------
print(tokenizar('não chove ^ tenho vontade de sair --> vou sair'))
print(tokenizar('-chove ^ tenho vontade de sair --> vou sair'))
print(tokenizar('-(p ^ q) ^ -q'))
print(tokenizar('p ^ q'))
print(tokenizar('p <-- q')) #operador errado não idenficica, resolver isso na validação
print(tokenizar('p <--> q'))
print(tokenizar('p <- -> q'))
print(tokenizar('p <> q'))
print(tokenizar('p ^ -%--> q')) #descobrir erro na validação
print(tokenizar('p 0 q'))
print(tokenizar('p ^ ^ q')) #identificar na validação
print(tokenizar('p ===> q'))
print(tokenizar('% ^ *')) #bad token deu certo eba
print(tokenizar('p <--> q ^ q <-- q'))

#--------------- testes posfixar -------------------------------
print(posfixar(tokenizar('- p ^ q --> q')))
print(posfixar(tokenizar('- (p ^ q) --> q')))
print(posfixar(tokenizar('- p ^ (q --> q)')))

#------------ combinacoes e quadro ------------------------
quadro_combinacoes(gerar_combinacoes(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q')))))
quadro_combinacoes(gerar_combinacoes(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q')))))