def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2  # encontra o meio da lista
        esquerda = lista[:meio]  # divide em esquerda
        direita = lista[meio:]  # e direita

        merge_sort(esquerda)  # ordena a esquerda
        merge_sort(direita)  # ordena a direita

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):  # combina as partes
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1


numeros = [64, 34, 25, 12, 22, 11, 90]
merge_sort(numeros)
print(numeros) 