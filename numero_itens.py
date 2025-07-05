def numero_itens_lista(lista):
    if not lista:
        return 0
    return 1 + numero_itens_lista(lista[1:])


resultado1 = numero_itens_lista([2, 4, 6])
print(resultado1)
