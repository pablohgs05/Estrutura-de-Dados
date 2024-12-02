    def percorrer_em_ordem(self):
        self._percorrer_em_ordem_recursivo(self.raiz)

    def _percorrer_em_ordem_recursivo(self, atual):
        if atual is not None:  # verifica se há um nó
            self._percorrer_em_ordem_recursivo(atual.esquerda)  # visita a esquerda
            print(atual.valor, end=" ")  # imprime o nó atual
            self._percorrer_em_ordem_recursivo(atual.direita)  # visita a direita