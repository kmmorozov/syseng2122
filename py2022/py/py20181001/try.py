a=10
b=0
try :
    c = b + m

except ZeroDivisionError:
    print('на 0 не делим ')
except NameError:
    print('Переменная не определена')
except:
    print('неизвестная ошибка')