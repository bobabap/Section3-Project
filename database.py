import psycopg2
import re
import sqlalchemy
from sqlalchemy import create_engine
import requests
import psycopg2.extras


host = 'ruby.db.elephantsql.com'
user = 'skudweoz'
database = 'skudweoz'
password = 'YhEaDm_37OMGdK9iEsKc8SOCL2eX14mt'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS movie_data;")
cur.execute("""CREATE TABLE IF NOT EXISTS movie_data (
    movie_title VARCHAR,
    movie_id INT,
    score INT,
    sword INT,
    user_name VARCHAR,
    genres VARCHAR,
    story VARCHAR)
""")



import pandas as pd

df = pd.read_csv('final_data.csv')
df.drop(['Unnamed: 0', 'user_number'], axis=1, inplace=True)



genre = [] 
for i in df['genres']:
    genre.append(re.sub('[-=.#/?:$}\]\[\']', '', i).split(','))

df['genres'] = genre
# for i in range(100):
#     print(df['movie_title'][i],
#         int(df['movie_id'][i]),
#         int(df['score'][i]),
#         int(df['sword'][i]),
#         df['user_name'][i],
#         df['genres'][i],
#         df['story'][i]
#         )

for i in range(15000):
    cur.execute("INSERT INTO movie_data (movie_title, movie_id, score, sword, user_name, genres, story) VALUES (%s, %s, %s, %s, %s, %s, %s);", 
                (str(df['movie_title'].iloc[i]), int(df['movie_id'].iloc[i]), int(df['score'].iloc[i]), int(df['sword'].iloc[i]), str(df['user_name'].iloc[i]), str(df['genres'].iloc[i]), str(df['story'].iloc[i])
                )
                )
#  ON CONFLICT (movie_id) DO NOTHING

connection.commit()
cur.close()
connection.close()



