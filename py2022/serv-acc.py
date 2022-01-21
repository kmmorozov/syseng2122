config = open('server-pass.txt','r')

for line in config:
    line = line.strip()
    split_line = line.split(',')
    #print(split_line)
    #print(type(split_line))
    print(f'К серверу {split_line[0]} нужно обращаться по порту {split_line[1]} с логином {split_line[2]} и паролем {split_line[3]} !')


config.close()
