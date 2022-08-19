from tracemalloc import start
from naver_movie import user_review_info_scrap
import pickle
import pandas as pd

filePath = './userid.txt'
with open(filePath, 'rb') as lf:
    readList = pickle.load(lf)

List = readList[:1000]
data = []
for user in List:
    user_sword = user_review_info_scrap.get_user_review(user, 10, 10) # 17471693
    if user_sword:
        user_sword = pd.DataFrame(user_sword).values
        for i in user_sword:
            data.append(i)
        # start.append(user_sword['user_number', 'movie_title', 'movie_id', 'score', 'sword', 'user_name'].values)
    else:
        pass

data = pd.DataFrame(data)
data.columns = ['user_number', 'movie_title', 'movie_id', 'score', 'sword', 'user_name']

data.to_csv('data.csv')