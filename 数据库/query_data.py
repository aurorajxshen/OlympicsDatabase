import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('olympics.db')
cursor = conn.cursor()

# 查询Athletes表
cursor.execute('SELECT * FROM Athletes')
athletes = cursor.fetchall()
print("Athletes:")
for athlete in athletes:
    print(athlete)

# 查询Coaches表
cursor.execute('SELECT * FROM Coaches')
coaches = cursor.fetchall()
print("\nCoaches:")
for coach in coaches:
    print(coach)

# 查询Teams表
cursor.execute('SELECT * FROM Teams')
teams = cursor.fetchall()
print("\nTeams:")
for team in teams:
    print(team)

# 查询Medals表
cursor.execute('SELECT * FROM Medals')
medals = cursor.fetchall()
print("\nMedals:")
for medal in medals:
    print(medal)

# 查询EntriesGender表
cursor.execute('SELECT * FROM EntriesGender')
entries_gender = cursor.fetchall()
print("\nEntriesGender:")
for entry in entries_gender:
    print(entry)

# 查询AthleteEvents表
cursor.execute('SELECT * FROM AthleteEvents')
athlete_events = cursor.fetchall()
print("\nAthleteEvents:")
for event in athlete_events:
    print(event)

# 关闭连接
conn.close()
