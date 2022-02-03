import telnetlib


HOST="10.1.6.119"
PORT ="5038"

tn =telnetlib.Telnet(HOST,PORT)

print('login')

tn.read_until(b'Asterisk Call Manager/2.10.5')


print('ok1')

tn.write(b'Action: Login\n')
tn.write(b'Username: kirill\n')
tn.write(b'Secret: 123456\n')
tn.write(b'\n')
tn.write(b'\n')
tn.read_until(b'Authentication accepted')
print('login ok')


tn.write(b'Action: Originate\n')
tn.write(b'Channel: sip/102\n')
tn.write(b'Context: my\n')
tn.write(b'Exten: 103\n')
tn.write(b'Priority: 1\n')
tn.write(b'Timeout: 30000\n')
tn.write(b'Callerid: 102\n')
tn.write(b'\n')
tn.write(b'\n')






