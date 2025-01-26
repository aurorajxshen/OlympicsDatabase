import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('olympics.db')
cursor = conn.cursor()

# 查询数据
cursor.execute('SELECT * FROM SignatureDishes')
rows = cursor.fetchall()

# 打印数据
for row in rows:
    print(row)

# 关闭连接
conn.close()
