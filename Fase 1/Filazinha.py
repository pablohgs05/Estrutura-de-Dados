class Nodo:
    def __init__(self, pessoa=None):
        self.pessoa = pessoa  # armazena a pessoa
        self.proximo = None  # ponteiro para o próximo nodo

class Loterica:
    def __init__(self):
        self.frente = None  # aponta para o primeiro elemento da fila
        self.traseira = None  # aponta para o último elemento da fila
        self.tamanho = 0  # tamanho da fila

    def entrar_na_fila(self, pessoa):
        novo_nodo = Nodo(pessoa)  # cria um novo nó para a pessoa
        if self.tamanho == 0:
            self.frente = novo_nodo  # se a fila está vazia, frente e traseira apontam para o novo nó
            self.traseira = novo_nodo
        else:
            self.traseira.proximo = novo_nodo  # conecta o novo nó ao final da fila
            self.traseira = novo_nodo  # atualiza a traseira para o novo nó
        self.tamanho += 1
        print(f"\n{pessoa} entrou na fila.")
        self.mostrar_fila()

    def sair_da_fila(self):
        if self.tamanho > 0:
            pessoa = self.frente.pessoa  # a pessoa a ser removida é o primeiro da fila
            self.frente = self.frente.proximo  # atualiza a frente para o próximo nó
            self.tamanho -= 1
            if self.tamanho == 0:
                self.traseira = None  # se a fila ficou vazia, resetamos a traseira para None
            print(f"\n{pessoa} saiu da fila.")
            self.mostrar_fila()
            return pessoa
        else:
            print("\nNão é possível remover alguém da fila, pois ela está vazia.")
            return None

    def mostrar_fila(self):
        if self.tamanho > 0:
            print("Fila atual:")
            atual = self.frente  # começa no primeiro elemento (frente)
            idx = 1
            while atual:
                print(f"{idx}. {atual.pessoa}")  # exibe a pessoa na fila
                atual = atual.proximo  # passa para o próximo nó
                idx += 1
        else:
            print("Fila está vazia.")
        print("-" * 20)

    def adicionar_pessoas(self):
        self.entrar_na_fila("Manoel")
        self.entrar_na_fila("Joseval")
        self.entrar_na_fila("Enzo")

    def remover_pessoas(self):
        self.sair_da_fila()
        self.sair_da_fila()

fila_loterica = Loterica()
fila_loterica.adicionar_pessoas()
fila_loterica.remover_pessoas()
