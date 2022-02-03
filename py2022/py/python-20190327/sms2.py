import os

soobsh='ИПАП- центр повышение квалификации и профпереподготовки специалистов I'
soobsh2='T и СТРОИТЕЛЬНОГО направления приветствует Вас!'
soobsh3='Клиентская служба работает:пн-пт с 9:00-18:00 по тел.8(800) 551-01-42'

number='89110271345'



def smssend(text,number):
    status=os.system(f'echo "{text}" | gammu sendsms  TEXT {number} -unicode')
    return(status)

result=smssend(soobsh,number)

print(result)

result=smssend(soobsh2,number)

print(result)

result=smssend(soobsh3,number)

print(result)