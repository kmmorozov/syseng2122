import pymysql


def get_data_from_file():
    data = []
    data_file = open('result.txt','r')
    for line in data_file:
        #print(line)
        split_line = line.split(';')
        #print(split_line)
        data.append(split_line)
    data_file.close()
    return data


def insert_data_to_mysql(data):
    connection = pymysql.connect(host='192.168.20.23', user='student', password='123456', database='pydb')
    cursor  = connection.cursor()
    for elem in data:
        cursor.execute(f'insert into tel_sprav values("{elem[0]}","{elem[1]}","{elem[2]}","{elem[3]}","{elem[4]}","{elem[5].strip()}");')
        print(f'insert into tel_sprav values("{elem[0]}","{elem[1]}","{elem[2]}","{elem[3]}","{elem[4]}","{elem[5].strip()}");')
    connection.commit()









if __name__ == '__main__':
    data = get_data_from_file()
    #print(data)
    insert_data_to_mysql(data)
    