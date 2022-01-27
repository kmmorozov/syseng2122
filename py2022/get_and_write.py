import pymysql


def get_db_data():
    connection = pymysql.connect(host='192.168.20.23', user='student', password='123456', database='pydb')
    cursor  = connection.cursor()
    cursor.execute('select * from tel_sprav;')
    result = cursor.fetchall()
    return result
    
def write_to_file(result):
    result_file = open('result.txt','w')
    for line in result:
        result_file.write(f'{line[0]};{line[1]};{line[2]};{line[3]};{line[4]};{line[5]}\n')
    result_file.close()
    
        
    
    
    

if __name__ == '__main__':
    result = get_db_data()
    write_to_file(result)
    

