import time
import os 
file = open('/home/prepod/tel.txt','r')
for line in file:
    line = line.split(':')
    print(f'{line[0]} {line[1]}')
    cfile = open(f'/home/prepod/calls/{line[0]}.call','w')
    cfile.write(f'Channel: SIP/sipnet/{line[0]} \n')
    cfile.write(f'MaxRetries: 1 \n')
    cfile.write(f'RetryTime: 1 \n')
    cfile.write(f'WaitTime: 20 \n')
    cfile.write(f'Context: my \n')
    cfile.write(f'Extension: 9999')
    cfile.close
os.system('scp /home/prepod/calls/* root@10.1.6.131:/var/spool/asterisk/outgoing/')
