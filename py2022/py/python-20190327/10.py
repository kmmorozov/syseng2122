dic = {'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'777':'Kirill'}
print(dic['1'])
print(dic)
print(dic['777'])
print('4' in dic)
print('77' in dic)
#print(type(list(dic)))
del dic['2']
print(dic)
dic2=dic.copy()
print(dic2)
print(len(dic2))
print(dic2.items())
print(dic2.keys())
print(dic2.values())
print(dic2)
print(dic2.pop('4','NoKey'))

print(dic2)
#print(dic2.popitem())
#print(dic2.popitem())
print(dic2)
print(dic2.setdefault('6','fsdfgdfgdf'))
#print(dic2.setdefault('6','six'))
print(dic2)
#print(dic2.setdefault('123','klfgsklgj'))
print(dic2.setdefault('6','seven'))
print(dic2)
dic.update(dic2)
print(dic)





ts = {'kirill':'123456','stefan':'123457','fedor':'654321','max':'234553','kirill':'555555'}
ts2 ={'kirill':'777777'}
#
#
print(ts)
ts.update(ts2)
print(ts)






