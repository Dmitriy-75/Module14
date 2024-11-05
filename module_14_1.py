         # Задача "Первые пользователи":

import sqlite3

# Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
# Создайте объект курсора и выполните следующие действия при помощи SQL запросов:

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число
# balance - целое число (не пустой)

cursor.execute('''
CREATE TABLE IF NOT EXISTS User(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Заполните её 10 записями:
# User1, example1@gmail.com, 10, 1000
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 1000

for i in range(1, 11):
    cursor.execute("INSERT INTO User(username, email, age, balance ) VALUES(?,?,?,?)",
                   (f'User{i}', f' example{i}@gmail.com', f'{i*10}', '1000'))

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:

for i in range(1, 11, 2):
    cursor.execute("UPDATE  User SET balance=? WHERE id=?",(500, i))

# Удалите каждую 3ую запись в таблице начиная с 1ой:
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM  User  WHERE id=?", (i,))

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

cursor. execute("SELECT username, email, age, balance FROM User WHERE age!=?", ('60',))
users = cursor. fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()