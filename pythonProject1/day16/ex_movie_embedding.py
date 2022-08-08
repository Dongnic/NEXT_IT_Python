import re

from konlpy.tag import Okt
from gensim.models import word2vec
import pandas as pd

from day5.mydb import Mydb

sql = """
        SELECT mv_title || ' 영화는 ' || TRIM(mv_reply) as mv_reply
        FROM movie_reply
        WHERE mv_reply IS NOT NULL
"""
db = Mydb()
okt = Okt()
nm = '한산'
df = pd.read_sql(sql, con=db.conn)
result = []
for i , v in df.iterrows():
    text = okt.pos(v['MV_REPLY'], norm=True, stem=True)
    # print(text)
    re = []
    for word in text:
        if not word[1] in ["Josa", "Modifier", "Punctuation", "Eomi"]:
            re.append(word[0])
        rl = (" ".join(re)).strip()
        result.append(rl)
print(result)
nlp_data = 'movie.nlp'
with open(nlp_data, 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))
wData = word2vec.LineSentence(nlp_data)
model = word2vec.Word2Vec(wData, sg=1, vector_size=200, window=3, min_count=3, workers=4)
model.save('movie.model')