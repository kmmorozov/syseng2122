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

sel = str('select * from logs;')
cursor.execute(sel)

for row in cursor.fetchall():
   if row[2]=='mkm':     
       print(f'В {row[1]} Кирилл работал c {row[3]} ')