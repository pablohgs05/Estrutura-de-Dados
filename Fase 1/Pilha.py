class No:
    def __init__(self, dado):
        self.dado = dado  # dado armazenado no nó (livro)
        self.proximo = None  # Ponteiro para o próximo nó

class Pilha:
    def __init__(self):
        self.topo = None  # ponteiro para o nó no topo da pilha (cabeça)

    def push(self, livro):
        # cria um novo nó e o coloca no topo da pilha
        novo_no = No(livro)
        novo_no.proximo = self.topo
        self.topo = novo_no
        print(f"O livro '{livro}' foi adicionado à pilha.")
        self.mostrar_pilha()

    def pop(self):
        # remove o nó do topo da pilha
        if self.topo:
            livro = self.topo.dado
            self.topo = self.topo.proximo
            print(f"O livro '{livro}' foi removido da pilha.")
            self.mostrar_pilha()
            return livro
        else:
            print("A pilha de livros está vazia.")
            return None

    def mostrar_pilha(self):
        # exibe todos os livros na pilha
        atual = self.topo
        elementos = []
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        print("Estado atual da pilha de livros:", elementos, "\n")

# Criação da pilha de livros
pilha_livros = Pilha()

# Adiciona livros à pilha
pilha_livros.push("Algoritmos em C")
pilha_livros.push("Assassin's Creed")
pilha_livros.push("Harry Potter")

# Remove livros da pilha
pilha_livros.pop()
pilha_livros.pop()