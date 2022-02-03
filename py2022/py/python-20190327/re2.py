import re 
shab1 = re.compile('AV')
shab2 = re.compile('community',re.I)


result = shab1.findall('AV Analytics Vidhya AV')
print(result)
result2 = shab2.findall('AV is largest analytics Community of India')
print(result2)
