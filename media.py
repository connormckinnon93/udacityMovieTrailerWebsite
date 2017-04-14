# This code was written while watching the associated course materials
# I have refactored some in order to simplify production code
# Other potential expansions of this code learned in the course can be found on the tv_shows branch


# From the Python Standard Library and contains methods to work with the browser
import webbrowser

# Refactored to create parent class for later use in incorporating TV Shows
class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

# Movie class used to save information about movies
class Movie(Video):
    
    """ This class stores movie related information """
    
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube, duration = None):
        
        # Inherits from the Video class and sets duration to none by default
        Video.__init__(self, title, duration)
        
        # Initializes the instance variables for this class
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube