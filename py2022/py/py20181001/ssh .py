import paramiko 

host = '10.1.6.190'
user = 'root'
secret = '123456'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('ls -l')
data = stdout.read() + stderr.read()
client.close()
