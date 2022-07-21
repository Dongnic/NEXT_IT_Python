# pip install pandas
import pandas as pd
df = pd.read_excel('./emp.xlsx')
print(df.head)

# 몇 개만 출력
print(df.head(2))
# 데이터 기초 정보
print(df.info())
# 데이터 구조
print(df.shape)
# 기초 통계량
print(df.describe())
# 컬럼별 타입
print(df.dtypes)
# 기존 열을 활용하여 쉽게 열을 만들 수 있음
df['salary_plus_one'] = df['SALARY'] + 1
df['salary_two'] = df['SALARY'] * 2
df['salary_10000_over'] = df['SALARY'] > 10000
total_salary = df['SALARY'].sum()
median_salary = df['SALARY'].quantile(0.5)
print(df.head())
print('봉급 합계 :', total_salary, '봉급 평균값 :', median_salary)

df['salary_squared'] = df['SALARY'].apply(lambda x : x * x)
print(df.head())
writer = pd.ExcelWriter('emp2.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='Sheet1')
writer.close()