import pandas as pd

df = pd.read_csv('./datasets/Titanic Passengers.csv')
print(df.columns)

# 'pclass' 티켓 (1 = 1등석 ...)
# 'survived' 종속 변수(target class (0:사망, 1:생존))
# 'name'
# 'age'
# 'sibsp' 탑승 자녀 수
# 'parch' 부모님 수
# 'ticket' 티켓 번호
# 'fare' 요금
# 'cabin' 수화물
print(df.describe())
info = df[['sex', 'survived']].groupby('sex', as_index=False).mean().sort_values(by='sex', ascending=False)
print(info)

# 여 : 1 남 0
df['sex'] = df['sex'].map({'female': 1, 'male': 0})
print(df.head())
# 결측치 평균 값으로(결측 치는 null 값임)
df['age'].fillna(value=df['age'].mean(), inplace=True)
# pclass 1 -> firstclass 컬럼의 1로 나머지는 0으로
df['firstClass'] = df['pclass'].apply(lambda x: 1 if x == 1 else 0)
df['secondClass'] = df['pclass'].apply(lambda x: 1 if x == 2 else 0)
df['thirdClass'] = df['pclass'].apply(lambda x: 1 if x == 3 else 0)
x = df[['sex', 'age', 'firstClass', 'secondClass', 'thirdClass']]
y = df[['survived']]

from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)

# 정규화(스케일링)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
train_x = scaler.fit_transform(train_x)
test_x = scaler.fit_transform(test_x)
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(train_x, train_y.values.ravel())
print(model.coef_)  # 기울기
print(model.intercept_)  # y절편

print('학습 데이터 성능 : ', model.score(train_x, train_y))
print('테스트 데이터 성능 : ', model.score(test_x, test_y))
import numpy as np

Jack = np.array([0.0, 20.0, 0.0, 0.0, 1.0])
Rose = np.array([1.0, 17.0, 1.0, 0.0, 0.0])
Na = np.array([0.0, 25.0, 0.0, 1.0, 0.0])
Baby = np.array([1.0, 3.0, 0.0, 1.0, 0.0])
sample = np.array([Jack, Rose, Na, Baby])
sample = scaler.transform(sample)
print(model.predict(sample))
