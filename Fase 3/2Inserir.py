class No:
    def __init__(self, valor):
        self.valor = valor  # guarda o valor do nó
        self.esquerda = None  # guarda o filho à esquerda
        self.direita = None  # guarda o filho à direita

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None  # começa com uma árvore vazia

    def inserir(self, valor):
        if self.raiz is None:  # se a árvore está vazia
            self.raiz = No(valor)  # o primeiro valor vira a raiz
        else:
            self._inserir_recursivo(self.raiz, valor)  # chama a função auxiliar

    def _inserir_recursivo(self, atual, valor):
        if valor < atual.valor:  # vai para a esquerda se for menor
            if atual.esquerda is None:  # encontrou espaço
                atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(atual.esquerda, valor)  # continua descendo
        elif valor > atual.valor:  # vai para a direita se for maior
            if atual.direita is None:  # encontrou espaço
                atual.direita = No(valor)
            else:
                self._inserir_recursivo(atual.direita, valor)  # continua descendo