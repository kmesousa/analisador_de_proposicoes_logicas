se for um parentesis abrindo

(
anterior pode ser

operador (unitario ou binario)
- ()
^ ()

outro parentesis abrindo
(())

proximo pode ser

um parenteses fechando
()

outro parenteses abrindo
((

uma operando

proximos_possiveis = {
    "(": ["(", ")", operando, operador_uni],
    ")": [")", operador_bi],
    operador_uni: ["(", operando, operador_uni]
    operador_bi: ["(", operando, operador_uni]
    operando: []
}