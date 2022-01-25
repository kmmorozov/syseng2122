import datetime


logfile = open('log.txt','a')
try:
    f1 = open('commands.txt','r')
    for line in f1:
        print(line)
    logfile.write(f'{str(datetime.datetime.now())} файл commands.txt открыли и прочитали \n')
    f1.close()
    logfile.write(f'{str(datetime.datetime.now())} файл commands.txt успешно закрыли \n')
except:
    print('error!!!')
    logfile.write(f'{str(datetime.datetime.now())} файл commands.txt не удалось прочитать или закрыть \n')
    

logfile.close()


# 
#f2 = open('general.conf','r')
# 
# for line in f2:
#     print(line)
# 
# f3 = open('servers.txt','r')
# 
# for line in f3:
#     print(line)
#     