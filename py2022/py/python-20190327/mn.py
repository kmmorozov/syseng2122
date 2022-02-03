mname=input('введите свое имя: ')
print('добрый день,',mname,'!')
print(f'Добрый день, {mname} !')
try:
    age=int(input('введите свой возраст: '))
    dopens=65-age
    print(f'Вам до пернсии {dopens} лет.')
except:
    print('Возраст введен не числом')


