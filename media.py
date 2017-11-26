import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    #movie ratings
    VALID_RATINGS = ["G","PG","PG-13","R"]
    """
    class Movie:
        - class of all my favorite movies
        
    init function:
        movie_title: display the title of movie
        movie_storyline: description of the movie
        poster_image: displays an image for the movie
        trailer_youtube: trailer for the movie

    show_trailer function:
        webbrowser.open: opens default webbroswer to youtube with the correct movie trailer

    """
    #instance variables
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        #open movie trailor
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
