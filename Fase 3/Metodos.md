## **1. Inserir**
Vamos criar a estrutura básica de uma árvore e o método para **inserir valores**. O nó raiz será definido inicialmente como `None`. Cada nó pode ter dois filhos: um à esquerda (valores menores) e outro à direita (valores maiores).

```python
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
```

### **Explicação**
- O método **`inserir`** adiciona um valor na posição correta da árvore.
- Começa verificando a raiz:
  - Se estiver vazia, o valor vira a raiz.
  - Caso contrário, desce pela árvore até encontrar uma posição vazia (esquerda ou direita).
- **Regra**: valores menores vão à esquerda; maiores, à direita.

---

## **2. Percorrer**
Agora, vamos criar o método para **percorrer a árvore**. Existem três formas principais de percorrer:
1. **Em ordem (in-order)**: Esquerda -> Nó Atual -> Direita.
2. **Pré-ordem (pre-order)**: Nó Atual -> Esquerda -> Direita.
3. **Pós-ordem (post-order)**: Esquerda -> Direita -> Nó Atual.

Aqui vamos implementar o **percurso em ordem**.

```python
    def percorrer_em_ordem(self):
        self._percorrer_em_ordem_recursivo(self.raiz)

    def _percorrer_em_ordem_recursivo(self, atual):
        if atual is not None:  # verifica se há um nó
            self._percorrer_em_ordem_recursivo(atual.esquerda)  # visita a esquerda
            print(atual.valor, end=" ")  # imprime o nó atual
            self._percorrer_em_ordem_recursivo(atual.direita)  # visita a direita
```

### **Explicação**
- Este método percorre a árvore de forma que os valores sejam exibidos **em ordem crescente**.
- Ele:
  1. Vai para a subárvore da esquerda.
  2. Exibe o valor do nó atual.
  3. Vai para a subárvore da direita.

### **Exemplo**
Para a árvore com os valores `[50, 30, 70, 20, 40, 60, 80]`, o percurso em ordem retornaria:
```
20 30 40 50 60 70 80
```

---

## **3. Remover**
A remoção de um nó tem três casos:
1. O nó **não tem filhos**: apenas remove o nó.
2. O nó tem **um filho**: substitui o nó pelo filho.
3. O nó tem **dois filhos**: substitui o nó pelo menor valor da subárvore à direita (sucessor).

```python
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
```

### **Explicação**
- **Caso 1**: Se o nó não tem filhos, simplesmente retorna `None`.
- **Caso 2**: Se o nó tem um único filho, retorna o filho (substituindo o nó atual).
- **Caso 3**: Se o nó tem dois filhos:
  1. Encontra o **menor valor da subárvore à direita** (sucessor).
  2. Substitui o valor do nó pelo sucessor.
  3. Remove o sucessor da subárvore à direita.

---

## **Exemplo Completo**

```python
arvore = ArvoreBinaria()

# inserindo valores
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

# percorrendo em ordem
print("Percurso em ordem:")
arvore.percorrer_em_ordem()  # saída: 20 30 40 50 60 70 80

# removendo um valor
arvore.remover(50)

# percorrendo novamente
print("\nApós remover 50:")
arvore.percorrer_em_ordem()  # saída: 20 30 40 60 70 80
```

---

## **Resumo**

- **Inserção**: Coloca o valor na posição correta da árvore.
- **Percurso**: Exibe os valores da árvore seguindo uma ordem específica.
- **Remoção**: Lida com 3 casos (sem filhos, com um filho ou com dois filhos).

Esses códigos são básicos e diretos, facilitando o entendimento e implementação de árvores binárias de busca.