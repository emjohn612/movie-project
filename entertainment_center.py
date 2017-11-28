import media
import fresh_tomatoes


"""
    instances for class Movie:
        title, storyline, poster_image, youtube_trailer
"""
the_road = media.Movie("The Road",
                       "In a dangerous post-apocalyptic world,\
                        an ailing father defends his son as they slowly\
                        travel to the sea."
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwNzk4NTU3NDReQTJeQWpwZ15BbWU3MDg3OTEyODI@._V1_UY268_CR0,0,182,268_AL_.jpg",  # noqa
                       "https://www.youtube.com/watch?v=FsFFwaRxoDw")

into_the_wild = media.Movie("Into the Wild",
                            "After graduating from Emory University,\
                             top student and athlete Christopher McCandless\
                             abandons his possessions, and hitchhikes to\
                             Alaska to live in the wilderness.",
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/Into-the-wild.jpg",  # noqa
                            "https://www.youtube.com/watch?v=2LAuzT_x8Ek")

the_incredibles = media.Movie("The Incredibles",
                              "A family of undercover superheroes, while\
                               trying to live the quiet suburban life, are\
                               forced into action to save the world.",
                              "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-18hpovx_f8238c31.jpeg?region=0,0,300,450",  # noqa
                              "https://www.youtube.com/watch?v=eZbzbC9285I")

man_on_fire = media.Movie("Man On Fire",
                          "In Mexico City, a former assassin swears vengeance\
                           on those who committed an unspeakable act against \
                           the family he was hired to protect.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BODFlMmEwMDgtYjhmZi00ZTE5LTk2NWQtMWE1Y2M0NjkzOGYxXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR0,0,182,268_AL_.jpg",  # noqa
                          "https://www.youtube.com/watch?v=rb-ZEBBKolc")

how_i_live_now = media.Movie("How I Live Now",
                             "An American girl, sent to the English countryside\
                              to stay with relatives, finds love and purpose\
                              while fighting for her survival as war envelops\
                              the world around her.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU4NTg4NzgzMF5BMl5BanBnXkFtZTgwOTU1NTMxMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                             "https://www.youtube.com/watch?v=RSaxm68PPT4")

hanna = media.Movie("Hanna",
                    "A sixteen-year-old girl who was raised by her father\
                     to be the perfect assassin is dispatched on a mission\
                     across Europe, tracked by a ruthless intelligence agent\
                     and her operatives.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BNTAzMTg1NjY0NF5BMl5BanBnXkFtZTcwODc3MTgzNA@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                    "https://www.youtube.com/watch?v=u73CLdHpbNk")

"""
fresh_tomatoes.open:
    call the (open_movies_page) function inside of the fresh_tomatoes.py file
"""
movies = [the_road, into_the_wild, the_incredibles,
          man_on_fire, how_i_live_now, hanna]
fresh_tomatoes.open_movies_page(movies)
