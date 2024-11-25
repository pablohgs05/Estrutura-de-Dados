def shell_sort(lista):
    gap = len(lista) // 2  # define o tamanho inicial do salto
    while gap > 0:
        for i in range(gap, len(lista)):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:  # desloca valores maiores
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp  # insere o valor na posição correta
        gap //= 2  # reduz o salto


numeros = [64, 34, 25, 12, 22, 11, 90]
shell_sort(numeros)
print(numeros) 