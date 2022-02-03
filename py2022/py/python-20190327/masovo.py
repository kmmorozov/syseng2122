import paramiko 
#host = '10.1.6.209'
#user = 'root'
#secret = '123qaz'
#port = 22
servers = open('/home/prepod/servers.txt','r')
file = open('/home/prepod/mycom2.txt','r')
for server in servers:
    splserver=server.split(':')
    host = splserver[0]
    user = splserver[1]
    secret = splserver[2]
    port = splserver[3].strip()
    
    print(port)
    print(host)
    print(secret)
    print(user)
 
    
    file = open('/home/prepod/mycom2.txt','r')
 
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключение
    client.connect(hostname=host, username=user, password=secret, port=port)
     
    # Выполнение команды
    for line in file:
        print(line)
        try:
            stdin, stdout, stderr = client.exec_command(line)
            data = stdout.read()+stderr.read()
            print(data.decode())
        except:
            print('не вышло')
   
    file.close()

 
 

servers.close()