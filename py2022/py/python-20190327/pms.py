import pymysql

file = open('/home/prepod/select.txt','w+')


try:
  
    db = pymysql.connect(host="10.1.6.87",user="py",passwd="123456",db="forpy")
    print('connect ok')
    cursor = db.cursor()
    cursor.execute('insert into telsprav values("kirill","morozov","m","79110271345")')
    print('insert ok')
    cursor.execute('select * from telsprav')
    result=cursor.fetchall()
    for el in result:
        #print(f'Ваше имя - {el[0]}, ваша фамилия - {el[1]}, а телефон: {el[3]} ')
        file.write(f'Ваше имя - {el[0]}, ваша фамилия - {el[1]}, а телефон: {el[3]} \n')
    
    file.close()
    
    


except:
    print('error')

