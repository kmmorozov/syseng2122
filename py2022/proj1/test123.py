import paramiko

 # Информация о сервере, имя хоста (IP-адрес), номер порта, имя пользователя и пароль

hostname = "192.168.20.22"
port = 22
username = "root"
password = "123qaz"
    
 # Создать объект SSH  
client = paramiko.SSHClient()
 # Автоматически добавлять стратегию, сохранять имя хоста сервера и ключевую информацию
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 # подключиться к серверу
client.connect(hostname, port, username, password, compress=True)

 # Выполнить команду linux
stdin, stdout, stderr = client.exec_command('ls /')

for line in stdout:
    print('... ' + line.strip('\n')) 
#or
print(stdout.readlines())