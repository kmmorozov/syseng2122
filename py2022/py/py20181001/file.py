import re
pattern = re.compile(r'Failed password',re.I)
ippat = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

f = open('/home/prepod/test.log')
for line in f:
    match = pattern.findall(line)
    #print(len(match))
    #print(match)
    if len(match) == 1:
       print('ok')
       zloip = ippat.findall(line)
       print(zloip[0])
       
       