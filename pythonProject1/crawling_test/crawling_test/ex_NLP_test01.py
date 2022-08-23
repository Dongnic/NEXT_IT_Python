import csv
import pandas as pd
from displayfunction import display
import numpy

print(numpy.__version__)
sur = pd.read_csv('inter.csv')
print(sur.info())
sur.columns = ["date", "comment", "satisfaction"]

print(sur.info())
print(sur.shape)
display(sur.head())
# 앞 뒤 공백 제거
sur['comment'] = sur['comment'].str.strip()
# 결측치 확인(공백말고 아예 빈 값은 결측치로 판단)
print("OUT[2] \n", sur.isna().sum())
# 결측치 제거
sur = sur.dropna(how='any')
print("OUT[3] \n", sur.isna().sum())
# 정규표현식(Regular Expression)
# 괄호 및 안에 내용 제거
sur['comment'] = sur['comment'].str.replace(r'\(.+?\)', '', regex=True)
# 특수문자 제거
sur['comment'] = sur['comment'].str.replace('[-=+,%&#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '', regex=True)
sur['comment'] = sur['comment'].str.strip()
# 요소 중에 빈 값 제거
for i, v in sur.iterrows():
    if v['comment'] == '':
        sur = sur.drop([i])
print(sur.head())


