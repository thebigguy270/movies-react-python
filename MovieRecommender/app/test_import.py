# test_import.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommender.recommender import load_data

print("Module imported successfully!")
