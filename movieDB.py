from movie import Movie
import util
import constants

import requests
from random import randint
import tmdbsimple as tmdb


def getMovies():
    movies = []
    count = 0
    while count < constants.NUMBER_OF_MEDIAS:
        id = randint(100, 1000)
        try:
            movie = tmdb.Movies(id)
            m = movie.info()
            if util.isValidImage(str(m['poster_path'])):
                item = Movie(m['title'], m['overview'],
                             str(constants.URL_IMAGE) + str(m['poster_path']),
                             'https://www.youtube.com/watch?v=' +
                             str(youtube(id)))
                movies.append(item)
                count = count + 1
        except requests.exceptions.HTTPError:
            print('There is no movie with the id: ' + str(id))

    return movies


def youtube(id):
    try:
        tmdb.API_KEY = constants.TMDB_API_KEY
        kwargs = {'append_to_response': 'trailers'}
        movie = tmdb.Movies(id).info(**kwargs)
        youtube = movie.get('trailers').get('youtube')[0]['source']
        # print youtube
        return youtube
    except IndexError:
        # In this API, not all movies has trailer in Youtube.
        print('No youtube url')
