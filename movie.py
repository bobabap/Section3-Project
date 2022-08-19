from naver_movie import movie_scrap
import pickle
import time
import random
import pandas as pd

filePath = './movieCode.txt'
with open(filePath, 'rb') as lf:
    readList = pickle.load(lf)
    
movie_id = list(map(int, readList))

# movie_id = 132626
# movie_data = movie_scrap.get_movie_data(movie_id)
# print(pd.DataFrame(movie_data))
movie_id = pd.read_csv('data.csv')['movie_id'].unique()

data = []
for i in movie_id:
    movie_data = movie_scrap.get_movie_data(i) # 17471693
    if movie_data:
        data.append(movie_data)
    else:
        pass

data = pd.DataFrame(data)

data.to_csv('genre.csv')