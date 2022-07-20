import sqlite3
# 조회
conn = sqlite3.connect('./example.db')
cur = conn.cursor()
cur.execute("""SELECT * FROM stocks""")
# 커서에서 바로 조회
for row in cur:
    print('1번째 : ', row)
print('='*100)
# cursor는 휘발성이기 때문에 출력 한 번 하면 뒤엔 안 나옴
# cur.execute("""SELECT * FROM stocks""")
for row in cur:
    print('2번째 : ', row)
cur.execute("""SELECT * FROM stocks""")
# Fetch 사용
# 1건
rows = cur.fetchone()
# 다건
rows = cur.fetchmany(3)
# 전체
rows = cur.fetchall()
print(rows)
conn.close()
