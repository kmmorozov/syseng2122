import paramiko 
 
host = '10.1.6.50'
user = 'root'
secret = '123qaz'
port = 22
 
client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Подключение
client.connect(hostname=host, username=user, password=secret, port=port)
 
# Выполнение команды
stdin, stdout, stderr = client.exec_command('reboot')




 
# Читаем результат
data = stdout.read()+stderr.read()
print(data.decode())
 
client.close()