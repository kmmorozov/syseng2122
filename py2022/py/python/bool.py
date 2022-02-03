
try:
    s='ава'
    if s :
        print('все ок ')
        x = 1/0
    else:
        print(' не вcе ок ')
except ValueError :
    print('ошибка типа данных ')
except ZeroDivisionError :
    print('на 0 делить нельзя ')
except :
    print('чето хз')