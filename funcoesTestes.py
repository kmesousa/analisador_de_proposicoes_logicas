from funcoesPrincipais import tokenizar, posfixar, extrair_variaveis, gerar_combinacoes, quadro_combinacoes, resolver, tabela_beta

#-------------- testes tokenizar --------------------------------
# TEM MTS ERROS COM O TOKENIZADOR TENHO Q CORRIGIR!!!!!!!!!!!
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
print(posfixar(tokenizar('-p ^ -q --> q')))

#-------------- extrair variáveis ----------------------
print(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q'))))
print(extrair_variaveis(posfixar(tokenizar('-chove ^ tenho vontade de sair --> vou sair'))))
print(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q'))))

#------------ combinacoes e quadro ------------------------
quadro_combinacoes(gerar_combinacoes(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q')))))
quadro_combinacoes(gerar_combinacoes(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q')))))
print(gerar_combinacoes(extrair_variaveis(posfixar(tokenizar('- (p ^ q) --> q')))))

#------------- resolução ------------------------------------
tabela_beta(resolver(posfixar(tokenizar('-p ^ -q'))))
tabela_beta(resolver(posfixar(tokenizar('p ^ q'))))
tabela_beta(resolver(posfixar(tokenizar('-p'))))
tabela_beta(resolver(posfixar(tokenizar('p / -p')))) #p tem mais linhas doq devia
tabela_beta(resolver(posfixar(tokenizar('p-->q'))))
tabela_beta(resolver(posfixar(tokenizar('p<--> q'))))
tabela_beta(resolver(posfixar(tokenizar('p ^ -p')))) #p tem mais linhas doq devia
tabela_beta(resolver(posfixar(tokenizar('p ^ -p --> -p ^ -p')))) #era pra ter só duas linhas, mas tem mt mais q isso, como corrigir?
tabela_beta(resolver(posfixar(tokenizar('p ^ -q --> -p ^q')))) #as linhas da tabela estão completamente erradas, aaa #pronto :)