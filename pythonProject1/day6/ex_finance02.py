import FinanceDataReader as fdr
import pandas as pd
# 그래프 기능 라이브러리
# pip install matplotlib
import matplotlib.pyplot as plt

# 삼성전자 종가기준 그래프
samsung_all = fdr.DataReader('005930')
samsung_all['Close'].plot()
plt.show()

# 테슬라 종가기준 그래프
TSLA = fdr.DataReader('TSLA')
TSLA['Close'].plot()
plt.show()
