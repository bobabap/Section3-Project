from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
import datatable as dt
import json
import re
from flask import jsonify
import requests



# from flask_app.routes.main_route import bp as main_bp

app = Flask(__name__)
# app.register_blueprint(main_bp)



matrix = dt.fread('matrix.csv')
matrix = matrix.to_pandas()

meta = pd.read_csv('final_data.csv')


genre = [] 
for i in meta['genres']:
    genre.append(re.sub('[-=.#/?:$}\]\[\']', '', i).split(','))

meta['genres'] = genre

# print(meta.columns)

matrix = matrix.fillna(-1)







def pearsonR(s1, s2):
    s1_c = s1 - s1.mean()
    s2_c = s2 - s2.mean()
    return np.sum(s1_c * s2_c) / np.sqrt(np.sum(s1_c ** 2) * np.sum(s2_c ** 2))

def recommend(input_movie, matrix, n, similar_genre=True):
    GENRE_WEIGHT = 0.1
    
    meta = pd.read_csv('final_data.csv')
    
    meta = meta[['movie_id', 'sword', 'movie_title', 'genres', 'score']]
    
    genre = [] 
    for i in meta['genres']:
        genre.append(re.sub('[-=.#/?:$}\]\[\']', '', i))

    meta['genres'] = genre
    
    input_genres = meta[meta['movie_title'] == input_movie]['genres'].iloc(0)[0]

    result = []
    for title in matrix.columns[1:]:
        if title == input_movie:
            continue

        # rating comparison
        cor = pearsonR(matrix[input_movie], matrix[title])
        
        # genre comparison
        if similar_genre and len(input_genres) > 0:
            temp_genres = meta[meta['movie_title'] == title]['genres'].iloc(0)[0]
            same_count = np.sum(np.isin(input_genres, temp_genres))
            cor += (GENRE_WEIGHT * same_count)
        
        if np.isnan(cor):
            continue
        else:
            result.append((title, '{:.2f}'.format(cor), temp_genres))
            
    result.sort(key=lambda r: r[1], reverse=True)

    return result[:n]

@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/movie', methods=['GET','POST'])
@app.route('/movie/<name>', methods=['GET','POST'])
def recommend_movie(name):
    recommend_result = recommend(name, matrix, 5, similar_genre=True)
    
    movie_ng = []
    for i in recommend_result:
        movie_ng.append({'Title' : i[0], 'Genre' : i[2]})

    return render_template('main.html', result=movie_ng, name=name)




if __name__ == '__main__':
    app.run(debug=True)