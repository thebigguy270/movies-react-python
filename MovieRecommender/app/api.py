# app/api.py
from flask import Flask, jsonify, request
import pandas as pd
from recommender.recommender import load_data
from recommender.collaborative import create_user_item_matrix, calculate_similarity, get_recommendations as collaborative_recommendations
from recommender.content_based import create_tfidf_matrix, calculate_similarity, get_recommendations as content_based_recommendations

app = Flask(__name__)

# Chemin vers le fichier CSV des films prétraités
processed_movies_path = 'data/processed/movies_processed.csv'
ratings_path = 'data/raw/ratings.csv'

# Charger les données prétraitées
movies = load_data(processed_movies_path, ratings_path)
ratings = pd.read_csv(ratings_path)

# Créer la matrice utilisateur-élément
user_item_matrix = create_user_item_matrix(ratings)

# Calculer la similarité entre les utilisateurs
user_similarity = calculate_similarity(user_item_matrix)

# Créer la matrice TF-IDF des genres de films
tfidf_matrix = create_tfidf_matrix(movies)

# Calculer la similarité entre les films
cosine_sim = calculate_similarity(tfidf_matrix)

@app.route('/recommend/user/<int:user_id>', methods=['GET'])
def recommend_user(user_id):
    recommendations = collaborative_recommendations(user_id, user_item_matrix, user_similarity, movies)
    result = recommendations.to_dict(orient='records')
    return jsonify(result)

@app.route('/recommend/movie', methods=['GET'])
def recommend_movie():
    title = request.args.get('title')
    recommendations = content_based_recommendations(title, cosine_sim, movies)
    result = recommendations.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
