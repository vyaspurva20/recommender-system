# error.py
# Intentional error to test AI CI agent

import pandas as pd

# This function is correctly defined
def load_data():
    data = {
        "user": ["Alice", "Bob", "Charlie"],
        "movie": ["Inception", "Titanic", "Matrix"],
        "rating": [5, 4, 5]
    }
    return pd.DataFrame(data)

# This will cause a NameError intentionally
def recommend_top_movies():
    # Typo function call (error)
    df = load_dta()   
    top_movies = df.groupby("movie")["rating"].mean().sort_values(ascending=False)
    print(top_movies)

# Execute function to trigger error
recommend_top_movies()
