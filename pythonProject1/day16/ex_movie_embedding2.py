import re

from konlpy.tag import Okt
from gensim.models import FastText
import pandas as pd

from day5.mydb import Mydb

sql = """
        SELECT mv_title || ' 영화는 ' || TRIM(mv_reply) as mv_reply
        FROM movie_reply
        WHERE mv_reply IS NOT NULL
"""
db = Mydb()
okt = Okt()
df = pd.read_sql(sql, con=db.conn)
result = []
for i, v in df.iterrows():
    result.append(v['MV_REPLY'])
data = [s.split() for s in result]
model = FastText(data, vector_size=200, sg=1, workers=4)
model.save('fasttext_movie.model')
print(model.wv.most_similar(positive=['한산']))