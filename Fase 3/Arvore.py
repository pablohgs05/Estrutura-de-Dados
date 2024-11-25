class No:
    # representa um nó da árvore
    def __init__(self, valor):
        self.valor = valor  # armazena o valor do nó
        self.esquerda = None  # referência para o filho à esquerda
        self.direita = None  # referência para o filho à direita


class ArvoreBinariaBusca:
    # representa uma árvore binária de busca
    def __init__(self):
        self.raiz = None  # inicializa a árvore sem nenhum nó

    def inserir(self, valor):
        # insere um valor na árvore
        if self.raiz is None:
            self.raiz = No(valor)  # define a raiz se a árvore estiver vazia
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, atual, valor):
        # insere recursivamente no local correto
        if valor < atual.valor:  # vai para a esquerda se menor
            if atual.esquerda is None:
                atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(atual.esquerda, valor)
        elif valor > atual.valor:  # vai para a direita se maior
            if atual.direita is None:
                atual.direita = No(valor)
            else:
                self._inserir_recursivo(atual.direita, valor)

    def em_ordem(self):
        # percorre a árvore em ordem crescente
        self._em_ordem_recursivo(self.raiz)

    def _em_ordem_recursivo(self, atual):
        # função auxiliar para percorrer em ordem
        if atual is not None:
            self._em_ordem_recursivo(atual.esquerda)  # percorre à esquerda
            print(atual.valor, end=" ")  # imprime o valor do nó atual
            self._em_ordem_recursivo(atual.direita)  # percorre à direita

    def remover(self, valor):
        # remove um nó da árvore
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, atual, valor):
        # função auxiliar para remoção recursiva
        if atual is None:
            return None  # retorna se o nó não for encontrado
        if valor < atual.valor:  # busca na subárvore esquerda
            atual.esquerda = self._remover_recursivo(atual.esquerda, valor)
        elif valor > atual.valor:  # busca na subárvore direita
            atual.direita = self._remover_recursivo(atual.direita, valor)
        else:
            # caso o nó tenha um filho ou nenhum
            if atual.esquerda is None:
                return atual.direita
            if atual.direita is None:
                return atual.esquerda
            # caso tenha dois filhos, encontra o menor na subárvore direita
            sucessor = self._encontrar_min(atual.direita)
            atual.valor = sucessor.valor  # substitui pelo sucessor
            atual.direita = self._remover_recursivo(atual.direita, sucessor.valor)
        return atual

    def _encontrar_min(self, atual):
        # encontra o menor valor em uma subárvore
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual


arvore = ArvoreBinariaBusca()

# inserindo valores
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

# percorrendo em ordem
print("árvore em ordem:")
arvore.em_ordem()
print()

# removendo
print("removendo o valor 50:")
arvore.remover(50)
arvore.remover(60)

# percorrendo em ordem novamente
print("árvore após a remoção:")
arvore.em_ordem()
print()