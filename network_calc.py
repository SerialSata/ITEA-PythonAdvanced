import socket

class NetworkView:
    def __init__(self):
        s = socket.socket()
        s.bind(('localhost', 5000))
        s.listen(5)
        self.c, a = s.accept()
        print('Connected', a)
        s.close()

    def _convert(self, mess):
        return str(mess).encode('utf-8')

    def input(self, mess):
        self.print(mess)
        return self.c.recv(1024).decode('utf-8')[:-2]

    def print(self, mess):
        self.c.sendall(self._convert(mess) + b'\n')


class ConsoleView:
    def input(self, mess):
        return input(mess)

    def print(self, mess):
        return print(mess)

# view = ConsoleView()
view = NetworkView()

while True:
    op = view.input("Operator: ")
    if op.lower() == 'q':
        break
    op1 = float(view.input('Operand1?: '))
    op2 = float(view.input('Operand2?: '))
    if op == '+':
        view.print(op1 + op2)
    elif op == '-':
        view.print(op1 - op2)
    else:
        view.print('Invalid operator')
