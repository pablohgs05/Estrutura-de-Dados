    def percorrer_em_ordem(self):
        self.percorrer_recursivo(self.raiz)

    def percorrer_recursivo(self, atual):
        if atual is not None:  # verifica se há um nó
            self.percorrer_recursivo(atual.esquerda)  # visita a esquerda
            print(atual.valor, end=" ")  # imprime o nó atual
            self.percorrer_recursivo(atual.direita)  # visita a direita