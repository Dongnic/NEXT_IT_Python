from day5.mydb import Mydb
import pandas as pd
db = Mydb()

# 김씨만 검색
mem_table = pd.read_sql(("""
                        SELECT * 
                        FROM member 
                        WHERE mem_name like '%'||:nm||'%' 
                        """), con=db.conn, params={"nm": "김"})
print(mem_table.head())
# 데이터 접근 iloc[행 인덱스, 열 인덱스], loc[행 인덱스]
print(mem_table.iloc[0, 2])
print(mem_table.loc[0])
print(mem_table.columns)
# iterrows : 행 단위로 출력
for i, row in mem_table.iterrows():
        print(i+1, '번째', row['MEM_NAME'])