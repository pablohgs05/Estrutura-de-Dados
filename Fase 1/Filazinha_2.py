class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


def adicionar(fila, name):
    new_node = Node(name)
    if fila is None:
        return new_node  # se a fila ta vazia, o novo nó é o primeiro
    else:
        current = fila
        while current.next is not None:  # percorre até o último nó
            current = current.next
        current.next = new_node  # add o novo nó no final
    return fila


def remover(fila):
    if fila is None:
        print("A fila está vazia! Não há mais ninguém para atender.")
        return None
    print(f"Atendendo: {fila.name}")
    return fila.next  # retorna o próximo nó como o novo início da fila


def mostrar(fila):
    if fila is None:
        print("A fila está vazia!")
    else:
        print("Fila da lotérica:")
        current = fila
        while current is not None:
            print(f"- {current.name}")
            current = current.next
        print()


fila = None  # fila inicial vazia

# adicionando os veios e o Enzo
fila = adicionar(fila, "Manoel")
fila = adicionar(fila, "Joseval")
fila = adicionar(fila, "Enzo")
mostrar(fila)

# removendo mais pessoas doq tem
fila = remover(fila) 
fila = remover(fila)  
fila = remover(fila)  
fila = remover(fila)  
mostrar(fila)
