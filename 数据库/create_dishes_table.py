import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('olympics.db')
cursor = conn.cursor()

# 创建SignatureDishes表
cursor.execute('''
CREATE TABLE IF NOT EXISTS SignatureDishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    city TEXT NOT NULL,
    cuisine TEXT NOT NULL,
    dishes TEXT NOT NULL
)
''')

# 提交更改并关闭连接
conn.commit()
conn.close()
