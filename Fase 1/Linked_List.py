class Node:
    def __init__(self, data):
        self.data = data  #armazena o dado
        self.next = None  #não aponta para nenhum próximo nó

class Listaencadeada:
    def __init__(self):
        self.head = None  #define a cabeça da lista, inicialmente vazia

    def add(self, data):
        new_node = Node(data)  #cria um novo nó com o dado
        new_node.next = self.head  #faz o novo nó apontar para o nó cabeça atual
        self.head = new_node  #atualiza a cabeça para o novo nó

#usando
linked_list = Listaencadeada()
linked_list.add("A")
linked_list.add("B")
linked_list.add("C")
