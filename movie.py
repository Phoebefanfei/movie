import pandas as pd
import datetime

tag = pd.read_csv('tags.csv') 
rate = pd.read_csv('ratings.csv')
movie = pd.read_csv('movies.csv')
link = pd.read_csv('links.csv')
genome_scores = pd.read_csv('genome-scores.csv')
genome_tags = pd.read_csv('genome-tags.csv')

q1 = tag.userId.nunique()
print(f"一共有{q1}位不同的用户")
q2 = movie.movieId.nunique()
print(f"一共有{q1}个不同的电影")
q3 = movie.genres.nunique()
print(f"一共有{q3}个不同的电影种类")
movie_link = pd.merge(movie,link,how='left',on='movieId')
fil_mv_lk = movie_link[movie_link[['tmdbId','tmdbId']].isnull().T.any()]
q4 = fil_mv_lk.movieId.nunique()
print(f"一共有{q4}个电影没有外部链接")
rate['timestamp'] = rate['timestamp'].apply(lambda x:datetime.datetime.utcfromtimestamp(x).strftime("%Y-%m-%d"))
q5 = rate[rate.apply(lambda x: x['timestamp'][0:4] == '2018', axis=1)].userId.nunique()
print(f"2018年一共有{q5}人进行过电影评分")