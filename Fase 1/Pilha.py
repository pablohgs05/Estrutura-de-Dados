class Livros:
    def __init__(self):
        self.stack = []  #lista para representar a pilha de livros

    def add_livro(self, livro):
        self.stack.append(livro)  #adiciona o livro ao topo da pilha
        print(f"O livro '{livro}' foi adicionado à pilha.")

    def remove_livro(self):
        if self.stack:
            livro = self.stack.pop()  #remove o livro do topo da pilha
            print(f"O livro '{livro}' foi removido da pilha.")
            return livro
        else:
            print("A pilha de livros está vazia.")
            return None

stack = Livros()
stack.add_livro("Algoritmos em C")
stack.add_livro("Assassin's Creed")
stack.add_livro("Harry Potter")
stack.remove_livro()  #remove o último que entrou
stack.remove_livro()  #remove o próximo na pilha
