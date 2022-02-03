mydict = {
    'kirill' : '89110271345',
    'aleksey' : '8951000001'
    }

sname = input('Введите имя абонента: ')

if sname in mydict:
    print('Телефон абонента ',mydict[sname])
else:
    print('Телефон не найден')
    added = int(input('Если хотите добавить нажните 1 в противном случае нажмите Enter '))
    if added   :
        aphone = input('Введите телефон абонента: ')
        mydict[sname] = aphone
        print(f'Для абонента {sname} Вы ввели телефон {mydict[sname]}')
        print('Спасибо1')
    else:
        print('Спасибо2')
       