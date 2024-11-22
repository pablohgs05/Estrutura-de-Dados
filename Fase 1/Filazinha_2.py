class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


def enqueue(queue, name):
    new_node = Node(name)
    if queue is None:
        return new_node  # se a fila ta vazia, o novo nó é o primeiro
    else:
        current = queue
        while current.next is not None:  # percorre até o último nó
            current = current.next
        current.next = new_node  # add o novo nó no final
    return queue


def dequeue(queue):
    if queue is None:
        print("A fila está vazia! Não há mais ninguém para atender.")
        return None
    print(f"Atendendo: {queue.name}")
    return queue.next  # retorna o próximo nó como o novo início da fila


def display(queue):
    if queue is None:
        print("A fila está vazia!")
    else:
        print("Fila da lotérica:")
        current = queue
        while current is not None:
            print(f"- {current.name}")
            current = current.next
        print()


queue = None  # fila inicial vazia

# adicionando os veios e o Enzo
queue = enqueue(queue, "Manoel")
queue = enqueue(queue, "Joseval")
queue = enqueue(queue, "Enzo")
display(queue)

# removendo mais pessoas doq tem
queue = dequeue(queue) 
queue = dequeue(queue)  
queue = dequeue(queue)  
queue = dequeue(queue)  
display(queue)