# recommender/collaborative.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


def create_user_item_matrix(ratings):
    """
    Crée une matrice utilisateur-élément (films) à partir des notes.
    """
    user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
    return user_item_matrix


def calculate_similarity(user_item_matrix):
    """
    Calcule la similarité cosine entre les utilisateurs.
    """
    user_similarity = cosine_similarity(user_item_matrix.fillna(0))
    return user_similarity


def get_recommendations(user_id, user_item_matrix, user_similarity, movies, n=10):
    """
    Recommande des films à un utilisateur donné en utilisant le filtrage collaboratif basé sur les utilisateurs.
    """
    user_index = user_item_matrix.index.tolist().index(user_id)
    similarity_scores = user_similarity[user_index]
    user_ratings = user_item_matrix.iloc[user_index].dropna()

    # Scores des utilisateurs similaires
    similar_users = user_item_matrix.loc[:, user_ratings.index]
    weighted_scores = similar_users.T.dot(similarity_scores).div(similarity_scores.sum())

    # Retirer les films déjà notés par l'utilisateur
    recommendations = weighted_scores.drop(user_ratings.index)
    recommendations = recommendations.sort_values(ascending=False).head(n)

    recommended_movies = movies[movies['movieId'].isin(recommendations.index)]
    return recommended_movies[['title', 'average_rating']]


if __name__ == '__main__':
    # Chemins vers les fichiers CSV
    ratings_path = '../data/raw/ratings.csv'
    movies_path = '../data/processed/movies_processed.csv'

    # Charger les données
    ratings = pd.read_csv(ratings_path)
    movies = pd.read_csv(movies_path)

    # Créer la matrice utilisateur-élément
    user_item_matrix = create_user_item_matrix(ratings)

    # Calculer la similarité entre les utilisateurs
    user_similarity = calculate_similarity(user_item_matrix)

    # Obtenir les recommandations pour un utilisateur donné
    user_id = 1
    recommendations = get_recommendations(user_id, user_item_matrix, user_similarity, movies)
    print(recommendations)
