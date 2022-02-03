import sqlite3
 
conn = sqlite3.connect("users.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
 
# Создание таблицы
# cursor.execute("""CREATE TABLE users(name text, phone text, groups text)
#              """)

mname = 'kirill1'
cursor.execute(f"""INSERT INTO users
                  VALUES ('{mname}', '89110271345', 'admins')""")
conn.commit()

data = cursor.execute('select * from users')
print(data.fetchall())


