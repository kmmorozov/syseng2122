import pymysql
db=pymysql.connect('127.0.0.1','root','123456','test')
cursor = db.cursor()
a='Morozov'
b='Kirill'
c='Mikhailovich'
ins = str(f"insert into test2 values('{a}','{b}','{c}')")
cursor.execute(ins)

ins2 = str("select * from test2;")

cursor.execute(ins2)

data = cursor.fetchall()

print(type(data))
print(data[5][0])

for line in data:
    print(type(line))
    
    print(line)


