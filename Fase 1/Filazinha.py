class Loterica:
    def __init__(self):
        self.line = []  #lista para representar a fila

    def enter_line(self, pessoa):
        self.line.append(pessoa)  #adiciona a pessoa ao final da fila
        print(f"{pessoa} entrou na fila.")

    def leave_line(self):
        if self.line:
            pessoa = self.line.pop(0)  #remove a primeira pessoa
            print(f"{pessoa} saiu da fila.")
            return pessoa
        else:
            print("A fila está vazia.")
            return None

#exemplo de uso
queue = Loterica()
queue.enter_line("Manoel")
queue.enter_line("Joseval")
queue.enter_line("Enzo")
queue.leave_line()  #Manoel saiu
queue.leave_line()  #Joseval saiu