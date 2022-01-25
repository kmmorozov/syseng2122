import logging

logfile = 'log_1.log'

log = logging.getLogger("my_log")
log.setLevel(logging.DEBUG)
FH = logging.FileHandler(logfile)
basic_formater = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
FH.setFormatter(basic_formater)
log.addHandler(FH)


try:
    f1 = open('commands.txt','r')
    log.info("файл открыли")
    for line in f1:
        print(line)
    log.info("файл прочитали")
    f1.close()
    log.info("файл закрыли")

    
except:
    print('error!!!')
    log.error("какая-то ошибка!!!")
    log.critical('а-а-а-а Все пропало!!!!')

    
    



