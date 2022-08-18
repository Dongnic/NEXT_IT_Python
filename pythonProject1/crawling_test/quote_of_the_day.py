# 유동준
from mydb import Mydb
import requests
from bs4 import BeautifulSoup
db = Mydb()

quote_list = []

def fn_crawling_quote():
    cnt = 0
    for i in range(16348, 16349):
        url = 'https://saramro.com/quotes/{0}'.format(str(i))
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(soup.prettify())
        content = soup.select_one('#bo_v_con')
        if content:
            content1 = str(content.text)
            content2 = str(content)
            # print(content)
            text = content1.split('-')[0].strip()
            writer = content2.split('-')[1].split('<')[0].strip()
            if writer:
                text = text.replace('\r', '')
                writer = writer.replace('\r', '')
                print(text)
                print(writer)
                print(len(writer), len(text))
                insert_sql = """
                                INSERT INTO quotes
                                VALUES (
                                seq_quotes.nextval, :1, :2)
                            """
                if len(writer) < 30 and len(text) < 333:
                    cnt += db.fn_insert(insert_sql, [writer, text])
                    print(cnt, '건 삽입')
    print('총', cnt, '건 삽입')


def fn_insert_quote():
    cnt = 0
    for i in quote_list:
        insert_sql = """
                    INSERT INTO quotes
                    VALUES (
                    seq_quotes.nextval, :1, :2)
                    """
        cnt += db.fn_insert(insert_sql, [i[0], i[1]])
        print(cnt, '건 삽입')
    print('총', cnt, '건 삽입')


fn_crawling_quote()
# fn_insert_quote()