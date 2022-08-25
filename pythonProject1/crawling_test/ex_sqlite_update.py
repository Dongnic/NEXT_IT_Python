# 데이터 삽입
import sqlite3
conn = sqlite3.connect('naver_map_url.db')
cur = conn.cursor()
query = """
            update url_data
            set (cate_3, cate_mix) = (select replace(cate_3, ',', ''), 
                                        replace(cate_mix, ',', '')
                                        from url_data
                                        where cat3_mix like '%피자,%'
            where cata_mix like '%피자,%'
        """
cur.executemany(query)
print(cur.rowcount)
conn.commit()
conn.close()
