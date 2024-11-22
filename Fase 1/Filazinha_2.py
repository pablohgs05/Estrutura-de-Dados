class Lista:
    def __init__(self, elemento):
        self.elemento = elemento  # armazena o elemento
        self.proximo = None  # ponteiro para o próximo nó (inicializado como None)


class Fila:
    def adicionar(self, elemento, primeiro, ultimo):
        novo = Lista(elemento)  # cria um novo nó
        print(f"\nAdicionando: {elemento}")
        if primeiro is None:  # se a fila está vazia
            primeiro = novo
            ultimo = novo
        else:
            ultimo.proximo = novo  # conecta o novo nó ao final da fila
            ultimo = novo  # atualiza o ponteiro "ultimo" para o novo nó
        self.mostrar_fila(primeiro)
        return primeiro, ultimo

    def remover(self, primeiro, ultimo):
        if primeiro is None:  # se a fila está vazia
            print("\nNão é possível remover, a fila está vazia.")
            return primeiro, ultimo
        elemento_removido = primeiro.elemento  # o elemento removido é o primeiro da fila
        print(f"\nRemovendo: {elemento_removido}")
        primeiro = primeiro.proximo  # move o ponteiro "primeiro" para o próximo nó
        if primeiro is None:  # se a fila ficou vazia, ajusta "ultimo" para None
            ultimo = None
        self.mostrar_fila(primeiro)
        return primeiro, ultimo

    def inicio(self, primeiro):
        if primeiro is None:  # se a fila estiver vazia
            print("\nFila vazia, não há inicio.")
            return None
        return primeiro.elemento  # retorna o elemento do primeiro nó

    def is_empty(self, primeiro):
        return primeiro is None  # verifica se a fila está vazia

    def mostrar_fila(self, primeiro):
        """Mostra a fila após cada operação"""
        if primeiro is not None:
            print("Fila atual:")
            atual = primeiro  # começa no primeiro elemento (primeiro)
            idx = 1
            while atual:
                print(f"{idx}. {atual.elemento}")  # exibe o elemento na fila
                atual = atual.proximo  # passa para o próximo nó
                idx += 1
        else:
            print("Fila está vazia.")
        print("-" * 20)


def fila():
    primeiro = None  # inicializa a fila como vazia
    ultimo = None

    fila = Fila()

    # adicionando elementos na fila
    primeiro, ultimo = fila.adicionar("Manoel", primeiro, ultimo)
    primeiro, ultimo = fila.adicionar("Joseval", primeiro, ultimo)
    primeiro, ultimo = fila.adicionar("Enzo", primeiro, ultimo)

    # exibe o primeiro elemento da fila
    print("Início da fila:", fila.inicio(primeiro)) 

    # removendo elementos da fila
    primeiro, ultimo = fila.remover(primeiro, ultimo)
    primeiro, ultimo = fila.remover(primeiro, ultimo)
    primeiro, ultimo = fila.remover(primeiro, ultimo)
    primeiro, ultimo = fila.remover(primeiro, ultimo)

    # verifica se a fila está vazia
    print("Fila está vazia?", fila.is_empty(primeiro)) 

    primeiro, ultimo = fila.adicionar("João", primeiro, ultimo)

    print("Início da fila após adição:", fila.inicio(primeiro))


fila()
