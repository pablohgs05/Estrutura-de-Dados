class No:
    def __init__(self, valor):
        self.valor = valor  # guarda o valor do nó
        self.esquerda = None  # referência ao filho à esquerda
        self.direita = None  # referência ao filho à direita


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None  # árvore começa vazia

    def inserir(self, valor):
        if self.raiz is None:  # se a árvore está vazia
            self.raiz = No(valor)  # o valor vira a raiz
            print("\n")
            print("---INSERINDOOOOOO---")
            print(f"Raiz {valor} inserida.")
        else:
            self.inserir_recursivo(self.raiz, valor)  # chama método auxiliar

    def inserir_recursivo(self, atual, valor):
        if valor < atual.valor:  # vai para a esquerda se for menor
            if atual.esquerda is None:
                atual.esquerda = No(valor)  # insere o valor à esquerda
                print(f"Nó {valor} inserido à esquerda de {atual.valor}.")
            else:
                self.inserir_recursivo(atual.esquerda, valor)  # continua descendo
        elif valor > atual.valor:  # vai para a direita se for maior
            if atual.direita is None:
                atual.direita = No(valor)  # insere o valor à direita
                print(f"Nó {valor} inserido à direita de {atual.valor}.")
            else:
                self.inserir_recursivo(atual.direita, valor)  # continua descendo

    def percorrer_em_ordem(self):
        print("Percorrendo em ordem:")
        self.percorrer_recursivo(self.raiz)
        print()  # para a próxima linha

    def percorrer_recursivo(self, atual):
        if atual is not None:  # verifica se o nó existe
            self.percorrer_recursivo(atual.esquerda)
            print(atual.valor, end=" ")  # exibe o valor do nó atual
            self.percorrer_recursivo(atual.direita) 

    def remover(self, valor):
        print("\n")
        print("---REMOVENDOOOOOO---")
        print(f"Iniciando remoção do nó com valor {valor}.")
        self.raiz, removido = self.remover_recursivo(self.raiz, valor)
        if removido is not None:
            print(f"Nó removido: {removido.valor}.")
        else:
            print(f"Nó com valor {valor} não encontrado.")

    def remover_recursivo(self, atual, valor):
        if atual is None:  # valor não encontrado
            return None, None

        if valor < atual.valor:  # busca na subárvore esquerda
            atual.esquerda, removido = self.remover_recursivo(atual.esquerda, valor)
            return atual, removido

        elif valor > atual.valor:  # busca na subárvore direita
            atual.direita, removido = self.remover_recursivo(atual.direita, valor)
            return atual, removido

        else:  # valor encontrado
            removido = atual  # registra o nó a ser removido
            print(f"Nó com valor {atual.valor} encontrado para remoção.")

            # caso 1: sem filhos à esquerda
            if atual.esquerda is None:
                print(f"Nó {atual.valor} removido.")
                return atual.direita, removido

            # caso 2: sem filhos à direita
            if atual.direita is None:
                print(f"Nó {atual.valor} removido.")
                return atual.esquerda, removido

            # caso 3: nó com dois filhos
            sucessor = self._encontrar_min(atual.direita)  # encontra o sucessor
            print(f"Sucessor encontrado: {sucessor.valor}. Substituindo {atual.valor} por {sucessor.valor}.")
            atual.valor = sucessor.valor  # substitui o valor
            atual.direita, _ = self.remover_recursivo(atual.direita, sucessor.valor)  # remove sucessor
            return atual, removido

    def _encontrar_min(self, atual):
        while atual.esquerda is not None:  # percorre até o menor valor
            atual = atual.esquerda
        return atual


arvore = ArvoreBinaria()

arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)
arvore.percorrer_em_ordem()

# remoção da raiz 
arvore.remover(50)
arvore.percorrer_em_ordem()

# remoção de outro nó random
arvore.remover(30)
arvore.percorrer_em_ordem()