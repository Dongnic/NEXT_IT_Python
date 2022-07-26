# 피마 인디언 데이터 (당뇨병 예측)
#
# 임신 횟수, 포도당 수치, 혈압, 피부두께, 인슐린, BMI, 당뇨병가족력, 나이
# 당뇨병 여부 (0:아님, 1:당뇨) <-- 종속 변수 이항분류
import pandas as pd
df = pd.read_csv('./datasets/pima-indians-diabetes.csv')
print(df.info())
x = df.iloc[:, 0:8]  # :은 전체 행을 의미 0:8은 0부터 8 전 까지를 의미
y = df.iloc[:, 8]
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)
model = LogisticRegression(max_iter=50000)  # max_iter 기본 값 100, 100번으로 결과 값이 안 나오면 오류 메세지와 함께 결과 값 출력
train_x = scaler.fit_transform(train_x)
test_x = scaler.fit_transform(test_x)
model.fit(train_x, train_y.values.ravel())
print(model.coef_)  # 기울기
print(model.intercept_)  # y절편
print('학습 데이터 성능 : ', model.score(train_x, train_y))
print('테스트 데이터 성능 : ', model.score(test_x, test_y))