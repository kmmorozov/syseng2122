mydict = {
    'kirill' : '891102713451',
    'aleksey' : '8951000001',
    'ivan' : '89110546545',
    'alex' : '895345301',
    'sergey' : '89116781345',
    'vladimir' : '8951006781',
    'nikita' : '89110245645',
    'nikolay' : '895145601'
    }

##print(mydict.setdefault('yaroslav','89991234567'))
##
##for i  in mydict:
##    print(f'У абонента {i} номер {mydict[i]}')
##

yourdict = {
    'kirill' : '89110271345',
    'a1' : '891105654455',
    'a2' : '895105465475',
    'a3' : '891105453452',
    'a4' : '895348767874',
    'a5' : '891167898932',
    'a6' : '895123423454',
    'a7' : '891102423424',
    'a8' : '895165757745'
    }
    
yourdict.update(mydict)


for i  in yourdict:
    print(f'У абонента {i} номер {yourdict[i]}')

print(yourdict.values())
