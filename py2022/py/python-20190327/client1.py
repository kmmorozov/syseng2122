import socket

conn = socket.socket()

conn.connect( ("127.0.0.1", 14901) )

conn.send(b"ls -l")
data = conn.recv(16384)
while data.decode().strip():
    print(data.decode().strip())
    data = conn.recv(16384)
conn.close()
    

