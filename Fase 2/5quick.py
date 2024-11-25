def quick_sort(lista):
    if len(lista) <= 1:  # caso base: lista com 0 ou 1 elemento
        return lista
    else:
        pivo = lista[0]  # escolhe o primeiro elemento como pivô
        menores = [x for x in lista[1:] if x <= pivo]  # elementos menores ou iguais
        maiores = [x for x in lista[1:] if x > pivo]  # elementos maiores
        return quick_sort(menores) + [pivo] + quick_sort(maiores)  # junta tudo


numeros = [64, 34, 25, 12, 22, 11, 90]
numeros = quick_sort(numeros)
print(numeros) 