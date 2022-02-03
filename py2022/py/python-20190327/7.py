
nodata = True

while nodata:
    try:
        a=float(input('Введите любое число: '))
        nodata = False
    except:
        print('bad data')


print(f'Вы ввели {a}')
        


