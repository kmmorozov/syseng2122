server_file = open('/home/kirill/py2022/servers.txt','r')

for line in server_file:
    print(line.strip())

server_file.close()