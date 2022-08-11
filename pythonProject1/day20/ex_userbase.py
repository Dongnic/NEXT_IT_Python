import pandas as pd

df_rating = pd.read_csv('./data/ratings.csv')
df_movie = pd.read_csv('./data/movies.csv')
df_rating.drop('timestamp', axis=1, inplace=True)
user_movie_rating = pd.merge(df_rating, df_movie, on='movieId')
user_movie = user_movie_rating.pivot_table('rating', index='userId', columns='title')
user_movie.fillna(0, inplace=True)

from sklearn.metrics.pairwise import cosine_similarity

user_base_metric = cosine_similarity(user_movie)
user_base_metric_df = pd.DataFrame(data=user_base_metric, index=user_movie.index, columns=user_movie.index)
print(user_base_metric_df.head())

def get_user_base(id, user_movie_ratings):
    mybest = user_movie_ratings[user_movie_rating['userId'] == id].sort_values(by='rating', ascending=False)[:6]
    print('내가 평점을 높게 준 영화: ', mybest['title'])
    # 대상 user id와 비슷한 유저 5명
    sim_user = user_base_metric_df[id].sort_values(ascending=False)[:6]
    id_list = sim_user.index.tolist()[1:]
    print(id_list)
    # 비슷한 유저 5명이 높은 평점을 준 내가 안 본 영화 추천
    data = []
    for i in id_list:
        print('user: ' + str(i))
        item = get_user_item(i, id, user_movie_rating)
        data = data + item
    set_item = set(data)
    return set_item

def get_user_item(id, userId, user_movie_rating):
    movie_list = user_movie_rating[user_movie_rating['userId'] == id]
    user_watch_movie = user_movie_rating[user_movie_rating['userId'] == userId]
    movies = movie_list[~movie_list['movieId'].isin(user_watch_movie['movieId'].values.tolist())]
    five_best = movies.sort_values(by='rating', ascending=False)[:5]
    return five_best['title'].values.tolist()

while True:
    id = input('user id: ')
    recommend_list = get_user_base(int(id), user_movie_rating)
    print('='*100)
    print('추천 영화')
    for i in recommend_list:
        print(i)