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
#del mydict['aleksey']
mydict['aleksey'] = '+38779434631'
print('--------------------------------------------------------------------')
for i  in mydict:
    print(f'У абонента {i} номер {mydict[i]}')

i=''
    
print(f'В нашем словаре  {len(mydict)} записей!')

print(f'эта структура данных - {type(mydict)}')

yourdict = mydict.copy()


mydict.clear()






print('--------------------------------------------------------------------')

for i  in yourdict:
    print(f'У абонента {i} номер {yourdict[i]}')
i=''
    
print(f'В нашем словаре  {len(mydict)} записей!')
print(f'В вашем словаре  {len(yourdict)} записей!')


#yourdict = ''

print(yourdict.get('yleksey','номер не найден'))

dictirems = yourdict.items()
print(dictirems)
print(yourdict.keys())




