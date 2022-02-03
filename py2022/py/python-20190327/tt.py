a=10
b=2


try:
    c=a/b
    print(c)
    
    
except ZeroDivisionError:
    
    print('на 0 делить нельзя ')

except NameError:
    print('переменная не определена')

except TypeError:
    print('ошибка типа переменной')

except:
    print('хз ошибка ')


print('сл действие ')

