import sys  
#import math
#from math import sqrt as sq 
from math import sqrt
#import math 



try:
    a = float(input('Введите а: '))
    b = float(input('Введите b: '))
    c = float(input('Введите c: '))
except:
    print('Введены неверные данные, я зыкрываюсь ')
    #sys.exit('bad data')


if a==0:
    print('Это не квадратное уравнение!')

else:

    D = b*b - 4*a*c
    print(D)


    if D > 0:
        x1 = ((-b)+(sqrt(D)))/(2*a)
        x2 = ((-b)-(sqrt(D)))/(2*a)
        print(f'Уравнение  имеет два корня.  x1 = {x1}  x2={x2} .')
   
    elif D == 0:
        x = (-b)/(2*a)
        print(f'Уравнение имеет два совпадающих корня x1 = {x}  x2={x} ')
   
    else:
        print('Уравнение не имеет корней!')
        


