import configparser

def get_connect_data(serv_file):
    server_dict = {}
    sf = open(serv_file,'r')
    for line in sf:
        data_list = line.split(':')
        server_dict.update({data_list[0]:data_list})
    return server_dict
        
    


def get_path():
    config = configparser.ConfigParser()
    config.read('general.conf')
    ser_file = config['global']['servers']
    com_file = config['global']['commands']
    return ser_file, com_file

    

if __name__ == '__main__':
    server_file, command_file = get_path()
    print(server_file)
    print(command_file)
    
    connect_data = get_connect_data(server_file)
    print(type(connect_data))
    print(connect_data)
    
    
    
    
    

