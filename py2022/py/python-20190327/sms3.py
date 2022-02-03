import os
import sys


#soobsh=input('Введи текст sms:')
#number=input('Введи номер:')

soobsh = sys.argv[1]
number = sys.argv[2]


def smssend(text,number):
    status=os.system(f'echo "{text}" | gammu sendsms  TEXT {number} -unicode')
    return(status)

result=smssend(soobsh,number)
print(result)
