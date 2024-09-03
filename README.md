# Movie Recommender System

This project is a movie recommendation system built with a Python backend and a React frontend. The backend API handles data processing and recommendation logic, while the frontend provides an interactive interface for users to receive movie recommendations.

## Project Structure

```plaintext
movie-recommender/
│
├── data/
│   ├── raw/                # Raw data (movies.csv, ratings.csv)
│   ├── processed/          # Processed data
│   └── scripts/            # Data processing scripts
│       └── data_exploration.py # Script for data exploration
│
├── recommender/
│   ├── __init__.py         # Package initializer
│   ├── collaborative.py    # Collaborative filtering logic
│   ├── content_based.py    # Content-based filtering logic
│   └── hybrid.py           # Hybrid recommendation logic
│   └── recommender.py      # Main recommendation engine
│
├── app/
│   ├── api.py              # Flask API for recommendations
│   ├── templates/          # HTML templates (if any)
│   └── static/             # Static files (CSS, JS)
│
├── frontend/               # React frontend
│   ├── public/             # Public assets
│   ├── src/                # Source files
│   │   ├── components/     # React components
│   │   ├── App.js          # Main React component
│   │   └── index.js        # React entry point
│   └── package.json        # Frontend dependencies
│
├── tests/
│   ├── test_data.py        # Tests for data processing
│   └── test_recommender.py # Tests for recommendation logic
│
├── requirements.txt        # Backend dependencies
├── README.md               # Project documentation
└── setup.py                # Backend setup script
