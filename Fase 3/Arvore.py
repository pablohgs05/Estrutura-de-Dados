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
        else:
            self.inserir_recursivo(self.raiz, valor)  # chama método auxiliar

    def inserir_recursivo(self, atual, valor):
        if valor < atual.valor:  # vai para a esquerda se for menor
            if atual.esquerda is None:
                atual.esquerda = No(valor)  # insere o valor à esquerda
            else:
                self.inserir_recursivo(atual.esquerda, valor)  # continua descendo
        elif valor > atual.valor:  # vai para a direita se for maior
            if atual.direita is None:
                atual.direita = No(valor)  # insere o valor à direita
            else:
                self.inserir_recursivo(atual.direita, valor)  # continua descendo

    # método para percorrer a árvore em ordem (menor para maior)
    def percorrer_em_ordem(self):
        self._percorrer_em_ordem_recursivo(self.raiz)

    def _percorrer_em_ordem_recursivo(self, atual):
        if atual is not None:  # verifica se o nó existe
            self._percorrer_em_ordem_recursivo(atual.esquerda)  # visita esquerda
            print(atual.valor, end=" ")  # exibe o valor do nó atual
            self._percorrer_em_ordem_recursivo(atual.direita)  # visita direita

    # método para remover um valor da árvore
    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, atual, valor):
        if atual is None:  # valor não encontrado
            return None
        if valor < atual.valor:  # busca na subárvore esquerda
            atual.esquerda = self._remover_recursivo(atual.esquerda, valor)
        elif valor > atual.valor:  # busca na subárvore direita
            atual.direita = self._remover_recursivo(atual.direita, valor)
        else:  # valor encontrado
            if atual.esquerda is None:  # sem filho à esquerda
                return atual.direita
            if atual.direita is None:  # sem filho à direita
                return atual.esquerda
            # nó com dois filhos: substitui pelo menor valor da direita
            sucessor = self._encontrar_min(atual.direita)
            atual.valor = sucessor.valor  # copia o valor do sucessor
            atual.direita = self._remover_recursivo(atual.direita, sucessor.valor)
        return atual

    def _encontrar_min(self, atual):
        while atual.esquerda is not None:  # encontra o menor valor
            atual = atual.esquerda
        return atual

# teste
arvore = ArvoreBinaria()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

# percorrendo
print("\nPercurso em ordem:")
arvore.percorrer_em_ordem()
# removendo
arvore.remover(50)
# percorrendo dnv
print("\nApós remover 50:")
arvore.percorrer_em_ordem()
print("\n")