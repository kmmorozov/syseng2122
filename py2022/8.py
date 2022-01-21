data_file = open('server-pass.txt','r')
server_dict = {}

for line in data_file:
    print(line)
    data_list = line.split(',')
    print(data_list)
    server_dict.update({data_list[0]:data_list})
    
print('-----------------------------------------------------')
print(server_dict.get('8.8.8.8')[2])
data_file.close()

    
    
    
    