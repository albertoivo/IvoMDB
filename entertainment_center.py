from movie import Movie
import fresh_tomatoes

toy_story = Movie("Toy Story", "A story of a boy and his toys that come to life",
                  "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg",
                  "https://www.youtube.com/watch?v=4KPTXpQehio")

movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)
