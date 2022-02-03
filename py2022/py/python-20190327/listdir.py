import os

filelist=os.listdir('/etc')

## /home/prepod/bcp

#os.system('cp /etc/resolv.conf /home/prepod/bcp')


#print(os.listdir('/home/prepod/bcp'))

for i in filelist:
    os.system(f'cp -r /etc/{i} /home/prepod/e1')
    



