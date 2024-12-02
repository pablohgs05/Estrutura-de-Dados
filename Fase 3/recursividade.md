### O que é recursão?
- **Recursão** é uma técnica onde uma função chama a **si mesma** para resolver problemas menores, até chegar em um caso "simples" (base) que pode ser resolvido diretamente.
- Exemplo clássico: calcular fatorial de um número:
  - \( fatorial(5) = 5 \times fatorial(4) \)
  - \( fatorial(4) = 4 \times fatorial(3) \)
  - E assim vai... até chegar em \( fatorial(1) = 1 \).

---

### Por que usar recursão em árvores?
- Árvores têm uma **estrutura hierárquica**: cada nó pode ter **subárvores** (esquerda e direita).
- Para percorrer, buscar, inserir ou remover, precisamos "navegar" pelos **nós e suas subárvores**.
- Recursão é perfeita para árvores porque resolve um **problema grande (árvore inteira)** dividindo-o em **problemas menores (subárvores)**.

---

### Como funciona nos métodos da árvore?

#### 1. **Inserir**
- Queremos inserir um valor no lugar certo (esquerda ou direita):
  - **Se o valor for menor**, vamos para a subárvore esquerda.
  - **Se o valor for maior**, vamos para a subárvore direita.
- A recursão é usada para continuar "descendo" pela árvore até encontrar um nó vazio onde o valor pode ser inserido.

**Exemplo:**
Inserir `40` na árvore:
```
        50
       /  \
     30    70
    /  \
  20    [vazio]
```
- O método recursivo vai:
  1. Comparar `40` com `50` (menor, vai à esquerda).
  2. Comparar `40` com `30` (maior, vai à direita).
  3. Encontrar o espaço vazio e inserir.

---

#### 2. **Percorrer**
- O percurso **em ordem** visita os nós na ordem crescente:
  - **Esquerda → Atual → Direita**
- A recursão faz o percurso para cada subárvore.

**Exemplo:** Percorrer:
```
        50
       /  \
     30    70
    /  \
  20    40
```
- A recursão vai:
  1. Visitar a subárvore da esquerda de `50` (que é `30`).
  2. Dentro de `30`, visitar sua subárvore da esquerda (`20`), imprimir `20`.
  3. Imprimir `30` e visitar a direita (`40`), imprimindo `40`.
  4. Voltar para `50`, imprimir `50` e visitar `70`.

Resultado: `20, 30, 40, 50, 70`.

---

#### 3. **Remover**
- Para remover, precisamos localizar o valor e lidar com três casos:
  1. **Sem filhos**: Apagar o nó.
  2. **Com um filho**: Substituir pelo filho.
  3. **Com dois filhos**: Substituir pelo menor valor da subárvore direita.
- A recursão ajuda a:
  - Localizar o nó que queremos remover.
  - Continuar "descendo" para ajustar a subárvore.

**Exemplo:** Remover `30`:
```
        50
       /  \
     30    70
    /  \
  20    40
```
1. A recursão encontra `30`.
2. O nó tem dois filhos (`20` e `40`).
3. Substituímos `30` por `40` (o menor valor da direita).

Resultado:
```
        50
       /  \
     40    70
    /
  20
```

---

### Por que não usar laços (`while`) no lugar de recursão?
- Com laços, o código fica **mais complexo** e **menos natural** para árvores, porque você precisaria gerenciar manualmente quais subárvores visitar.
- A recursão "automaticamente" lida com isso, ao chamar a função para cada subárvore, simplificando o processo.

---

### Resumo
1. **Recursão** é usada porque árvores são **estruturas hierárquicas** (divididas em subárvores).
2. Cada operação (inserir, percorrer, remover) se resolve descendo por nós e subárvores.
3. A recursão simplifica o código, evitando a necessidade de laços complicados.