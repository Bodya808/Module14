import sqlite3

connect = sqlite3.connect('not_telegram.db')
cursor = connect.cursor()

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
sum_balances = cursor.fetchone()[0]

if total_users > 0:
    average_balance = sum_balances / total_users
else:
    average_balance = 0

print(f"Средний баланс всех пользователей: {average_balance}")

connect.commit()
connect.close()
