def valor_mais_alto(lista):
    if not lista:
        raise ValueError("Lista não pode estar vazia")
    if len(lista) == 1:
        return lista[0]
    else:
        return max(lista[0], valor_mais_alto(lista[1:]))
    
    
resultado1 = valor_mais_alto([2, 4, 6])
print(resultado1)