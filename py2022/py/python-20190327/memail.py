import smtplib

gmail_user = 'monitorzabb123@gmail.com'  
gmail_password = 'GYxjB94rEs9UEQd'

sent_from = gmail_user  
to = ['kmmorozov@gmail.com']  
subject = 'PING LOSS'  
body = 'test'

email_text = "Subject: server nedostupen  \n\n  5 ping loss "

print(email_text)




try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:  
    print('Something sent wrong...')

