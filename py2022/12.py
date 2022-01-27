import pymysql
 
#con = pymysql.connect('192.168.20.23', 'student', '123456', 'pydb')

connection = pymysql.connect(host='192.168.20.23', user='student', password='123456', database='pydb')

cursor  = connection.cursor()

# insert into tel_sprav values('1','Kirill','Morozov','M','m','89110271345');


cursor.execute('insert into tel_sprav values("1","Kirill","Morozov","M","m","89110271345");')

connection.commit()

result = cursor.fetchall()

cursor.execute('select * from tel_sprav;')

result = cursor.fetchall()

for line in result:
    print(line)







