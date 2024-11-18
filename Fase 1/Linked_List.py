class Node:
    def __init__(self, data):
        self.data = data  # armazena o dado
        self.next = None  # inicialmente, não aponta para nenhum próximo nó

class ListaEncadeada:
    def __init__(self):
        self.head = None  # define a cabeça da lista como vazia

    def add(self, data):
        # cria um novo nó com o dado e insere no início da lista
        new_node = Node(data)
        new_node.next = self.head  # o novo nó aponta para a antiga cabeça
        self.head = new_node  # atualiza a cabeça para o novo nó
        print(f"\nO elemento '{data}' foi adicionado à lista.")
        self.mostrar_lista()

    def mostrar_lista(self):
        # exibe os elementos da lista encadeada em ordem
        atual = self.head  # começa pela cabeça
        print("Lista atual: ", end="")
        while atual:  # percorre a lista até o final
            print(f"{atual.data} -> ", end="")
            atual = atual.next  # avança para o próximo nó
        print("None")  # indica o fim da lista

# usando a lista encadeada
linked_list = ListaEncadeada()
linked_list.add("A")  # adiciona o elemento 'A'
linked_list.add("B")  # adiciona o elemento 'B'
linked_list.add("C")  # adiciona o elemento 'C'