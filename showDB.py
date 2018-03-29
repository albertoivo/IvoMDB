from tvshow import TVShow
import showDB
import constants
import util
import requests
from random import randint
import tmdbsimple as tmdb


def getTVShows():
    shows = []
    count = 0
    while count < constants.NUMBER_OF_MEDIAS:
        id = randint(1400, 2000)
        try:
            movie = tmdb.TV(id)
            m = movie.info()
            if util.isValidImage(str(m['poster_path'])):
                item = TVShow(m['name'], m['overview'],
                              str(constants.URL_IMAGE) + str(m['poster_path']),
                              'https://www.youtube.com/watch?v=' +
                              str(youtube(id)))
                shows.append(item)
                count = count + 1
        except requests.exceptions.HTTPError:
            print('There is no show with the id: ' + str(id))

    return shows


def youtube(id):
    try:
        tmdb.API_KEY = constants.TMDB_API_KEY
        kwargs = {'append_to_response': 'videos'}
        movie = tmdb.TV(id).info(**kwargs)
        youtube = movie.get('videos').get('results')[0]['key']
        # print youtube
        return youtube
    except IndexError:
        # In this API, not all movies has trailer in Youtube.
        print('No youtube url')
