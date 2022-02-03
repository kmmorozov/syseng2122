import re

str = 'Moe imya - Kirill Morozov phone: 89110271345 e-mail: Kmmorozov@gmail.com ivanivanov@gmail.com  site: www.nadejnei.net'

regexp = '\w+@\w+[.]\w+'

#regexp = ' ' 

## match  от начала стоки
##substr = re.match(regexp,str)
##print(substr.group(0))
##print(substr.start())
##print(substr.end())

## search - по строке
##
subsrt = re.findall(regexp,str,re.I)
print(subsrt)

#subsrt = re.findall(regexp,str,re.I)
#print(type(subsrt))

#substr = re.split(regexp,str)

#print(substr)

#date = '2018-05-14-19-11'

#ss = re.split('-',date,maxsplit=3)
#print(ss)

spath = '/etc/log/messages'

spath = re.subn('etc','var',spath)[0]

print(spath)










