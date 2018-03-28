from movie import Movie
from tvshow import TVShow
import fresh_tomatoes

toy_story = Movie("Toy Story", "A story of a boy and his toys that come to life",
                  "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg",
                  "https://www.youtube.com/watch?v=4KPTXpQehio")

the_big_bang_theory = TVShow("The Big Bang Theory", "A lot of nerds",
                             "https://news.bitcoin.com/wp-content/uploads/2017/11/hhaudtyduua.jpg",
                             "https://www.youtube.com/watch?v=WBb3fojgW0Q")

movies = [toy_story]
shows = [the_big_bang_theory]

fresh_tomatoes.open_page(movies, shows)
