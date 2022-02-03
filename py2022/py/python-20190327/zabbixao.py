import os
import time
import smtplib
import requests



gmail_user = 'stefanbelgrade1389@gmail.com'  
gmail_password = '123qaz123qaz'

sent_from = gmail_user  
to = ['kmmorozov@gmail.com']  
subject = 'PING LOSS'  
body = 'test'

email_text = "Subject: server nedostupen  \n\n  5 ping loss "



errcount = 0 


while 1:
    time.sleep(10)   
   # testping = os.system('ping angryoffers.info -c 1  > /dev/null')
    try:
        testping=requests.get('http://angryoffers.info').ok
    except:
        testping=False
    print(testping)
    if  not testping:
        errcount = errcount+1
        print('not ok')
        print(errcount)
        if errcount == 5:
            print('оправляем письмо админу')
            try:  
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, email_text)
                server.close()

                print('Email sent!')
            except:  
                print('Something went wrong...')


            
        
    else:
        errcount=0
        print('ok')
        print(errcount)
        
        
        
    