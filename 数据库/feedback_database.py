import sqlite3

# 连接到数据库
conn = sqlite3.connect('olympics.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL
)
''')

# 提交并关闭连接
conn.commit()
conn.close()
