import json
import fresh_tomatoes
import media

"""Displays information about the movies in movies.json in a browser."""
with open('movies.json') as movie_file:
    movie_specs = json.load(movie_file)
    movies = map(lambda x: media.Movie(**x), movie_specs)
    fresh_tomatoes.open_movies_page(movies)