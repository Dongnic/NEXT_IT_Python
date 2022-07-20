import  cx_Oracle

class Mydb:

    def __init__(self):
        self.conn = None
        self.get_connection()

    def __del__(self):
        try:
            if self.conn:
                print('conn finish')
                self.conn.close()
        except Exception as e:
            print(str(e))

    def get_connection(self):
        self.conn = cx_Oracle.connect('java', 'oracle', 'localhost:1521/XE', encoding = 'UTF-8')
        return self.conn

    def get_select(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_select_param(self, query, param):
        cur = self.conn.cursor()
        cur.execute(query, param)
        rows = cur.fetchall()
        cur.close()
        return rows

    # 한 건
    def fn_insert(self, query, param):
        cur = self.conn.cursor()
        cur.execute(query, param)
        cnt = cur.rowcount
        cur.close()
        self.conn.commit()
        return cnt

    # 여러건
    def fn_insert_list(self, query, param):
        cur = self.conn.cursor()
        cur.executemany(query, param)
        cnt = cur.rowcount
        cur.close()
        self.conn.commit()
        return cnt

if __name__ == '__main__':
    print('conn text')
    db = Mydb()
    conn = db.get_connection()
    print(conn.version)