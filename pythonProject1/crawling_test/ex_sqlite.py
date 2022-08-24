import sqlite3
# 임시 메모리 DB 접속
# conn = sqlite3.connect(':memory:')

# 파일형태로 저장
conn = sqlite3.connect('naver_map_url.db')
# 데이터 타입 (동적타입)
# NULL, INTEGER, REAL, TEXT, BLOB
cur = conn.cursor()
cur.execute(""" CREATE TABLE naver_map_url(
                     url text
                )        
""")