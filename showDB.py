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
    while count < 10:
        id = randint(1400, 2000)
        try:
            movie = tmdb.TV(id)
            m = movie.info()
            if util.isValidImage(str(m['poster_path'])):
                item = TVShow(m['name'], m['overview'],
                              str(constants.URL_IMAGE) + str(m['poster_path']),
                              'https://www.youtube.com/watch?v=4KPTXpQehio')
                shows.append(item)
                count = count + 1
        except requests.exceptions.HTTPError:
            print('There is no show with the id: ' + str(id))

    return shows
