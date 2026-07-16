from funcoes import *

print(validar(tokenizar("(p ^ q) ^ - q")))
print(validar(tokenizar("-q")))
print(validar(tokenizar("- -q")))
print(validar(tokenizar("- ^ q")))
print(validar(tokenizar("p ^ (-q)")))
print(validar(tokenizar("(p ^) q ")))