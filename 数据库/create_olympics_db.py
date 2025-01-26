import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('olympics.db')
cursor = conn.cursor()

# 创建Athletes表
cursor.execute('''
CREATE TABLE IF NOT EXISTS Athletes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sex TEXT NOT NULL,
    age INTEGER,
    height REAL,
    weight REAL,
    team TEXT,
    noc TEXT,
    discipline TEXT
)
''')

# 创建Coaches表
cursor.execute('''
CREATE TABLE IF NOT EXISTS Coaches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    noc TEXT,
    discipline TEXT
)
''')

# 创建Teams表
cursor.execute('''
CREATE TABLE IF NOT EXISTS Teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    noc TEXT,
    discipline TEXT
)
''')

# 创建Medals表
cursor.execute('''
CREATE TABLE IF NOT EXISTS Medals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rank INTEGER,
    team TEXT,
    gold INTEGER,
    silver INTEGER,
    bronze INTEGER,
    total INTEGER,
    rank_by_total INTEGER
)
''')

# 创建EntriesGender表
cursor.execute('''
CREATE TABLE IF NOT EXISTS EntriesGender (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discipline TEXT NOT NULL,
    female INTEGER,
    male INTEGER,
    total INTEGER
)
''')

# 创建AthleteEvents表
cursor.execute('''
CREATE TABLE IF NOT EXISTS AthleteEvents (
    id INTEGER PRIMARY KEY,
    name TEXT,
    sex TEXT,
    age INTEGER,
    height REAL,
    weight REAL,
    team TEXT,
    noc TEXT,
    games TEXT,
    year INTEGER,
    season TEXT,
    city TEXT,
    sport TEXT,
    event TEXT,
    medal TEXT
)
''')

# 提交更改并关闭连接
conn.commit()
conn.close()