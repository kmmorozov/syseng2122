from time import sleep
import os

ok = 0
ko = 0 

while True:
    sleep(5)
    print('!!!')
    result = os.system('ping -c 1 192.168.20.37 > /dev/null')
    if result :
        ko = ko + 1
        if ko == 10:
            print('отправляю sms - сервер 192.168.20.37 не доступен!!!')
    elif ko > 0 and  result == 0:
        ko = 0
        print('отправляю sms - сервер 192.168.20.37 доступен!!!')
        
        
        