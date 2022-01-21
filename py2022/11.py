import os
log_file = open('log.txt','r')
bad_ip = {}

for  line in log_file:
    #print(line)
    result = line.find('Failed password')
    #print(result)
    if result >= 0 :
        #print(line)
        data_list = line.split()
       # print(data_list[10])
        #os.system(f'iptables -A INPUT -s {data_list[10]}')
        bad_ip.update({data_list[10]:'ok'})

#print(bad_ip.keys())

for key in  bad_ip:
    #print(key)
    os.system(f'iptables -A INPUT -s {key} -j DROP')

        