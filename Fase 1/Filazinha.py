class Loterica:
    def __init__(self):
        self.fila = []  # lista para representar a fila

    def entrar_na_fila(self, pessoa):
        # adiciona a pessoa ao final da fila
        self.fila.append(pessoa)
        print(f"\n{pessoa} entrou na fila.")
        self.mostrar_fila()

    def sair_da_fila(self):
        # remove a primeira pessoa da fila
        if self.fila:  # verifica se a fila não está vazia
            pessoa = self.fila.pop(0)
            print(f"\n{pessoa} saiu da fila.")
            self.mostrar_fila()
            return pessoa
        else:
            print("\nA fila está vazia.")
            return None

    def mostrar_fila(self):
        # exibe a fila em ordem, como se fosse uma linha
        if self.fila:  # verifica se há pessoas na fila
            print("Fila atual:")
            for idx, pessoa in enumerate(self.fila, start=1):
                print(f"{idx}. {pessoa}")  # printando com indice p n confundir
        else:
            print("Fila está vazia.")
        print("-" * 20)  # base

    def adicionar_pessoas(self):
        # adicionando pessoas na fila
        self.entrar_na_fila("Manoel")
        self.entrar_na_fila("Joseval")
        self.entrar_na_fila("Enzo")

    def remover_pessoas(self):
        # remove as pessoas da fila
        self.sair_da_fila()
        self.sair_da_fila()

# uso
fila_loterica = Loterica()
fila_loterica.adicionar_pessoas()
fila_loterica.remover_pessoas()