# pip install pandas
import pandas as pd

user = {"name": ["Tom", "Tyrell", "Claire"]
        , "age": [60, 25, 30]}
df_user_age = pd.DataFrame(user)
print(df_user_age.head())
# 다이렉트로 생성
df_user_height = pd.DataFrame({
        "name": ["Tom", "Tyrell", "Claire"]
        , "height": [6.2, 4.9, 5.5]
})
# join ('name'를 기준으로)
joined = df_user_age.set_index("name").join(df_user_height.set_index('name'))
print(joined.head())
# 인덱스를 다시 숫자로
print(joined.reset_index())
# 'gender'를 기준으로 평균
joined['gender'] = ['M', 'M', 'F']
print(joined.head())
# group by 기능 (내장 함수 이외의 apply 함수를 통해 함수를 적용 할 수 있음)
print('평균', joined.groupby('gender').mean()) # mean() : 평균
