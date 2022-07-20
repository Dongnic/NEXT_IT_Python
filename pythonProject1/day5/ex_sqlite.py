import sqlite3
# 임시 메모리 DB 접속
# conn = sqlite3.connect(':memory:')

# 파일형태로 저장
conn = sqlite3.connect('example.db')
print(sqlite3.version)
print(conn)
# 데이터 타입 (동적타입)
# NULL, INTEGER, REAL, TEXT, BLOB
cur = conn.cursor()
cur.execute(""" CREATE TABLE stocks(
                      data text
                    , trans text
                    , symbol text 
                    , qty real
                    , price real
                )        
""")