

#mname=input('Введите свое имя: ')

try:
    mage=float(input('Введите свои возраст: '))
except ValueError:
    print('Вы ввели неверные данные, введите возраст числом')
    mage=int(input('Введите свои возраст: '))

newage=mage+10

print('Привет,',mname,',через 10 лет вам будет', newage,'.')

print(f'Привет, {mname}, через 10 лет Вам будет {newage}.')



