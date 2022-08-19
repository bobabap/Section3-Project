import pandas as pd

data = pd.read_csv('data.csv')
data.drop(['Unnamed: 0'], axis=1, inplace=True)

genre = pd.read_csv('genre.csv')
genre.drop(['Unnamed: 0', 'title'], axis=1, inplace=True)

final_data = pd.merge(data, genre, on='movie_id', how='inner')

final_data.to_csv('final_data.csv')