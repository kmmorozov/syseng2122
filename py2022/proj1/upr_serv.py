import configparser
import paramiko


def get_connect_data(serv_file):
    server_dict = {}
    sf = open(serv_file,'r')
    for line in sf:
        data_list = line.split(':')
        server_dict.update({data_list[0]:data_list})
    sf.close()
    return server_dict


def get_commands(comm_file):
    commands = []
    cf = open(comm_file,'r')
    for line in cf:
        #print(line)
        commands.append(line.strip())
    cf.close()
    return commands
    


def get_path():
    config = configparser.ConfigParser()
    config.read('general.conf')
    ser_file = config['global']['servers']
    com_file = config['global']['commands']
    return ser_file, com_file

def push_commands_to_server(server,user,passwd,commands):
    print(server, user, passwd, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, '22', user, passwd, look_for_keys=False, allow_agent=False)
    #client.connect(server, '22' , 'root', '123qaz', compress=True)
    #client.connect(hostname, port, username, password, compress=True)
    #stdin, stdout, stderr = client.exec_command('ls /')
    for command in commands:
        stdin, stdout, stderr = client.exec_command(command)
        print('=================================================')
        for line in stdout:
            print('... ' + line.strip('\n'))
        print('=================================================')
        
    
    
    
    

if __name__ == '__main__':
    server_file, command_file = get_path()
    connect_data = get_connect_data(server_file)
    #print(connect_data)
    commands = get_commands(command_file)
    servers = connect_data.keys()
    for server in servers:
       username = (connect_data[server][1]).strip()
       password = (connect_data[server][2]).strip()
       push_commands_to_server(server.strip(),username,password,commands)
       
       
        
        
    
    
    
    
    
    

