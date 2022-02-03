mydict = {
    'kirill' : '89110271345',
    'aleksey' : '8951000001',
    'ivan' : '89110546545',
    'alex' : '895345301',
    'sergey' : '89116781345',
    'vladimir' : '8951006781',
    'nikita' : '89110245645',
    'nikolay' : '895145601'
    }
##
##print(mydict.pop('nikita','Элемент не найден '))
##
##
##try:
##    print(mydict.pop('nikita'))
##except KeyError:
##    print('Элемент не найден')
##
##print(mydict.pop('nikita','Элемент не найден '))

#print(type(mydict.popitem()))
try:
    while 1:
        print(f'{mydict.popitem()[0]} ---- {mydict.popitem()[1]}')
   
except:
    print('ошибка')
##print(mydict.popitem())
##print(mydict.popitem())
##print(mydict.popitem())
##print(mydict.popitem())
##print(mydict.popitem())
##print(mydict.popitem())
##print(mydict.popitem())








