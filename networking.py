import socket

s = socket.socket()
print("socket created successfully")

# port > 1024

port = 18345
s.bind(('', port))
print('socket binded to port', port)
s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print("got connection from ", addr)
    c.send('Thank you for connecting'.encode())
    c.close()
    break
