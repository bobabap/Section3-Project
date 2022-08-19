import requests
import json
from bs4 import BeautifulSoup
import time
import random
import csv
import pandas as pd
import pickle



NationCode = {'한국': 'KR', '영국': 'GB', '미국': 'US', '일본':'JP'}
def getMovieCodeByNation(NationCode):
     
    movieCode = []
 
    for key, val in NationCode.items():
        url = f'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?nation={val}&page=10000'
 
        response = requests.get(url)
 
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            
            # html에서 div 태그 중 class이름이 pagenavigation 태그를 찾아라
            pagenavigation = soup.find('div','pagenavigation')
 
            # pagenavigation내 <a> 태그 중 마지막 태그의 text 값
            lastPage = pagenavigation.find_all('a')[-1].text.replace(',','')

            for i in range(1, int(lastPage)+1):
                url = f'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?nation={val}&page={i}'
                response2 = requests.get(url)
                if response2.status_code == 200:
                    html = response2.text
                    soup = BeautifulSoup(html, 'lxml')
                    
                    # html에서 ul 태그 중 class이름이 directory_list 태그를 찾아라
                    directory_list = soup.find('ul','directory_list')
                    allA = directory_list.findAll('a')
                    for a in allA:
                        if '?code=' in str(a):
                            movieCode.append(str(a).split('?code=')[1].split('"')[0])
                    time.sleep(random.uniform(0.5, 1))
                else : 
                    print(response2.status_code)
        else : 
            print(response.status_code)
    
    return movieCode

movieCode = getMovieCodeByNation(NationCode)


filePath = './movieCode.txt'
with open(filePath, 'wb') as lf:
    pickle.dump(movieCode, lf)
    
    
with open(filePath, 'rb') as lf:
    readList = pickle.load(lf)
    print(readList)