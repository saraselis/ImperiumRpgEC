class Stack:
    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, personagem):
        self.stack.append(personagem)
        self.len_stack += 1

    def pop(self):
        if not self.empty():
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1
        else:
            return 'Não foi possível retirar nenhum elemento, lista vazia'

    def topo(self):
        if not self.empty():
            return self.stack[-1]
        else:
            return 'Pilha vazia'

    def empty(self):
        if(self.len_stack == 0):
            return True
        return False

    def show_pilha(self):
        saida=' '
        for i in self.stack:
            saida += f'{i} '
            saida += '-> '
        print(saida)

    def tamanho(self):
        return self.len_stack
