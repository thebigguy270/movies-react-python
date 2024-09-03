from setuptools import setup, find_packages

setup(
    name='movie-recommender',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'pandas',
        'numpy',
        'scikit-learn',
        # Ajoutez ici d'autres dépendances nécessaires
    ],
    entry_points={
        'console_scripts': [
            'movie-recommender=main:main',
        ],
    },
    include_package_data=True,
    description='A movie recommendation system using collaborative and content-based filtering',
    author='Marc-Antoine Lussier',
    author_email='marcantoinelssr4@example.com',
    url='https://github.com/votreprofil/movie-recommender',  # Mettez ici l'URL de votre projet
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
