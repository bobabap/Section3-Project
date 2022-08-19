from naver_movie import user_sword_scrap
import pickle
import time
import random
import pandas as pd

filePath = './movieCode.txt'
with open(filePath, 'rb') as lf:
    readList = pickle.load(lf)


movie_id = list(map(int, readList))


def user_get_id():
    result = []
    for i in movie_id:
        user_sword = user_sword_scrap.request_get_user_code(i, start_page=1, end_page=1)
        if type(user_sword) is list:
            result.append(user_sword)
        else:
            pass
    return result

user_dict = user_get_id()

user_list = []
for i in user_dict:
    for z in i:
        user_list.append(z['user'])


filePath = './userid.txt'
with open(filePath, 'wb') as lf:
    pickle.dump(user_list, lf)


userfilePath = './user_id.txt'
with open(filePath, 'rb') as lf:
    readList = pickle.load(lf)
    print(list(map(int, readList)))
