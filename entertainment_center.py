# Contains the code to produce the website
import fresh_tomatoes

# Contains the classes used to manage information related to movies
import media

# Some of my favourite movies saved to instances of Movie
unbreakable = media.Movie("Unbreakable",
                          "A man wrestles with whether or not he is a hero",
                          "https://upload.wikimedia.org/wikipedia/en/9/9e"
                          "/Unbreakableposterwillis.jpg",
                          "https://www.youtube.com/watch?v=HGrN6blSCGw")

guardians_galaxy = media.Movie("Guardians of the Galaxy",
                               "A group of misfits join save the galaxy",
                               "https://upload.wikimedia.org/wikipedia/en/8/8f"
                               "/GOTG-poster.jpg",
                               "https://www.youtube.com/watch?v=d96cjJhvlMA")

kings_summer = media.Movie("The Kings of Summer",
                           "3 boys try to make it on their own in the woods",
                           "https://upload.wikimedia.org/wikipedia/en/7/7c"
                           "/The_Kings_of_Summer.jpg",
                           "https://www.youtube.com/watch?v=j4yg5qPhCKo")

gattaca = media.Movie("GATTACA",
                      "A Dystopian future based around genetic screening",
                      "https://upload.wikimedia.org/wikipedia/en/b/bb"
                      "/Gataca_Movie_Poster_B.jpg",
                      "https://www.youtube.com/watch?v=b68CEs8_oGI")

ex_machina = media.Movie("Ex_Machina",
                         "A frightening look into the future of AI",
                         "https://upload.wikimedia.org/wikipedia/en/b/ba"
                         "/Ex-machina-uk-poster.jpg",
                         "https://www.youtube.com/watch?v=84vfsHCe2M0")

arrival = media.Movie("Arrival",
                      "Alien visitors and a race against the clock",
                      "https://upload.wikimedia.org/wikipedia/en/d/df"
                      "/Arrival%2C_Movie_Poster.jpg",
                      "https://www.youtube.com/watch?v=SUiavMWW5Vo")

# Run the code to write movies to site and open
movies = [unbreakable, guardians_galaxy,
          kings_summer, gattaca, ex_machina, arrival]
fresh_tomatoes.open_movies_page(movies)
