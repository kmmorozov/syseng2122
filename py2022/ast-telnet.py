import telnetlib

HOST = '192.168.20.23'
PORT = "5038"

tn = telnetlib.Telnet(HOST,PORT)

print('connect ok')

tn.read_until(b'Asterisk Call Manager/5.0.3')


tn.write(b'Action: login\n')
tn.write(b'Username: kirill\n')
tn.write(b'Secret: 123456\n')
tn.write(b'\n')
tn.write(b'\n')

tn.read_until(b'Authentication accepted')

print('login ok')

