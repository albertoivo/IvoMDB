from movie import Movie
import util
import constants

import requests
from random import randint
import tmdbsimple as tmdb


def getMovies():
    movies = []
    count = 0
    while count < 10:
        id = randint(100, 1000)
        try:
            movie = tmdb.Movies(id)
            m = movie.info()
            if util.isValidImage(str(m['poster_path'])):
                item = Movie(m['title'], m['overview'], str(constants.URL_IMAGE) + str(m['poster_path']),
                             'https://www.youtube.com/watch?v=4KPTXpQehio')
                movies.append(item)
                count = count + 1
        except requests.exceptions.HTTPError:
            print('There is no movie with the id: ' + str(id))

    return movies
