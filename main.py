import showDB
import movieDB
import fresh_tomatoes
import tmdbsimple as tmdb

tmdb.API_KEY = 'fb63a0c036ee1bc7d7a9f95390b63d32'

print('Loading... Please wait a moment...')
print('Searching for random movies in the The Movie Database API.')
print('This may take a while.')

movies = movieDB.getMovies()
shows = showDB.getTVShows()

fresh_tomatoes.open_page(movies, shows)
