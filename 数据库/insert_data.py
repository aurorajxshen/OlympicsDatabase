import pandas as pd
import sqlite3
import os

# 文件路径
base_path = 'D:\\徐瑞阳中传\\大二下\\信息设计\\小组作业'

files = {
    'Athletes': os.path.join(base_path, 'Athletes.xlsx'),
    'Coaches': os.path.join(base_path, 'Coaches.xlsx'),
    'Teams': os.path.join(base_path, 'Teams.xlsx'),
    'Medals': os.path.join(base_path, 'Medals.xlsx'),
    'EntriesGender': os.path.join(base_path, 'EntriesGender.xlsx'),
    'athlete_events': os.path.join(base_path, 'athlete_events.csv')
}

# 连接到SQLite数据库
conn = sqlite3.connect('olympics.db')

# 读取并插入每个文件的数据到相应的数据库表中
for table_name, file_path in files.items():
    if file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)

    # 打印数据框列名和数据
    print(f"Inserting into {table_name} with columns: {df.columns.tolist()}")

    # 将DataFrame插入到SQL表中
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# 提交更改并关闭连接
conn.commit()
conn.close()
