def insertion_sort(lista):
    # percorre a lista do segundo elemento em diante
    for i in range(1, len(lista)):
        chave = lista[i]  # guarda o valor atual
        j = i - 1
        while j >= 0 and lista[j] > chave:  # desloca valores maiores para frente
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave  # insere o valor na posição correta


numeros = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(numeros)
print(numeros)