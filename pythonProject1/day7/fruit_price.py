# 유동준
from day5.mydb import Mydb
import json
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
db = Mydb()
fruit_data = []
today_price_val = []
reg_week_val = []


def fn_price():
    url = 'https://nongup.gg.go.kr/data/62?tab=3&search_type=after&search_item=0014'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())
    table_tbody = soup.select_one('.des_table tbody')
    # print(table_tbody)
    trs = table_tbody.find_all('tr')
    if trs:
        for tr in trs:
            reg_date = tr.select_one("td:nth-child(1)").text
            today_price = tr.select_one("td:nth-child(2)").text
            week_price = tr.select_one("td:nth-child(3)").text
            year5_avr = tr.select_one("td:nth-child(4)").text
            week_price_cp = tr.select_one("td:nth-child(5)").text
            year5_avr_cp = tr.select_one("td:nth-child(6)").text
            # print(reg_date, today_price, week_price, year5_avr, week_price_cp, year5_avr_cp)
            fruit_data.append([reg_date, today_price, week_price, year5_avr, week_price_cp, year5_avr_cp])
            print(fruit_data)


def fn_insert_fruit():
    cnt = 0
    for i in fruit_data:
        insert_sql = """
                    INSERT INTO fruitPrice(
                    seq, reg_date, today_price, week_price, year5_avr, week_price_cp, year5_avr_cp)
                    VALUES (
                    fruit_seq.nextval, to_date(:1,'YYYY-MM-DD'), :2, :3, :4, :5, :6)
                    """
        cnt = db.fn_insert(insert_sql, [i[0], i[1], i[2], i[3], i[4], i[5]])
    print(cnt)


def fn_get_today_price():
    select_price_sql = """
                 SELECT today_price
                 FROM fruitPrice
                 ORDER BY seq desc
                 """
    today_price_result = db.get_select(select_price_sql)
    for item in today_price_result:
        temp1 = ''.join(item).replace(",", "")
        today_price_val.append(int(temp1))


def fn_get_reg_week():
    select_date_sql = """
                 SELECT reg_date
                 FROM fruitPrice
                 ORDER BY seq desc
                 """
    reg_week_result = db.get_select(select_date_sql)
    for item in reg_week_result:
        result = item[0].strftime("%Y-%m-%d")
        reg_week_val.append(result)


# fn_price()
# fn_insert_fruit()
fn_get_reg_week()
fn_get_today_price()

x = np.arange(len(today_price_val))
plt.bar(x, today_price_val)
plt.xticks(x, reg_week_val)

plt.show()