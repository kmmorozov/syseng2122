import requests
import re 

rhtml = requests.get('http://greenatom.ru')
#print(rhtml.text)

print(rhtml)
myhtml = rhtml.text
print(myhtml)

