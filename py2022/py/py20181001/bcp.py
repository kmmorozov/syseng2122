import os
## делаем резаервную копию

adir = input('Введите источник:')
apath = input('Введите путь: ')
aname = input('Введите имя архива: ')
print(f'tar czvf {apath}{aname}.tar.gz {adir}')
result=os.system(f'tar czvf {apath}{aname}.tar.gz {adir}')
print(str(result))