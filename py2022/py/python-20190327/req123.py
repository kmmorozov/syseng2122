import requests
import re 

rhtml = requests.get('https://ipap.ru')
#print(rhtml.text)

print(rhtml)
myhtml = rhtml.text

#print(myhtml)

emailshab=re.compile('\w+@\w+[.]\w+')

phoneshab = re.compile('\d{11}|\d[-]\d+[-]\d+[-]\d+[-]\d+')

email = emailshab.findall(myhtml)
phone =  phoneshab.findall(myhtml)





print(email)
print(phone)