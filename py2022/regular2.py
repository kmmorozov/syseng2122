import re

st = 'Menya zovut Kirill 8-911-027-13-45 Morozov moy telefon 89110271345, moya pochta 5 kmmo7rozov@gmail.com fjskfjj@ya.ru'


result = re.findall(r'\d-\d+-\d+-\d+-\d+|\d+',st)


result2 = re.findall(r'\w+@\w+\.\w+',st)

result3  = re.sub(r'\w+@\w+\.\w+','kirill@ipap.ru',st)


print(result)

print(result2)

print(result3)