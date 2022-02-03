import pymysql

db = pymysql.connect(host="10.1.6.87",user="py",passwd="123456",db="forpy")

cursor=db.cursor()


file = open('/home/prepod/students.csv','r')

for line in file:
   # print(line.split(';'))
    line=line.split(';')
    ins=f'insert into telsprav values("{line[0]}","{line[1]}","{line[2]}","{line[3].strip()}")'
   # print(ins)
    cursor.execute(ins)
    
    