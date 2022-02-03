import time

mname=input('введите свое имя: ')
print('добрый день,',mname,'!')
print(f'Добрый день, {mname} !')
nodata=1

while nodata ==1:
    try:
        age=int(input('введите свой возраст: '))
        dopens=65-age
        print(f'Вам до пернсии {dopens} лет.')
        nodata=0
    except:
        print('повторите ввод данных')
        