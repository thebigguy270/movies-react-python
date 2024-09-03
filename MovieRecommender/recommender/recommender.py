# recommender/recommender.py
import pandas as pd


def load_data(movies_path, ratings_path):
    """
    Charge les données de films et de notes depuis les fichiers CSV.
    """
    movies = pd.read_csv(movies_path)
    ratings = pd.read_csv(ratings_path)
    return movies, ratings


def preprocess_data(movies, ratings):
    """
    Prétraite les données en calculant les notes moyennes des films.
    """
    movies['genres'] = movies['genres'].str.split('|')

    # Calculer la note moyenne pour chaque film
    average_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()
    average_ratings.columns = ['movieId', 'average_rating']

    # Fusionner les données de films avec les notes moyennes
    movies = pd.merge(movies, average_ratings, on='movieId')
    return movies


def recommend_top_movies(movies, n=10):
    """
    Recommande les films avec les meilleures notes moyennes.
    """
    top_movies = movies.sort_values(by='average_rating', ascending=False).head(n)
    return top_movies[['title', 'average_rating']]


if __name__ == '__main__':
    # Chemins vers les fichiers CSV
    movies_path = 'data/raw/movies.csv'
    ratings_path = 'data/raw/ratings.csv'

    # Charger et prétraiter les données
    movies, ratings = load_data(movies_path, ratings_path)
    movies = preprocess_data(movies, ratings)

    # Obtenir les meilleures recommandations
    top_movies = recommend_top_movies(movies)
    print(top_movies)
