import webbrowser


class Movie(object):
    '''This class provides a way to store movie related information'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
