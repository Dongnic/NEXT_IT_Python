# 데이터 삽입
import sqlite3
conn = sqlite3.connect('naver_map_url.db')
cur = conn.cursor()
query = """
            select rowid from url_data
        """
cur.execute(query)
print(cur.rowcount)
# 전체
rows = cur.fetchall()
print(rows)
conn.close()
