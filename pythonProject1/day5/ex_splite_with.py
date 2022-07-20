#with 사용
import sqlite3
conn = sqlite3.connect('./example.db')
# 사용이 끝나면 close를 하지 않아도 connection 종료
with conn:
    cur = conn.cursor()
    cur.execute("""SELECT * FROM stocks""")
    rows = cur.fetchall()
    for row in rows:
        print(row)