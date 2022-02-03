zoo = ('питон','медведь','сова')
print('В зоопарке ', len(zoo), ' зверя')
print(f'В зоопарке  {len(zoo)}  зверя')
zoo1 = ('удафф','опоссум')

allzoo =  zoo + zoo1
sovsemall = 'ворона','корова','собака',allzoo
print(sovsemall) 
print(sovsemall[3][2])
print(len(sovsemall))
try :
    #del sovsemall[1]
    #print(sovsemall)
    b = 10/'pfsdfs'
    
#except TypeError :
 #   print('ошибка типа данных')
except ZeroDivisionError :
    print('на 0 делить нельзя')
except:
    print('какая-то ошибка')
    
    
    
    
    
    