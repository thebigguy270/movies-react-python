import pandas as pd
import os
# Chemins vers les fichiers CSV
movies_path = 'data/raw/movies.csv'
ratings_path = 'data/raw/ratings.csv'

# Obtenir le chemin du répertoire courant du script
current_dir = os.path.dirname(os.path.abspath(__file__))
processed_dir = os.path.join(current_dir, '../../data/processed')
processed_file_path = os.path.join(processed_dir, 'movies_processed.csv')


# Créer le répertoire s'il n'existe pas déjà
os.makedirs(processed_dir, exist_ok=True)

# Charger les données
movies = pd.read_csv(movies_path)
ratings = pd.read_csv(ratings_path)

# Exploration initiale des données
print("Movies DataFrame:")
print(movies.head())
print("\nMovies Info:")
print(movies.info())

print("\nRatings DataFrame:")
print(ratings.head())
print("\nRatings Info:")
print(ratings.info())

# Vérifier les valeurs manquantes
print("\nMissing values in Movies:")
print(movies.isnull().sum())

print("\nMissing values in Ratings:")
print(ratings.isnull().sum())

# Prétraitement des données
# Transformer les genres en liste de genres
movies['genres'] = movies['genres'].str.split('|')

# Calculer la note moyenne pour chaque film
average_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()
average_ratings.columns = ['movieId', 'average_rating']

# Fusionner les données de films avec les notes moyennes
movies = pd.merge(movies, average_ratings, on='movieId')

# Sauvegarder les données prétraitées
movies.to_csv(processed_file_path, index=False)

print("\nProcessed Movies DataFrame:")
print(movies.head())
