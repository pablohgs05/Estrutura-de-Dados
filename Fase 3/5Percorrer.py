def percorrer_pre_ordem(self):
    self.percorrer_recursivo_pre_ordem(self.raiz)

def percorrer_recursivo_pre_ordem(self, atual):
    if atual is not None:
        print(atual.valor, end=" ")  # processa o nó atual
        self.percorrer_recursivo_pre_ordem(atual.esquerda)  # visita a esquerda
        self.percorrer_recursivo_pre_ordem(atual.direita)  # visita a direita

def percorrer_em_ordem(self):
    self.percorrer_recursivo_em_ordem(self.raiz)

def percorrer_recursivo_em_ordem(self, atual):
    if atual is not None:
        self.percorrer_recursivo_em_ordem(atual.esquerda)  # visita a esquerda
        print(atual.valor, end=" ")  # processa o nó atual
        self.percorrer_recursivo_em_ordem(atual.direita)  # visita a direita

def percorrer_pos_ordem(self):
    self.percorrer_recursivo_pos_ordem(self.raiz)

def percorrer_recursivo_pos_ordem(self, atual):
    if atual is not None:
        self.percorrer_recursivo_pos_ordem(atual.esquerda)  # visita a esquerda
        self.percorrer_recursivo_pos_ordem(atual.direita)  # visita a direita
        print(atual.valor, end=" ")  # processa o nó atual