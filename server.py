# import socket
# import threading
#
# # синхронный сервер
#
#
# def handle(c):
#     while True:
#         data = c.recv(1024)
#         if not data:
#             c.close()
#             break
#         print(data)
#         c.sendall(data)
#
#
# s = socket.socket()
# s.bind(('localhost', 5000))
# s.listen(5)
# print('Waiting...')
# while True:
#     c, a = s.accept()
#     print('Connected: ', a)
#     t = threading.Thread(target=handle, args=(c, ))
#     t.start()

# асинхронный сервер

import socket
import select


def handle(c):
    data = c.recv(1024)
    if not data:
        connections.remove(c)
        c.close()
        return
    print(data)
    c.sendall(data)

s = socket.socket()
s.bind(('localhost', 5000))
s.setblocking(False)
s.listen(5)
print('Waiting...')
connections = [s]
while True:
    r_s, _, _ = select.select(connections, [], [])
    for r in r_s:
        if r == s:
            c, a = s.accept()
            print('Connected: ', a)
            connections.append(c)
        else:
            handle(r)
