def soma_lista_recursiva(lista):
    if not lista:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        primeiro_elemento = lista[0]
        resto_da_lista = lista[1:]
        resultado_recursao = soma_lista_recursiva(resto_da_lista)
        soma_atual = primeiro_elemento + resultado_recursao
        return soma_atual


resultado1 = soma_lista_recursiva([2, 4, 6])
print(resultado1)
