# app.py
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Charger les données pré-traitées
movies = pd.read_csv('data\processed\movies_processed.csv')

@app.route('/recommend', methods=['GET'])
def recommend():
    top_movies = movies.sort_values(by='average_rating', ascending=False).head(10)
    result = top_movies[['title', 'average_rating']].to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
