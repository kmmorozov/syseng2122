import requests
import re 

result = requests.get('https://ipap.ru')

#print(result.text)


result2 = re.findall(r'\w+@\w+\.\w+',result.text)
print(result2)


