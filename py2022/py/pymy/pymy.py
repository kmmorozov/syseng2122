import pymysql

#date = input('Введите дату: ')
#user = input('Введите имя: ')
#service = input('Введите службу: ')
#event = input('Введите событие: ' )


try: 
    db = pymysql.connect('10.1.6.190','student','12345678','test')
    cursor=db.cursor()
    print('connect OK')
    conn=1
except:
    print('Not connect')

if conn:
    try:
       file=open('log.txt')
       for line in file:
           sline = line.split()
           date = sline[0]
           user = sline[1]
           service = sline[2]
           event = sline[3]
           print('строка прочитана')
           ins=str(f"insert into logs(date,user,service,event)   values('{date}','{user}','{service}','{event}');")
           cursor.execute(ins)
           print('insert ok')
           
    except:
        print('нет такого файла')
    
       #ins = str('select * from logs')
    
    print('ok')