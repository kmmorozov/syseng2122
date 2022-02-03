#import math
from math import sqrt 
# 	5x^2-23x+8=0
#	a     b  c

print('решаем кв ур')


a=int(input('Введите a: '))
b=int(input('Введите b: '))
c=input('Введите c: ')
c=int(c)
    

D=b**2-4*a*c

print(f'Дискриминант {D}')
#Ds - корень  из дискриминанта

#Ds = math.sqrt(D)
#Ds = sqrt(D)
#print(f'корень из дискриминанта {Ds}')

if D > 0:
    Ds = sqrt(D) # если D больше нуля извлекаем корень

    x1 = (-b + Ds)/(2 * a) #первый корень 
    x2 = (-b - Ds)/(2 * a) #второй корень
    
    print(f'первый корень уравнения {x1}')
    print(f'второй  корень уравнения {x2}')

elif D == 0:
    x1 = (-b)/(2 * a)
    print(f'единственный  корень уравнения {x1}')

else:
    
    print('Уравнение не имеет корней')
    
    
    
    
    
    
    
    











