a= 'sdfdsf'
b = 5


try:
    a = int(a)
    c = b/a
    print(c)
except ZeroDivisionError:
    print('не дели на 0 ')
except ValueError:
    print('не вводи строку')
except TypeError:
    print('ошибка типа данных')
except :
    print('неизвестная ошибка')

    
