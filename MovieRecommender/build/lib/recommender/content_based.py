# recommender/content_based.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def create_tfidf_matrix(movies):
    """
    Crée une matrice TF-IDF des genres de films.
    """
    movies['genres'] = movies['genres'].apply(lambda x: ' '.join(x))
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    return tfidf_matrix


def calculate_similarity(tfidf_matrix):
    """
    Calcule la similarité cosine entre les films.
    """
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim


def get_recommendations(title, cosine_sim, movies, n=10):
    """
    Recommande des films similaires à un film donné en utilisant la similarité cosine.
    """
    # Obtenir l'index du film correspondant au titre
    idx = movies[movies['title'] == title].index[0]

    # Obtenir les scores de similarité pour tous les films avec ce film
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Trier les films en fonction des scores de similarité
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Obtenir les scores des n films les plus similaires
    sim_scores = sim_scores[1:n + 1]

    # Obtenir les indices des films
    movie_indices = [i[0] for i in sim_scores]

    # Retourner les titres des films les plus similaires
    return movies.iloc[movie_indices][['title', 'average_rating']]


if __name__ == '__main__':
    # Chemin vers le fichier CSV des films prétraités
    processed_movies_path = '../data/processed/movies_processed.csv'

    # Charger les données prétraitées
    movies = pd.read_csv(processed_movies_path)

    # Créer la matrice TF-IDF des genres de films
    tfidf_matrix = create_tfidf_matrix(movies)

    # Calculer la similarité entre les films
    cosine_sim = calculate_similarity(tfidf_matrix)

    # Obtenir les recommandations pour un film donné
    title = 'Toy Story (1995)'
    recommendations = get_recommendations(title, cosine_sim, movies)
    print(recommendations)
