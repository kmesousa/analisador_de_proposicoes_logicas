from funcoes import tokenizar, posfixar, extrair_variaveis, gerar_combinacoes, resolver, tabela

title = lambda string: print(f'{ string }'.upper().center(90, '='))

#-------------- testes tokenizar --------------------------------
# TEM MTS ERROS COM O TOKENIZADOR TENHO Q CORRIGIR!!!!!!!!!!!
title('tokenizar')
print(tokenizar('não chove ^ tenho vontade de sair -->vou sair'))
print(tokenizar('-chove ^ tenho vontade de sair --> vou sair'))
print(tokenizar('-(p ^ q) ^ -q'))
print(tokenizar('p ^q'))
print(tokenizar('p <-- q')) #operador errado não idenficica, resolver isso na validação
print(tokenizar('p <-->q'))
print(tokenizar('p <- ->q'))
print(tokenizar('p <> q'))
print(tokenizar('p ^ -%--> q')) #descobrir erro na validação
print(tokenizar('p 0 q'))
print(tokenizar('p ^ ^ q')) #identificar na validação
print(tokenizar('p ===> q'))
print(tokenizar('% ^ *')) #bad token deu certo eba
print(tokenizar('p <--> q ^ q <-- q'))

#--------------- testes posfixar -------------------------------
title('posfixar')
print(posfixar(tokenizar('- p ^ q --> q')))
print(posfixar(tokenizar('- (p ^ q) --> q')))
print(posfixar(tokenizar('- p ^ (q --> q)')))
print(posfixar(tokenizar('-p ^ -q --> q')))

#-------------- extrair variáveis ----------------------
title('extrair variáveis')
print(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q'))))
print(extrair_variaveis(posfixar(tokenizar('-chove ^ tenho vontade de sair --> vou sair'))))
print(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q'))))

#------------ combinacoes e quadro ------------------------
title('combinações')
# quadro_combinacoes(gerar_combinacoes(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q')))))
# quadro_combinacoes(gerar_combinacoes(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q')))))
print(gerar_combinacoes(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q')))))

#------------- resolução ------------------------------------
title('resolução')
print(resolver(posfixar(tokenizar('p ^ q'))))
# tabela(resolver(posfixar(tokenizar('p ^ q'))))
# tabela(resolver(posfixar(tokenizar('-p'))))
# tabela(resolver(posfixar(tokenizar('p / -p'))))
# tabela(resolver(posfixar(tokenizar('p-->q'))))
# tabela(resolver(posfixar(tokenizar('p<--> q'))))
print(resolver(posfixar(tokenizar('p ^ -p --> q'))))
print(resolver(posfixar(tokenizar('p ^ -p --> -p ^ -p'))))
print(resolver(posfixar(tokenizar('p ^ -q --> -p ^q'))))
print(resolver(posfixar(tokenizar('-chove ^ tenho vontade de sair --> vou sair'))))

#---------------- tabela completa final -----------------------------------
title('tabela final')
tabela(posfixar(tokenizar('-p ^ -q')))
tabela(posfixar(tokenizar('p ^ -p')))
tabela(posfixar(tokenizar('p / - p')))
tabela((posfixar(tokenizar('-chove ^ tenho vontade de sair --> vou sair'))))
