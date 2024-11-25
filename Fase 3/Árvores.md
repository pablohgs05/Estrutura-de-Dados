## O que é uma Árvore?

Uma **árvore** é uma estrutura de dados hierárquica, composta por nós (ou vértices). Cada nó pode ter um ou mais filhos, mas apenas um pai (exceto o nó raiz, que não tem pai).

### Terminologia

- **Raiz**: O nó mais alto da árvore. Não possui pai.
- **Nó**: Elemento da árvore que pode ter filhos.
- **Subárvore**: Qualquer nó e todos os seus descendentes.
- **Folha**: Nó que não tem filhos (nós terminais).
- **Profundidade**: Número de arestas desde a raiz até o nó.
- **Altura**: Número máximo de arestas de um nó até uma folha.

### Árvore Binária

Uma **árvore binária** é um tipo especial de árvore onde cada nó pode ter no máximo dois filhos: um à esquerda e outro à direita.

- **Filho à esquerda**: Menor que o nó pai.
- **Filho à direita**: Maior que o nó pai.

### O que é uma Árvore Binária de Busca (ABB)?

Uma **Árvore Binária de Busca** é uma árvore binária com uma característica especial: para cada nó da árvore, todos os valores da subárvore à esquerda são menores que o valor do nó, e todos os valores da subárvore à direita são maiores.

#### Propriedades da Árvore Binária de Busca (ABB):
1. **Organização**: A árvore é organizada de tal forma que, para qualquer nó:
   - O valor do nó à esquerda é menor.
   - O valor do nó à direita é maior.
2. **Pesquisa Rápida**: A ABB permite buscas rápidas em tempo O(log n) (para árvores balanceadas), já que cada comparação elimina metade dos elementos restantes.

---

## Operações em uma Árvore Binária de Busca

As operações principais em uma ABB são **inserção**, **remoção** e **percurso**. Vamos explicar cada uma delas no código a seguir.

### 1. Inserção

A **inserção** em uma ABB acontece de maneira recursiva, sempre colocando o valor no lugar adequado, de acordo com a ordem da árvore. Se o valor for menor que o nó atual, vai para a subárvore esquerda; caso contrário, vai para a subárvore direita.

#### Código de inserção:

```python
class No:
    def __init__(self, valor):
        self.valor = valor  # o valor armazenado no nó
        self.esquerda = None  # referência para o nó à esquerda
        self.direita = None  # referência para o nó à direita

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None  # inicializa a árvore com a raiz como None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)  # se a árvore estiver vazia, insere o valor como raiz
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, atual, valor):
        if valor < atual.valor:  # se o valor for menor, vai para a esquerda
            if atual.esquerda is None:
                atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(atual.esquerda, valor)
        elif valor > atual.valor:  # se o valor for maior, vai para a direita
            if atual.direita is None:
                atual.direita = No(valor)
            else:
                self._inserir_recursivo(atual.direita, valor)
```

### 2. Percurso

Existem três tipos principais de **percurso** em uma árvore binária:
- **Em ordem (in-order)**: Visita o nó da esquerda, depois o nó atual, e finalmente o nó à direita.
- **Pré-ordem (pre-order)**: Visita o nó atual, depois o nó da esquerda, e finalmente o nó à direita.
- **Pós-ordem (post-order)**: Visita o nó da esquerda, depois o nó à direita, e finalmente o nó atual.

#### Código de percurso em ordem (in-order):

```python
    def em_ordem(self):
        self._em_ordem_recursivo(self.raiz)

    def _em_ordem_recursivo(self, atual):
        if atual is not None:
            self._em_ordem_recursivo(atual.esquerda)  # percorre a subárvore à esquerda
            print(atual.valor, end=" ")  # imprime o valor do nó atual
            self._em_ordem_recursivo(atual.direita)  # percorre a subárvore à direita
```

### 3. Remoção

A **remoção** de um nó em uma ABB é mais complexa e depende de três casos:
1. **Nó sem filhos**: Simplesmente remove o nó.
2. **Nó com um filho**: Substitui o nó pelo único filho.
3. **Nó com dois filhos**: Encontra o nó sucessor (o menor valor da subárvore à direita) e o substitui no nó a ser removido.

#### Código de remoção:

```python
    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, atual, valor):
        if atual is None:
            return None
        if valor < atual.valor:  # busca na subárvore esquerda
            atual.esquerda = self._remover_recursivo(atual.esquerda, valor)
        elif valor > atual.valor:  # busca na subárvore direita
            atual.direita = self._remover_recursivo(atual.direita, valor)
        else:
            if atual.esquerda is None:  # se o nó não tem filho à esquerda
                return atual.direita
            if atual.direita is None:  # se o nó não tem filho à direita
                return atual.esquerda
            # caso o nó tenha dois filhos
            sucessor = self._encontrar_min(atual.direita)
            atual.valor = sucessor.valor  # substitui pelo valor do sucessor
            atual.direita = self._remover_recursivo(atual.direita, sucessor.valor)
        return atual

    def _encontrar_min(self, atual):
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
```

---

## Exemplos de Uso

### Inserindo elementos

```python
arvore = ArvoreBinariaBusca()

# inserindo valores na árvore
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

# percorrendo a árvore em ordem
arvore.em_ordem()  # saída: 20 30 40 50 60 70 80
```

### Removendo elementos

```python
# removendo um valor
arvore.remover(50)

# percorrendo a árvore após remoção
arvore.em_ordem()  # saída: 20 30 40 60 70 80
```

---

## Complexidade de Tempo

- **Inserção**: O(n) no pior caso (árvore desbalanceada), mas O(log n) no caso médio (árvore balanceada).
- **Pesquisa**: O(n) no pior caso, mas O(log n) no caso médio.
- **Remoção**: O(n) no pior caso (árvore desbalanceada), mas O(log n) no caso médio.

---

## Conclusão

A **Árvore Binária** é uma estrutura fundamental para implementar operações eficientes de busca, inserção e remoção de dados. Com a característica de manter a ordem dos elementos, ela facilita a realização de buscas binárias, otimizando o desempenho em diversas situações.