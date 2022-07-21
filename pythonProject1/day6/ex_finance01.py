# pip install -U finance-datareader
import FinanceDataReader as fdr

# 한국거래소 상장종목 전체
import pandas as pd

df_krx = fdr.StockListing('KRX')
print(df_krx.head())
df = df_krx[["Symbol", "Market", "Name"]]
print(df.head())
samsung_all = fdr.DataReader('005930')
samsung_2021 = fdr.DataReader('005930', '2021')
print(samsung_all.head())
print(samsung_2021.head())

KOSPI = df_krx[df_krx['Market'].str.contains('KOSPI')]
writer = pd.ExcelWriter('kospi.xlsx', engine='openpyxl')
KOSPI.to_excel(writer, sheet_name='Sheet1')
writer.close()
print(samsung_all.describe())
print(samsung_2021.describe())