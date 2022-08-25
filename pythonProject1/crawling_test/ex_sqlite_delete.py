# 데이터 삽입
import sqlite3
conn = sqlite3.connect('naver_map_url.db')
cur = conn.cursor()
query = """
            delete from url_data
            where rowid < ?
            and naver_map_url is null
        """
cur.execute(query, "670")
print(cur.rowcount)
conn.commit()
conn.close()
