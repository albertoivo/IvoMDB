import tmdbsimple as tmdb

tmdb.API_KEY = 'fb63a0c036ee1bc7d7a9f95390b63d32'


kwargs = {'append_to_response': 'videos'}
movie = tmdb.TV(1400).info(**kwargs)
youtube = movie.get('videos').get('results')[0]['key']

print(youtube)
