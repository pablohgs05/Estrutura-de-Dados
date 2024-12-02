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