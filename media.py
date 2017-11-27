import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    """
    class Movie:
        - class of all my favorite movies

    init function:
        movie_title: display the title of movie
        movie_storyline: description of the movie
        poster_image: displays an image for the movie
        trailer_youtube: trailer for the movie

    show_trailer function:
        - Opens default webbroswer to youtube with the correct movie trailer


    """

    def __init__(self, mov_title, mov_storyline, post_image, trailer_youtube):
        self.title = mov_title
        self.storyline = mov_storyline
        self.poster_image_url = post_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
