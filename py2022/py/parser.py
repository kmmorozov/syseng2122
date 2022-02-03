import telnetlib
import pymysql


HOST = '10.1.6.119'
PORT = '5038'

tn = telnetlib.Telnet(HOST,PORT)
print('connect')
tn.read_until(b'Asterisk Call Manager/2.10.5')
print('ответ получен')

tn.write(b'Action: Login\n')
tn.write(b'Username: kirill\n')
tn.write(b'Secret: 123456\n')
tn.write(b'\n')
tn.write(b'\n')
tn.read_until(b'Authentication accepted')
print('login ok')

while True:
    
        pk = tn.read_until(b'\n\r\n')
        mass=pk.splitlines()
        if str(mass[0]) == "b'Event: DialBegin'":
            
            print(((mass[5]).decode('utf8').split())[1])
            print((mass[12]).decode('utf8').split()[1])
            
            cid = (((mass[5]).decode('utf8').split())[1])
            exten = ((mass[12]).decode('utf8').split()[1])    
            
           # ins = f"insert into calls values('1234','{cid}','{exten}');"
            
            #print(ins)
            #cursor.execute(ins)
            



        
        