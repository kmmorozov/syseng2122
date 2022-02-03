from time import sleep

from os import listdir
from os.path import isfile, join

#from pathlib import Path

import ftplib
import smtplib

f=open(r'/home/student/SergeevPA/student.txt','r')

studentdir=r'/home/student/SergeevPA/WORK'
data=[line.strip().split(':') for line in f]
host='ftp.ipap.ru'

con=ftplib.FTP(host,data[0][1], data[0][2])
con.encoding='utf-8'
con.sendcmd('OPTS UTF8 ON')

gmail_user='stefanbelgrade1389@gmail.com'
gmail_password='123qaz123qaz'

sent_from=gmail_user
to='youremail@gmail.com'
subject='Videozapis\' zany\'atia'
email_text=f"Subject: {subject}\n\n Dlja vas byla vylozhena zapis po adresu ftp://{host}. Login {data[0][1]}, parol {data[0][2]}."

while True:
#     try:
    files = [spis for spis in listdir(studentdir) if isfile(join(studentdir,spis))]
    sleep(5)
    for name in files:
        fullname=join(studentdir,name)
        f=open(fullname,'rb')
        con.encoding='utf-8'
        con.sendcmd('OPTS UTF8 ON')
        send=con.storbinary('STOR ' + name, f)
        print(f'Передача файла {fullname} завершена')
    server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user,gmail_password)
    server.sendmail(sent_from,to,email_text)
    server.close()
    print('Email sent!')
#     except:
#         print('Передача не удалась')
#         con.close()