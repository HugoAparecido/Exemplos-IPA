numeros = [5, 1, 9, 3]  # Lista de números a serem ordenados
tamanho = len(numeros)

# Loop principal do Bubble Sort
for i in range(tamanho - 1):
    for j in range(tamanho - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Troca os elementos de posição
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Imprime a lista ordenada
print("Lista ordenada:")
for i in range(tamanho):
    print(numeros[i], end=" ")
