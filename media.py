import fresh_tomatoes
import movie

toy_story = movie.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")
# print(toy_story.storyline)
avatar = movie.Movie("Avatar",
                    "A marine on a alien planet",
                    "http://www.impawards.com/2009/posters/avatar.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()
enders_game = movie.Movie("Ender`s game",
                          "A kid that leaves earth to train for battle vs a ailen army",
                          "https://upload.wikimedia.org/wikipedia/en/8/8c/Ender's_Game_poster.jpg",
                          "https://www.youtube.com/watch?v=vP0cUBi4hwE")

movies = [toy_story, avatar, enders_game]
# fresh_tomatoes.open_movies_page(movies)
# print(movie.Movie.valid_ratings)
print(movie.Movie.__doc__)