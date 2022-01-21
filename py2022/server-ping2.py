import os

server_file = open('/home/kirill/py2022/servers.txt','r')


for server in server_file:

    result = os.system(f'ping -c 1 {server.strip()} > /dev/null')
    if result:
        print(f'IP адрес этого сервера {server.strip()} и он не пингуется!')
        
    else:
        print(f'IP адрес этого сервера {server.strip()} и он  пингуется!')

server_file.close()