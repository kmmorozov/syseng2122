#!/usr/local/bin/python3.6
import re
import os
from time import sleep


def fw():
    f = open('/var/log/secure','r')
    try:
        w = open('/root/log.txt','w')
    except:
        os.system('touch /root/log.txt')
        w = open('/root/log.txt','w')

    for str in f:

        regexp = 'Failed password'
        try: 
            twork = re.search(regexp,str,re.I).group(0)
            ip = re.findall('\d+[.]\d+[.]\d+[.]\d+',str)
            print(ip[0])
            #print(f'/usr/sbin/iptables -A INPUT  -s {ip[0]} -j DROP')
            fs =f'/usr/sbin/iptables -A INPUT  -s {ip[0]} -j DROP'
            os.system(fs)
            w.write(fs +'\n')
            
            
            
        except:
            print('нет совпадений')

    f.close()
    w.close()


while 1:
    fw()
    sleep(5)
    
    