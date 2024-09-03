# Movie Recommender System

## Description

This is a movie recommender system that uses collaborative filtering, content-based filtering, and hybrid methods to suggest movies to users. The project consists of a Python backend that processes movie data and provides recommendations, and a ReactJS frontend for users to interact with the recommender system.

## Features

- **Collaborative Filtering**: Recommends movies based on user ratings.
- **Content-Based Filtering**: Recommends movies based on the content features of movies the user has liked.
- **Hybrid Method**: Combines collaborative and content-based filtering for better recommendations.
- **REST API**: Exposes the recommender system as an API.
- **ReactJS Frontend**: A simple frontend to interact with the recommender system.

## Prerequisites

- Python 3.7+
- Node.js 14+
- npm or Yarn
- Git

## Installation

### Backend (Python)

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/movie-recommender.git
    cd movie-recommender
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure the required datasets are in the `data/raw/` directory:
    - `movies.csv`
    - `ratings.csv`

5. Run the data preprocessing script:
    ```bash
    python data/scripts/data_exploration.py
    ```

6. Start the backend server:
    ```bash
    python app/api.py
    ```

### Frontend (ReactJS)

1. Navigate to the frontend directory:
    ```bash
    cd app
    ```

2. Install the required npm packages:
    ```bash
    npm install
    ```

3. Start the React development server:
    ```bash
    npm start
    ```

The React app should now be running at `http://localhost:3000` and the backend API at `http://localhost:5000`.

## Usage

1. Open your browser and go to `http://localhost:3000`.
2. Enter the necessary inputs to receive movie recommendations.
3. The frontend communicates with the backend to fetch and display the recommended movies.

## Testing

### Backend

Run the unit tests for the recommender system:

```bash
python -m unittest discover -s tests
