import mydb
db = mydb.Mydb()
print(db.conn.version)
sql = """
    SELECT *
    FROM member
    """
mem_list = db.get_select(sql)
# print(mem_list)
# insert_sql = """
#             INSERT INTO stocks(
#             seq, item_code, stock_name, close_price)
#             VALUES (
#             1, :1, :2, :3)
#             """
# cnt = db.fn_insert(insert_sql, [10000, '테스트', 1000.95])
# print(cnt)
# seq 사용할 시퀀스 생성 ( 1 ~ 999999 )
# 4일날 했던 https://m.stock.naver.com
# KOSPI의 전체 주가를 stocks 테이블에 insert 하시오
# 함수로 구현 fn_now_kospi_stock()
import json
import requests
from bs4 import BeautifulSoup
import csv
stock_data = []
def fn_now_kospi_stock():
    for j in range(1, 10):
        url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={0}&pageSize=50'.format(str(j))
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        jsonObj = json.loads(soup.text)
        stock_list = jsonObj['stocks']
        for stock in stock_list:
            # print(stock['itemCode'],stock['stockName'],stock['closePrice'])
            stock_data.append([stock['itemCode'], stock['stockName'], stock['closePrice']])
    for i in stock_data:
        insert_sql = """
                    INSERT INTO stocks(
                    seq, item_code, stock_name, close_price)
                    VALUES (
                    stock_seq.nextval, :1, :2, :3)
                    """
        cnt = db.fn_insert(insert_sql, [i[0], i[1], i[2]])
        print(cnt)
fn_now_kospi_stock()

















ㅋㅋ






