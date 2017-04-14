import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    """ This class stores movie related information """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube, duration = None):
        Video.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    def show_poster(self):
        webbrowser.open(self.poster_image_url)

class TvShow(Video):
    """ This class stores TV show related information """
    
    def __init__(self, title, season, episode, tv_station, duration = None):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
    
    def get_local_listing():
        return None