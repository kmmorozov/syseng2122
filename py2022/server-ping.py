import os

servers = ['192.168.20.37','8.8.8.8','8.8.4.4','192.168.20.1']


for server in servers:

    result = os.system(f'ping -c 1 {server} > /dev/null')
    if result:
        print(f'IP адрес этого сервера {server} и он не пингуется!')
        
    else:
        print(f'IP адрес этого сервера {server} и он  пингуется!')
    
    
    
    