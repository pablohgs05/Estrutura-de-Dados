def selection_sort(lista):
    # percorre toda a lista
    for i in range(len(lista)):
        menor_indice = i  # assume que o atual é o menor
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor_indice]:  # encontra o menor elemento
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]  # troca o menor para a posição correta


numeros = [64, 34, 25, 12, 22, 11, 90]
selection_sort(numeros)
print(numeros)