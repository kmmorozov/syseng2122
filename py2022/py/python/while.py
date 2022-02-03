import time
from time import sleep


a = 10
b=1
while b:
    
    a = a - 1
    if a == 5:
        print('не  выводим 5 ')
        continue
    
    print(a)
    sleep(0.001)
else:
    print('дно достигнуто')
    