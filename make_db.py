import os
import sqlite3
import re
import pandas as pd

# DB_FILENAME = 'movie.db'
# DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

# conn = sqlite3.connect(DB_FILENAME)
# cur = conn.cursor()


# cur.execute("DROP TABLE IF EXISTS movie_data;")
# cur.execute("""CREATE TABLE IF NOT EXISTS movie_data (
#     movie_title VARCHAR,
#     movie_id INT,
#     score INT,
#     sword INT,
#     user_name VARCHAR,
#     genres VARCHAR,
#     story VARCHAR)
# """)


# import pandas as pd

# df = pd.read_csv('final_data.csv')
# df.drop(['Unnamed: 0', 'user_number'], axis=1, inplace=True)



# genre = [] 
# for i in df['genres']:
#     genre.append(re.sub('[-=.#/?:$}\]\[\']', '', i).split(','))

# df['genres'] = genre


# for i in range(len(df.index)):
#     cur.execute("INSERT INTO movie_data (movie_title, movie_id, score, sword, user_name, genres, story) VALUES (?, ?, ?, ?, ?, ?, ?);", 
#                 (str(df['movie_title'].iloc[i]), int(df['movie_id'].iloc[i]), int(df['score'].iloc[i]), int(df['sword'].iloc[i]), str(df['user_name'].iloc[i]), str(df['genres'].iloc[i]), str(df['story'].iloc[i])
#                 )
#                 )
    
    
# conn.commit()

# cur.close()
# conn.close()