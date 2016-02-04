import media
import fresh_tomatoes

# initialize movie
toy_story = media.Movie("Toystory",
                        "A story about a boy and his toys come to live",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

# initialize movie
avatar = media.Movie("Avatar",
                     "A group marine-guys on a planet with aliens",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# initialize movie
five_hundred_days_of_summer = media.Movie("500 days of Summer",
                                          "The film is presented in a nonlinea"
                                          "r narrative, jumping between variou"
                                          "s days within the 500 days of Tom a"
                                          "nd Summer's relationship.",
                                          "https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/Five_hundred_days_of_summer.jpg/220px-Five_hundred_days_of_summer.jpg",  # NOQA
                                          "https://www.youtube.com/watch?v=PsD0NpFSADM")  # NOQA

# Add each movie to the movies list
movies = [toy_story, avatar, five_hundred_days_of_summer]

# Generate the html-page
fresh_tomatoes.open_movies_page(movies)
