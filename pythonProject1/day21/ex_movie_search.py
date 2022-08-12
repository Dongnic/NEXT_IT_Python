import pandas as pd

df_ratings = pd.read_csv('../day20/data/ratings.csv')
df_movies = pd.read_csv('../day20/data/movies.csv')
df_ratings.drop('timestamp', axis=1, inplace=True)
user_movie_rating = pd.merge(df_ratings, df_movies, on='movieId')
movie_user_rating = user_movie_rating.pivot_table('rating', index='title', columns='userId')
movie_user_rating.fillna(0, inplace=True)
print(movie_user_rating.head(10))

from sklearn.metrics.pairwise import cosine_similarity
item_base = cosine_similarity(movie_user_rating)
item_base_collabor = pd.DataFrame(data=item_base, index=movie_user_rating.index, columns=movie_user_rating.index)

def get_item_base(title, collabor):
    return collabor[title].sort_values(ascending=False)[:6]

while True:
    text = input('영화 이름: ')
    print(get_item_base((text, item_base_collabor)))