import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer  # 피체 벡터화
from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도

df = pd.read_csv('csv/url_data.csv')
print(df.info())

count_vect_category = CountVectorizer(min_df=0, ngram_range=(1,2))
place_category = count_vect_category.fit_transform(df['cate_mix'])
place_simi_cate = cosine_similarity(place_category, place_category)
place_simi_cate_sorted_ind = place_simi_cate.argsort()[:, ::-1]
