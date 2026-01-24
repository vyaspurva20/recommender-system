# test_app.py
import pytest
import app

def test_recommend_output_type():
    """Check that recommend() returns a list"""
    movie = app.movies.iloc[0].title
    result = app.recommend(movie)
    assert isinstance(result, list)

def test_recommend_output_length():
    """Check that recommend() returns 5 movies"""
    movie = app.movies.iloc[0].title
    result = app.recommend(movie)
    assert len(result) == 5

def test_movies_pickle_loads():
    """Check that pickle files load correctly"""
    import pickle
    movies = pickle.load(open("movies_dict.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    assert len(movies) > 0
    assert len(similarity) > 0
def test_fail():
    assert 1==0
