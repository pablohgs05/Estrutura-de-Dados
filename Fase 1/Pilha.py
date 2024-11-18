class No:
    def __init__(self, dado):
        self.dado = dado  # dado armazenado no nó (livro)
        self.proximo = None  # ponteiro para o próximo nó

class Pilha:
    def __init__(self):
        self.topo = None  # ponteiro para o nó no topo da pilha (cabeça)

    def push(self, livro):
        # cria um novo nó e o coloca no topo da pilha
        novo_no = No(livro)
        novo_no.proximo = self.topo  # faz o novo nó apontar para o nó que era o topo antes
        self.topo = novo_no  # atualiza o topo para ser o novo nó
        print(f"\nO livro '{livro}' foi adicionado.")
        self.mostrar_pilha()

    def pop(self):
        # remove o nó do topo da pilha
        if self.topo:  # verifica se há algum nó no topo da pilha
            livro = self.topo.dado  # armazena o dado do nó atual (o topo)
            self.topo = self.topo.proximo  # atualiza o topo para o próximo nó
            print(f"\nO livro '{livro}' foi removido.")
            self.mostrar_pilha()
            return livro  # retorna o dado do nó removido
        else:
            print("A pilha de livros está vazia.")  # mensagem caso a pilha esteja vazia
            return None

    def mostrar_pilha(self):
        # exibe todos os livros na pilha, um acima do outro
        atual = self.topo  # começa pelo topo da pilha
        print("Visualizando pilha de livros:")
        while atual:  # percorre todos os nós enquanto houver elementos
            print(f"| {atual.dado} |")  # printa o dado do nó como se fosse um livro na pilha
            atual = atual.proximo  # vai para o próximo nó
        print("-" * 20)  # basezinha

    def adicionar_livros(self):
        # adiciona livros à pilha
        self.push("Algoritmos em C")
        self.push("Assassin's Creed")
        self.push("Harry Potter")
        
    def remover_livros(self):
        # remove livros da pilha
        self.pop()
        self.pop()

# exemplo de uso
pilha_livros = Pilha()
pilha_livros.adicionar_livros()
pilha_livros.remover_livros()