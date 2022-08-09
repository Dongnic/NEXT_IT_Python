import FinanceDataReader as fdr
import pandas as pd

def fn_get_stock(p_code, p_start, p_end):
    # 삼성 005930
    df_all = fdr.DataReader(p_code, p_start, p_end)
    # 인덱스에 있던 데이터를 -> 컬럼으로
    # 인덱스 자리를 0 ~
    df = df_all.reset_index()
    seq = df['Date'].dt.strftime('%Y-%m-%d')
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Change']].astype(str)
    df['Date'] = seq
    file_nm = '{0}_{1}_{2}.xlsx'.format(p_code, p_start.replace('-', ''), p_end.replace('-', ''))
    writer = pd.ExcelWriter(file_nm, engine='openpyxl')
    df.to_excel(writer, 'Sheet1')
    writer.save()
