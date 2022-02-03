import telnetlib

HOST="10.1.6.131"
PORT ="5038"

tn =telnetlib.Telnet(HOST,PORT)

print('login')

tn.read_until(b'Asterisk Call Manager/2.10.4')

print('ok1')

tn.write(b'Action: Login\n')
tn.write(b'Username: kirill\n')
tn.write(b'Secret: 123456\n')
tn.write(b'\n')
tn.write(b'\n')
tn.read_until(b'Authentication accepted')
print('login ok')

while 1:
    
    ar=tn.read_until(b'\n\r\n')
   # print(type(ar))
    arstr=ar.splitlines()
    #print(arstr)
##    for  stroka in arstr:
##        print(stroka.decode())
    #print(arstr[0].decode())
##
    if arstr[0].decode() == 'Event: DialBegin':
        print(arstr[5].decode().split(' ')[1])
        print(arstr[12].decode().split(' ')[1])
        
        
        

