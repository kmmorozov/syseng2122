import sqlite3

sqlite_connection = sqlite3.connect('sqlite_python.db')
cursor = sqlite_connection.cursor()
print("База данных создана и успешно подключена к SQLite")

cursor.execute('''create table tel_sprav(name text, surname text, thirdname text, sex text, phone text)''')

